"""PostToolUse hook: warn when Claude writes "AI slop" UI defaults.

Reads the hook JSON on stdin and checks only the text Claude just wrote (Write
content or Edit new_string) in UI files: navy and blue-slate colours, blue-tinted
grey pages, Tailwind slate/gray/indigo defaults, purple gradients, gradient text
and overused font families. Findings go back to Claude as additionalContext; the
hook never blocks. Rationale lives in ~/.claude/rules/ui-anti-slop.md.

Opt out per project with "env": {"UI_SLOP_CHECK": "off"} in .claude/settings.json.
Must stay compatible with /usr/bin/python3 (3.9) and use the stdlib only.
"""

import colorsys
import json
import math
import os
import re
import sys

UI_EXTS = {
    ".css", ".scss", ".sass", ".less", ".html", ".htm", ".jsx", ".tsx", ".js", ".ts",
    ".mjs", ".cjs", ".vue", ".svelte", ".astro", ".mdx",
}
SKIP_PARTS = ("/node_modules/", "/dist/", "/build/", "/.next/", "/.git/")
SKIP_SUFFIXES = ("schema.d.ts", ".min.css", ".min.js")
MAX_CHARS = 400_000
MAX_HITS = 10

DEFAULT_HEXES = {
    "#667eea": "the stock purple-blue gradient start",
    "#764ba2": "the stock purple-blue gradient end",
    "#6366f1": "Tailwind indigo-500",
    "#4f46e5": "Tailwind indigo-600",
    "#7c3aed": "Tailwind violet-600",
    "#8b5cf6": "Tailwind violet-500",
    "#5e6ad2": "the Linear indigo",
}

