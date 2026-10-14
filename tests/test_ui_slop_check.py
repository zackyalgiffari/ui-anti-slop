"""Tests for scripts/ui-slop-check.py, run the way Claude Code runs the hook.

Each test pipes a PostToolUse payload into the script and inspects what it
prints. Run with: python3 -m unittest discover -s tests -v
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest

SCRIPT = os.path.join(os.path.dirname(__file__), os.pardir, "scripts", "ui-slop-check.py")


def run_hook(payload, env_extra=None):
    env = dict(os.environ)
    env.pop("UI_SLOP_CHECK", None)
    env.update(env_extra or {})
    stdin = payload if isinstance(payload, str) else json.dumps(payload)
    result = subprocess.run(
        [sys.executable, "-I", SCRIPT],
        input=stdin,
        capture_output=True,
        text=True,
        env=env,
        check=False,
    )
    return result


def write(path, content, cwd="/project"):
    return {"tool_name": "Write", "cwd": cwd, "tool_input": {"file_path": path, "content": content}}


def context_of(result):
    """The additionalContext text, or None when the hook stayed silent."""
    if not result.stdout.strip():
        return None
    output = json.loads(result.stdout)
    hook = output["hookSpecificOutput"]
    assert hook["hookEventName"] == "PostToolUse"
    return hook["additionalContext"]


class NavyAndGradients(unittest.TestCase):
    def test_tsx_write_flags_slate_gradient_and_navy_hex(self):
        content = (
            '<div className="bg-slate-900 text-white">\n'
            '<h1 className="bg-gradient-to-r from-indigo-500 to-purple-600 '
            'bg-clip-text text-transparent">Hi</h1>\n'
            'const ink = "#0F172A";\n'
            "</div>"
        )
        result = run_hook(write("/project/src/Hero.tsx", content))
        self.assertEqual(result.returncode, 0)
        text = context_of(result)
        self.assertIn("src/Hero.tsx", text)
        self.assertIn("L1 `bg-slate-900`", text)
        self.assertIn("`from-indigo-500`: indigo/violet gradient", text)
        self.assertIn("`to-purple-600`: indigo/violet gradient", text)
        self.assertIn("gradient text", text)
        self.assertIn("L3 `#0F172A`: navy / blue-slate", text)

    def test_edit_reports_line_in_the_edited_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "page.css")
            with open(path, "w") as fh:
                fh.write(".page { background: #f6f6f2; }\n.x { color: #F5F6FA; }\n")
            payload = {
                "tool_name": "Edit",
                "cwd": tmp,
                "tool_input": {
                    "file_path": path,
                    "old_string": "x",
                    "new_string": ".x { color: #F5F6FA; }",
                },
            }
            text = context_of(run_hook(payload))
        self.assertIn("page.css", text)
        self.assertIn("L2 `#F5F6FA`: blue-tinted grey", text)

    def test_shadcn_bare_hsl_oklch_and_dark_variants(self):
        content = (
            "--background: 222.2 84% 4.9%;\n"
            "--card: oklch(0.21 0.034 264.7);\n"
            '<div className="dark:bg-gray-950/80">'
        )
        text = context_of(run_hook(write("/project/src/index.css", content)))
        self.assertIn("`--background: 222.2 84% 4.9%`: navy", text)
        self.assertIn("`oklch(0.21 0.034 264.7)`: navy", text)
        self.assertIn("`bg-gray-950`", text)

    def test_known_default_hexes(self):
        text = context_of(run_hook(write("/project/a.css", "a { color: #6366f1; }")))
        self.assertIn("Tailwind indigo-500", text)


class Fonts(unittest.TestCase):
    def test_default_fonts_in_font_contexts(self):
        content = (
            'font-family: "Inter", sans-serif;\n'
            '@import "@fontsource-variable/geist";\n'
            '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans">\n'
        )
        text = context_of(run_hook(write("/project/index.css", content)))
        self.assertIn("`Inter`: overused default font", text)
        self.assertIn("`@fontsource-variable/geist`", text)
        self.assertIn("`Plus Jakarta Sans`", text)

    def test_seeded_second_wave_fonts(self):
        content = (
            '<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1">\n'
            '<link href="https://api.fontshare.com/v2/css?f[]=satoshi@400,700&f[]=clash-display@600">\n'
            '@import "@fontsource/fraunces";\n'
        )
        text = context_of(run_hook(write("/project/index.html", content)))
        self.assertIn("`Instrument Serif`", text)
        self.assertIn("`satoshi`", text)
        self.assertIn("`clash-display`", text)
        self.assertIn("`@fontsource/fraunces`", text)

    def test_word_inter_outside_font_context_is_ignored(self):
        content = "const interval = 3; // Inter-process timer"
        self.assertIsNone(context_of(run_hook(write("/project/timer.ts", content))))


class Svg(unittest.TestCase):
    def test_logo_svg_flags_navy_fill_and_live_text_font(self):
        content = (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">\n'
            '<rect width="256" height="256" rx="48" fill="#0F172A"/>\n'
            '<text x="128" y="160" font-family="Inter" fill="#fff">A</text>\n'
            "</svg>"
        )
        text = context_of(run_hook(write("/project/brand/logo.svg", content)))
        self.assertIn("brand/logo.svg", text)
        self.assertIn("L2 `#0F172A`: navy / blue-slate", text)
        self.assertIn("L3 `Inter`: overused default font", text)

    def test_clean_svg_mark_is_silent(self):
        content = (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" role="img">\n'
            "<title>Mark</title>\n"
            '<path fill="#2E3B1F" fill-rule="evenodd" d="M32 32h192v192H32zM96 96v64h64V96z"/>\n'
            '<path fill="#B5562A" d="M120 120h16v16h-16z"/>\n'
            "</svg>"
        )
        self.assertIsNone(context_of(run_hook(write("/project/brand/mark.svg", content))))


class Silence(unittest.TestCase):
    def test_clean_palette_is_silent(self):
        content = ":root{--bg:#F3F4EF;--ink:#1C2420;--lamp:#F5A524;--booth:#0F1612}"
        self.assertIsNone(context_of(run_hook(write("/project/a.css", content))))

    def test_non_ui_files_are_ignored(self):
        for path in ("/project/notes.md", "/project/themes.py", "/project/node_modules/x/a.css"):
            with self.subTest(path=path):
                result = run_hook(write(path, "#0F172A bg-slate-900"))
                self.assertIsNone(context_of(result))

    def test_opt_out_env_var(self):
        result = run_hook(write("/project/a.tsx", "bg-slate-900"), {"UI_SLOP_CHECK": "off"})
        self.assertIsNone(context_of(result))

    def test_other_tools_are_ignored(self):
        payload = {"tool_name": "Read", "tool_input": {"file_path": "/project/a.css"}}
        self.assertIsNone(context_of(run_hook(payload)))

    def test_garbage_stdin_exits_cleanly(self):
        result = run_hook("not json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")


class Limits(unittest.TestCase):
    def test_hits_are_capped(self):
        lines = "\n".join("c%d { color: #0F17%02X; }" % (i, i + 0x20) for i in range(15))
        text = context_of(run_hook(write("/project/many.css", lines)))
        self.assertIn("…and 5 more", text)


if __name__ == "__main__":
    unittest.main()
