"""Check a palette against the comfort floor in references/comfort.md.

Usage: palette-check.py [--strict] ROLE[:name]=#HEX ...

Roles: ground, surface, ink, muted, accent, primary, signal, and the same with a
"dark-" prefix for a dark theme. Each theme needs exactly one ground; every other
token is measured against it. The "#" is optional; quote the tokens if your shell
treats "#" specially. Example:

  palette-check.py 'ground:wax=#F8F7F3' 'ink:soot=#2A2420' 'primary:soga=#8A4B22' \
      'accent:vat=#3D5E86' 'signal:leaf=#467748'

Prints OKLCH, the WCAG 2 contrast ratio and the APCA Lc of each token against its
ground, then the findings. FAIL means a WCAG 2 AA minimum is missed. WARN means
the token sits outside the comfort floor, whose numbers are heuristics. Ratios
and Lc values are printed rounded down, so a printed value never looks like a
pass that failed. Exits 1 on any FAIL (or any WARN with --strict), 2 on a usage
error, 0 otherwise.
Must stay compatible with /usr/bin/python3 (3.9) and use the stdlib only.
"""

import argparse
import collections
import math
import re
import sys

ROLES = ("ground", "surface", "ink", "muted", "accent", "primary", "signal")
NEUTRAL_ROLES = ("ground", "surface", "ink", "muted")
COLOUR_ROLES = ("accent", "primary")
TOKEN_RE = re.compile(
    r"^(dark-)?([a-z]+)(?::([\w.-]+))?=#?([0-9a-f]{6}|[0-9a-f]{3})$", re.IGNORECASE
)

# The comfort floor (references/comfort.md). OKLCH lightness and chroma.
GROUND_L = {"light": (0.96, 1.0), "dark": (0.15, 0.24)}
GROUND_MAX_C = {"light": 0.015, "dark": 0.02}
CREAM_MIN_C = 0.008  # from here a light ground at hue 60-100 reads as beige or cream
# Light surfaces may sit either side of the ground; dark surfaces rise (lighter).
SURFACE_STEP = {"light": (0.02, 0.06), "dark": (0.03, 0.05)}
SURFACE_MAX_C = 0.02
INK_L = {"light": (0.18, 0.35), "dark": (0.88, 0.94)}
INK_MAX_C = 0.03
ACCENT_C = {"light": (0.07, 0.20), "dark": (0.07, 0.14)}
DARK_ACCENT_MIN_L = 0.70
BODY_RATIO, AA_TEXT, AA_NON_TEXT = 7.0, 4.5, 3.0
BODY_LC, MUTED_LC = 75, 60
SATURATED_C = 0.12
CORE_CAP = 4  # 2-3 core colours + 1 accent; neutrals and status colours don't count
ACHROMATIC_C = 0.002  # below this chroma a hue means nothing
# OKLCH hues of the navy, slate and blue-grey family: #0F172A is 266°, #F1F5F9 248°.
BLUE_HUES = (220, 290)
BEIGE_HUES = (60, 100)

Token = collections.namedtuple("Token", "theme role name hex rgb l c h")


def rgb_from_hex(digits):
    if len(digits) == 3:
        digits = "".join(c * 2 for c in digits)
    return tuple(int(digits[i : i + 2], 16) / 255 for i in (0, 2, 4))


def linear(channel):
    if channel <= 0.04045:
        return channel / 12.92
    return ((channel + 0.055) / 1.055) ** 2.4


def oklch(rgb):
    """OKLCH of an sRGB triple in 0..1 (Björn Ottosson's OKLab)."""
    r, g, b = (linear(c) for c in rgb)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = (math.copysign(abs(x) ** (1 / 3), x) for x in (l, m, s))
    lightness = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    b = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    return lightness, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


def luminance(rgb):
    return sum(k * linear(c) for k, c in zip((0.2126, 0.7152, 0.0722), rgb))