HEX_RE = re.compile(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b")
RGB_RE = re.compile(r"rgba?\(\s*(\d{1,3})[\s,]+(\d{1,3})[\s,]+(\d{1,3})")
HSL_RE = re.compile(r"hsla?\(\s*(-?[\d.]+)(?:deg)?[\s,]+([\d.]+)%[\s,]+([\d.]+)%")
# shadcn v3 style tokens: --background: 222.2 84% 4.9%;
BARE_HSL_RE = re.compile(r"--[\w-]+:\s*(-?[\d.]+)\s+([\d.]+)%\s+([\d.]+)%")
OKLCH_RE = re.compile(r"oklch\(\s*([\d.]+)(%?)\s+([\d.]+)\s+(-?[\d.]+)")

CLASS_RULES = [
    (
        re.compile(
            r"(?<![\w-])(?:bg|from|via|to|border|ring|fill|stroke|divide|outline)-"
            r"(?:slate|gray)-(?:800|900|950)\b"
        ),
        "Tailwind slate/gray 800-950 is navy",
    ),
    (
        re.compile(r"(?<![\w-])(?:bg|from|via|to)-(?:blue|indigo|sky)-(?:900|950)\b"),
        "navy surface",
    ),
    (
        re.compile(r"(?<![\w-])(?:from|via|to)-(?:indigo|violet|purple|fuchsia)-\d{2,3}\b"),
        "indigo/violet gradient",
    ),
]
FONT_NAMES_RE = re.compile(
    r"\b(Inter|Geist|Poppins|Roboto|Montserrat|Space Grotesk|Plus Jakarta Sans|DM Sans"
    r"|Outfit|Manrope|Sora)\b"
)
FONTSOURCE_RE = re.compile(
    r"@fontsource(?:-variable)?/(inter|geist|poppins|roboto|montserrat|space-grotesk"
    r"|plus-jakarta-sans|dm-sans|outfit|manrope|sora)\b"
)
FONT_CONTEXT_RE = re.compile(r"font|next/font|fonts\.googleapis|fonts\.bunny", re.I)


def rgb_from_hex(digits):
    if len(digits) in (3, 4):
        digits = "".join(c * 2 for c in digits[:3])
    digits = digits[:6]
    return tuple(int(digits[i : i + 2], 16) for i in (0, 2, 4))


def rgb_from_oklch(lightness, chroma, hue):
    a = chroma * math.cos(math.radians(hue))
    b = chroma * math.sin(math.radians(hue))
    l_ = lightness + 0.3963377774 * a + 0.2158037573 * b
    m_ = lightness - 0.1055613458 * a - 0.0638541728 * b
    s_ = lightness - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_**3, m_**3, s_**3
    linear = (
        4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )

    def encode(x):
        x = min(max(x, 0.0), 1.0)
        return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055

    return tuple(round(encode(x) * 255) for x in linear)


def classify(hue, sat, light):
    """hue in degrees, sat and light in 0..1."""
    if 195 <= hue <= 265 and sat > 0.12 and light < 0.28:
        return "navy / blue-slate (hue %d°, L %d%%)" % (hue, light * 100)
    if 200 <= hue <= 250 and sat > 0.15 and light > 0.93:
        return "blue-tinted grey, navy's light-mode twin (hue %d°)" % hue
    return None


def classify_rgb(rgb):
    r, g, b = (min(max(c, 0), 255) / 255 for c in rgb)
    h, light, sat = colorsys.rgb_to_hls(r, g, b)
    return classify(h * 360, sat, light)


def colour_hits(line):
    for m in HEX_RE.finditer(line):
        value = "#" + m.group(1)
        rgb = rgb_from_hex(m.group(1))
        known = DEFAULT_HEXES.get("#%02x%02x%02x" % rgb)
        reason = known or classify_rgb(rgb)
        if reason:
            yield value, reason
    for m in RGB_RE.finditer(line):
        reason = classify_rgb(tuple(int(x) for x in m.groups()))
        if reason:
            yield m.group(0) + ")", reason
    for regex in (HSL_RE, BARE_HSL_RE):
        for m in regex.finditer(line):
            hue, sat, light = (float(x) for x in m.groups())
            reason = classify(hue % 360, sat / 100, light / 100)
            if reason:
                yield m.group(0), reason
    for m in OKLCH_RE.finditer(line):
        lightness = float(m.group(1)) / (100 if m.group(2) else 1)
        reason = classify_rgb(
            rgb_from_oklch(lightness, float(m.group(3)), float(m.group(4)))
        )
        if reason:
            yield m.group(0) + ")", reason


def other_hits(line):
    for regex, reason in CLASS_RULES:
        for m in regex.finditer(line):
            yield m.group(0), reason
    if "bg-clip-text" in line and "text-transparent" in line:
        yield "bg-clip-text text-transparent", "gradient text"
    for m in FONTSOURCE_RE.finditer(line):
        yield m.group(0), "overused default font"
    if FONT_CONTEXT_RE.search(line):
        for m in FONT_NAMES_RE.finditer(line.replace("+", " ")):
            yield m.group(0), "overused default font"


def is_ui_file(path):
    lowered = path.lower()
    if any(part in lowered for part in SKIP_PARTS) or lowered.endswith(SKIP_SUFFIXES):
        return False
    name = os.path.basename(lowered)
    return name.startswith("tailwind.config.") or os.path.splitext(name)[1] in UI_EXTS


def line_offset(path, snippet):
    """Line number of the snippet's first line inside the edited file (0-based)."""
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            content = fh.read()
    except OSError:
        return None
    index = content.find(snippet)
    return None if index < 0 else content.count("\n", 0, index)


def main():
    if os.environ.get("UI_SLOP_CHECK", "").lower() in ("off", "0", "false", "no"):
        return
    try:
        payload = json.load(sys.stdin)
    except ValueError:
        return
    tool = payload.get("tool_name")
    tool_input = payload.get("tool_input") or {}
    path = tool_input.get("file_path") or ""
    if tool == "Write":
        text = tool_input.get("content") or ""
        offset = 0
    elif tool == "Edit":
        text = tool_input.get("new_string") or ""
        offset = line_offset(path, text)
    else:
        return
    if not text or not path or not is_ui_file(path) or len(text) > MAX_CHARS:
        return

    hits, seen = [], set()
    for number, line in enumerate(text.splitlines(), start=1):
        for value, reason in list(colour_hits(line)) + list(other_hits(line)):
            if (value.lower(), reason) in seen:
                continue
            seen.add((value.lower(), reason))
            where = "L%d" % (number + offset) if offset is not None else "new text"
            hits.append("- %s `%s`: %s" % (where, value, reason))
    if not hits:
        return

    shown = hits[:MAX_HITS]
    if len(hits) > MAX_HITS:
        shown.append("- …and %d more" % (len(hits) - MAX_HITS))
    cwd = payload.get("cwd") or ""
    display = os.path.relpath(path, cwd) if cwd and path.startswith(cwd) else path
    message = "\n".join(
        ["UI slop check on %s (see ~/.claude/rules/ui-anti-slop.md):" % display]
        + shown
        + [
            "Replace these with colours and type chosen for this subject, or say why the "
            "brief or the project's design system requires them."
        ]
    )
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": message,
            }
        },
        sys.stdout,
    )


if __name__ == "__main__":
    try:
        main()
    except Exception:  # a broken check must never get in the way of an edit
        pass