def wcag_ratio(rgb_a, rgb_b):
    high, low = sorted((luminance(rgb_a), luminance(rgb_b)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def apca_lc(text_rgb, ground_rgb):
    """APCA-W3 0.0.98G contrast of text on a ground; negative for light text on dark."""

    def screen_y(rgb):
        y = sum(k * c**2.4 for k, c in zip((0.2126729, 0.7151522, 0.0721750), rgb))
        return y + (0.022 - y) ** 1.414 if y < 0.022 else y

    text, ground = screen_y(text_rgb), screen_y(ground_rgb)
    if abs(ground - text) < 0.0005:
        return 0.0
    if ground > text:
        sapc = (ground**0.56 - text**0.57) * 1.14
        return 0.0 if sapc < 0.1 else (sapc - 0.027) * 100
    sapc = (ground**0.65 - text**0.62) * 1.14
    return 0.0 if sapc > -0.1 else (sapc + 0.027) * 100


def floor_to(value, places):
    """Round down for display, so 4.499 never prints as a passing 4.50."""
    factor = 10**places
    return math.floor(value * factor + 1e-9) / factor


def fmt_ratio(ratio):
    return "%.2f:1" % floor_to(ratio, 2)


def fmt_lc(lc):
    return "Lc %.1f" % floor_to(abs(lc), 1)


def hue_distance(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


def in_range(value, bounds):
    return bounds[0] <= value <= bounds[1]


def is_blue_tinted(token):
    # Light blue-greys carry very little chroma: Tailwind gray-50 #F9FAFB is C 0.0017.
    min_c = 0.0015 if token.l > 0.9 else 0.003
    return token.c >= min_c and in_range(token.h, BLUE_HUES)


def parse_token(text):
    m = TOKEN_RE.match(text.strip())
    if not m:
        raise ValueError("expected ROLE[:name]=#HEX with a 3- or 6-digit hex, got %r" % text)
    dark, role, name, digits = m.groups()
    role = role.lower()
    if role not in ROLES:
        raise ValueError("unknown role %r in %r (roles: %s)" % (role, text, ", ".join(ROLES)))
    rgb = rgb_from_hex(digits)
    hexcode = "#" + "".join("%02X" % round(c * 255) for c in rgb)
    return Token("dark" if dark else "light", role, name or role, hexcode, rgb, *oklch(rgb))


def label(token):
    role = ("dark-" if token.theme == "dark" else "") + token.role
    name = "" if token.name == token.role else " " + token.name
    return "%s%s %s" % (role, name, token.hex)


def check_ground(ground):
    theme, found = ground.theme, []
    if ground.hex == "#000000":
        found.append(("WARN", "%s: pure black ground; lift it to L %.2f-%.2f"
                      % (label(ground), *GROUND_L["dark"])))
    elif not in_range(ground.l, GROUND_L[theme]):
        found.append(("WARN", "%s: L %.3f is outside the %s-ground band %.2f-%.2f"
                      % (label(ground), ground.l, theme, *GROUND_L[theme])))
    if theme == "light" and ground.c >= CREAM_MIN_C and in_range(ground.h, BEIGE_HUES):
        found.append(("WARN", "%s: chroma %.3f at hue %.0f° reads as a beige or cream page, the "
                      "second-wave tell, unless the brief asks for it; keep warm tints under C %.3f"
                      % (label(ground), ground.c, ground.h, CREAM_MIN_C)))
    elif ground.c > GROUND_MAX_C[theme]:
        found.append(("WARN", "%s: chroma %.3f > %.3f reads as a coloured page, not a tinted one"
                      % (label(ground), ground.c, GROUND_MAX_C[theme])))
    return found


def check_surface(token, ground):
    found = []
    step = token.l - ground.l
    low, high = SURFACE_STEP[token.theme]
    if token.theme == "dark" and not in_range(step, (low, high)):
        found.append(("WARN", "%s: lightness step %+.3f from the ground; dark surfaces rise by "
                      "L +%.2f to +%.2f" % (label(token), step, low, high)))
    elif token.theme == "light" and not in_range(abs(step), (low, high)):
        found.append(("WARN", "%s: lightness step %+.3f from the ground is outside ±%.2f-%.2f"
                      % (label(token), step, low, high)))
    if token.c > SURFACE_MAX_C:
        found.append(("WARN", "%s: chroma %.3f > %.2f on a large area"
                      % (label(token), token.c, SURFACE_MAX_C)))
    return found


def check_token(token, ground, label_colours):
    if token.role == "surface":
        return check_surface(token, ground)
    ratio = wcag_ratio(token.rgb, ground.rgb)
    lc = abs(apca_lc(token.rgb, ground.rgb))
    where = "%s / %s on the ground" % (fmt_ratio(ratio), fmt_lc(lc))
    found = []
    if token.role == "ink":
        if ratio < AA_TEXT:
            found.append(("FAIL", "%s: %s, below %.1f:1 for text" % (label(token), where, AA_TEXT)))
        elif ratio < BODY_RATIO or lc < BODY_LC:
            found.append(("WARN", "%s: %s; body text wants %.0f:1 and Lc %d+"
                          % (label(token), where, BODY_RATIO, BODY_LC)))
        if token.hex in ("#000000", "#FFFFFF"):
            found.append(("WARN", "%s: pure %s text glares; use L %.2f-%.2f"
                          % (label(token), "black" if token.hex == "#000000" else "white",
                             *INK_L[token.theme])))
        elif not in_range(token.l, INK_L[token.theme]):
            found.append(("WARN", "%s: L %.3f is outside the ink band %.2f-%.2f"
                          % (label(token), token.l, *INK_L[token.theme])))
        if token.c > INK_MAX_C:
            found.append(("WARN", "%s: chroma %.3f > %.2f for body text"
                          % (label(token), token.c, INK_MAX_C)))
    elif token.role == "muted":
        if ratio < AA_TEXT:
            found.append(("FAIL", "%s: %s, below %.1f:1 for text" % (label(token), where, AA_TEXT)))
        elif lc < MUTED_LC:
            found.append(("WARN", "%s: %s; secondary text wants Lc %d+"
                          % (label(token), where, MUTED_LC)))
    else:  # accent, primary, signal
        if ratio < AA_NON_TEXT:
            found.append(("FAIL", "%s: %s, below %.1f:1 for a fill or icon (and %.1f:1 as text)"
                          % (label(token), where, AA_NON_TEXT, AA_TEXT)))
        elif ratio < AA_TEXT and token.role in COLOUR_ROLES:
            found.append(("WARN", "%s: %s is enough for a fill or icon, but text and links in it "
                          "need %.1f:1" % (label(token), where, AA_TEXT)))
        if token.role == "accent":
            low, high = ACCENT_C[token.theme]
            if token.c > high:
                found.append(("WARN", "%s: chroma %.3f > %.2f; calm the accent"
                              % (label(token), token.c, high)))
            elif token.c < low:
                found.append(("WARN", "%s: chroma %.3f < %.2f is too grey to work as an accent"
                              % (label(token), token.c, low)))
        elif token.role == "primary" and token.c > ACCENT_C[token.theme][1]:
            found.append(("WARN", "%s: chroma %.3f > %.2f; calm the primary"
                          % (label(token), token.c, ACCENT_C[token.theme][1])))
        if token.role in COLOUR_ROLES and token.theme == "dark" and token.l < DARK_ACCENT_MIN_L:
            found.append(("WARN", "%s: L %.3f; on dark, lighten accents to L %.2f+"
                          % (label(token), token.l, DARK_ACCENT_MIN_L)))
        if token.role == "primary":
            best = max(label_colours, key=lambda t: wcag_ratio(t.rgb, token.rgb))
            best_ratio = wcag_ratio(best.rgb, token.rgb)
            if best_ratio < AA_TEXT:
                found.append(("WARN", "%s: no label colour reaches %.1f:1 on this fill; the best "
                              "is %s at %s" % (label(token), AA_TEXT, best.hex,
                                               fmt_ratio(best_ratio))))
    return found


def check_theme(tokens, brand_is_blue):
    ground = next(t for t in tokens if t.role == "ground")
    white = Token(ground.theme, "label", "white", "#FFFFFF", (1.0, 1.0, 1.0), 1.0, 0.0, 0.0)
    label_colours = [ground, white] + [t for t in tokens if t.role == "ink"]
    found = check_ground(ground)
    for token in tokens:
        if token is not ground:
            found.extend(check_token(token, ground, label_colours))

    for token in tokens:
        # A blue brand may tint its text blue; its grounds and surfaces still may not.
        exempt = brand_is_blue and token.role in ("ink", "muted")
        if token.role in NEUTRAL_ROLES and is_blue_tinted(token) and not exempt:
            found.append(("WARN", "%s: hue %.0f° tints this neutral blue (the navy and slate "
                          "family); tint it toward the brand's own hue" % (label(token), token.h)))

    colours = [t for t in tokens if t.role in COLOUR_ROLES
               or (t.role in NEUTRAL_ROLES and t.c > 0.05)]
    if len({t.hex for t in colours}) > CORE_CAP:
        found.append(("WARN", "%d colours besides neutrals and status colours; the floor is 2-3 "
                      "core colours + 1 accent" % len({t.hex for t in colours})))
    saturated = [t for t in colours + [t for t in tokens if t.role == "signal"]
                 if t.c > SATURATED_C]
    for i, a in enumerate(saturated):
        for b in saturated[i + 1 :]:
            if a.role == b.role == "signal" or a.hex == b.hex:
                continue  # status colours rarely touch; the same colour can't vibrate
            if hue_distance(a.h, b.h) >= 90 and abs(a.l - b.l) < 0.2:
                found.append(("WARN", "%s and %s: two saturated hues %.0f° apart at similar "
                              "lightness vibrate side by side or as text on each other"
                              % (label(a), label(b), hue_distance(a.h, b.h))))
    return found


def report(tokens_by_theme, out):
    width = max([4] + [len(t.name) for ts in tokens_by_theme.values() for t in ts])
    row = "%-6s %-8s %-*s %-7s  %-5s  %-5s  %-3s  %-8s %s\n"
    out.write(row % ("theme", "role", width, "name", "hex", "L", "C", "h", "ratio", "APCA"))
    for theme, tokens in tokens_by_theme.items():
        ground = next(t for t in tokens if t.role == "ground")
        for t in tokens:
            hue = "-" if t.c < ACHROMATIC_C else "%.0f" % t.h
            if t is ground:
                ratio, lc = "-", "-"
            else:
                ratio = fmt_ratio(wcag_ratio(t.rgb, ground.rgb))
                lc = fmt_lc(apca_lc(t.rgb, ground.rgb))
            out.write(row % (theme, t.role, width, t.name, t.hex, "%.3f" % t.l, "%.3f" % t.c,
                             hue, ratio, lc))


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check palette tokens against the comfort floor (references/comfort.md).")
    parser.add_argument("tokens", nargs="+", metavar="ROLE[:name]=#HEX")
    parser.add_argument("--strict", action="store_true", help="exit 1 on warnings too")
    args = parser.parse_args(argv)

    tokens_by_theme, seen = collections.OrderedDict(), set()
    for text in args.tokens:
        try:
            token = parse_token(text)
        except ValueError as exc:
            parser.error(str(exc))
        key = (token.theme, token.role, token.name.lower())
        if key in seen:
            parser.error("duplicate token %s; give one of them another name (ROLE:name=#HEX)"
                         % label(token))
        seen.add(key)
        tokens_by_theme.setdefault(token.theme, []).append(token)
    for theme, tokens in tokens_by_theme.items():
        grounds = [t for t in tokens if t.role == "ground"]
        prefix = "dark-" if theme == "dark" else ""
        if len(grounds) != 1:
            parser.error("the %s theme needs exactly one %sground token" % (theme, prefix))
        ground = grounds[0]
        if theme == "light" and ground.l < 0.5:
            parser.error("ground %s is dark (L %.2f); give a dark theme with dark-ground, "
                         "dark-ink and the other dark- roles" % (ground.hex, ground.l))
        if theme == "dark" and ground.l > 0.5:
            parser.error("dark-ground %s is light (L %.2f); give a light theme with ground, ink "
                         "and the other roles without the dark- prefix" % (ground.hex, ground.l))

    brand_is_blue = any(t.role in COLOUR_ROLES and in_range(t.h, BLUE_HUES) and t.c > 0.05
                        for tokens in tokens_by_theme.values() for t in tokens)
    findings = []
    for tokens in tokens_by_theme.values():
        findings.extend(check_theme(tokens, brand_is_blue))

    report(tokens_by_theme, sys.stdout)
    sys.stdout.write("\n")
    for level, message in findings:
        sys.stdout.write("%s %s\n" % (level, message))
    fails = sum(1 for level, _ in findings if level == "FAIL")
    warns = len(findings) - fails
    sys.stdout.write("%sResult: %d fail, %d warning%s\n"
                     % ("\n" if findings else "", fails, warns, "" if warns == 1 else "s"))
    return 1 if fails or (args.strict and warns) else 0


if __name__ == "__main__":
    sys.exit(main())
