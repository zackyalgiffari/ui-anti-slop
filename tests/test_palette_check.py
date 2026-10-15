"""Tests for scripts/palette-check.py.

The formula tests import the script; the rest run it the way the skill does.
Run with: python3 -m unittest discover -s tests -v
"""

import importlib.util
import os
import subprocess
import sys
import unittest

SCRIPT = os.path.join(os.path.dirname(__file__), os.pardir, "scripts", "palette-check.py")

# The worked example in references/colour.md, both themes.
CALM = [
    "ground:wax=#F8F7F3", "surface:cambric=#FFFFFF", "ink:soot=#2A2420", "muted:ash=#6B635B",
    "primary:soga=#8A4B22", "accent:vat=#3D5E86", "signal:leaf=#467748",
    "dark-ground:soot=#1C1612", "dark-surface:char=#26201C", "dark-ink:wax=#E4E1DB",
    "dark-muted:ash=#BCB6AF", "dark-primary:soga=#D1966D", "dark-accent:vat=#84AFDC",
    "dark-signal:leaf=#76AF77",
]


def load_module():
    spec = importlib.util.spec_from_file_location("palette_check", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(*args):
    return subprocess.run(
        [sys.executable, "-I", SCRIPT, *args], capture_output=True, text=True, check=False
    )


class Formulas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pc = load_module()

    def rgb(self, hexcode):
        return self.pc.rgb_from_hex(hexcode.lstrip("#"))

    def test_apca_matches_the_reference_values(self):
        cases = [
            ("#888888", "#FFFFFF", 63.06),
            ("#FFFFFF", "#888888", -68.54),
            ("#000000", "#AAAAAA", 58.15),
            ("#AAAAAA", "#000000", -56.24),
        ]
        for text, ground, expected in cases:
            with self.subTest(text=text, ground=ground):
                lc = self.pc.apca_lc(self.rgb(text), self.rgb(ground))
                self.assertAlmostEqual(lc, expected, places=2)

    def test_wcag_ratio(self):
        self.assertAlmostEqual(self.pc.wcag_ratio(self.rgb("#000"), self.rgb("#FFF")), 21.0)
        self.assertAlmostEqual(
            self.pc.wcag_ratio(self.rgb("#767676"), self.rgb("#FFFFFF")), 4.54, places=2
        )

    def test_oklch(self):
        lightness, chroma, _ = self.pc.oklch(self.rgb("#FFFFFF"))
        self.assertAlmostEqual(lightness, 1.0, places=4)
        self.assertLess(chroma, 0.001)
        lightness, chroma, hue = self.pc.oklch(self.rgb("#0F172A"))
        self.assertAlmostEqual(lightness, 0.208, places=3)
        self.assertAlmostEqual(chroma, 0.040, places=3)
        self.assertAlmostEqual(hue, 266, delta=1)


class Palettes(unittest.TestCase):
    def test_worked_example_is_clean(self):
        result = run(*CALM)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("Result: 0 fail, 0 warnings", result.stdout)
        self.assertIn("light  ink      soot    #2A2420  0.266  0.012  56   14.28:1", result.stdout)
        self.assertIn("light  surface  cambric #FFFFFF  1.000  0.000  -    1.07:1", result.stdout)

    def test_slop_palette_reports_each_finding(self):
        result = run(
            "ground=#EFE8D8", "surface=#E2D3B5", "ink=#000000", "muted=#A39E93",
            "primary=#E0301E", "accent=#1F4FE0", "accent:cyan=#00D1FF", "signal=#B8D6A0",
            "dark-ground=#0F172A", "dark-ink=#FFFFFF", "dark-accent=#6366F1",
        )
        self.assertEqual(result.returncode, 1)
        out = result.stdout
        expected = [
            "WARN ground #EFE8D8: L 0.932 is outside the light-ground band",
            "second-wave tell",
            "WARN surface #E2D3B5: chroma 0.043 > 0.02 on a large area",
            "WARN ink #000000: pure black text glares",
            "FAIL muted #A39E93: 2.18:1",
            "WARN primary #E0301E: chroma 0.213 > 0.20",
            "FAIL accent cyan #00D1FF: 1.48:1",
            "FAIL signal #B8D6A0",
            "vibrate side by side",
            "WARN dark-ground #0F172A: hue 266° tints this neutral blue",
            "WARN dark-ink #FFFFFF: pure white text glares",
            "WARN dark-accent #6366F1: L 0.585; on dark, lighten accents",
            "Result: 3 fail,",
        ]
        for text in expected:
            with self.subTest(text=text):
                self.assertIn(text, out)

    def test_cream_ground(self):
        result = run("ground=#F7F4ED", "ink=#2A2420")
        self.assertIn("WARN ground #F7F4ED: chroma 0.010 at hue 87° reads as a beige or cream", result.stdout)

    def test_blue_brand_does_not_excuse_blue_surfaces(self):
        result = run("dark-ground=#1C1612", "dark-surface=#1D2129", "dark-ink=#E4E1DB",
                     "dark-accent=#84AFDC")
        self.assertIn("WARN dark-surface #1D2129: hue 264° tints this neutral blue", result.stdout)

    def test_tailwind_gray_50_is_blue(self):
        result = run("ground=#F9FAFB", "ink=#222222")
        self.assertIn("WARN ground #F9FAFB: hue 248° tints this neutral blue", result.stdout)

    def test_dark_surfaces_must_rise(self):
        out = run("dark-ground=#1C1612", "dark-surface=#221C18", "dark-ink=#E4E1DB").stdout
        self.assertIn("step +0.026 from the ground; dark surfaces rise by L +0.03 to +0.05", out)
        out = run("dark-ground=#1C1612", "dark-surface=#110C09", "dark-ink=#E4E1DB").stdout
        self.assertIn("dark surfaces rise", out)

    def test_printed_ratios_round_down(self):
        out = run("ground=#FFFFFF", "muted=#168484", "accent=#24A5A5").stdout
        self.assertIn("FAIL muted #168484: 4.49:1", out)
        self.assertIn("FAIL accent #24A5A5: 2.99:1", out)

    def test_accent_and_primary_text_contrast(self):
        out = run("ground=#FFFFFF", "ink=#2A2A2A", "primary=#5B8A8A", "accent=#7A7F84").stdout
        self.assertIn("is enough for a fill or icon, but text and links in it need 4.5:1", out)
        self.assertIn("no label colour reaches 4.5:1 on this fill; the best is #FFFFFF", out)
        self.assertIn("is too grey to work as an accent", out)

    def test_signal_next_to_primary_can_vibrate(self):
        out = run("ground=#FFFFFF", "ink=#2A2A2A", "primary=#1F5FD0", "signal=#D0362B").stdout
        self.assertIn("primary #1F5FD0 and signal #D0362B: two saturated hues", out)

    def test_greys_print_no_hue(self):
        out = run("ground=#FFFFFF", "ink=#222222").stdout
        self.assertIn("ink      ink    #222222  0.252  0.000  -    15.90:1", out)

    def test_input_is_case_insensitive_and_names_may_have_dots(self):
        result = run("GROUND=#ffffff", "Ink:body.text=#222")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("body.text", result.stdout)

    def test_palette_cap(self):
        result = run(
            "ground=#FAFAF7", "ink=#2A2420", "primary=#8A4B22", "accent=#3D5E86",
            "accent:moss=#4E6B2E", "accent:plum=#6B2E5E", "accent:ochre=#8A6A12",
        )
        self.assertIn("5 colours besides neutrals and status colours", result.stdout)

    def test_strict_fails_on_warnings(self):
        tokens = ["ground=#FFFFFF", "ink=#000000"]
        self.assertEqual(run(*tokens).returncode, 0)
        self.assertEqual(run("--strict", *tokens).returncode, 1)


class Usage(unittest.TestCase):
    def test_usage_errors_exit_2(self):
        cases = [
            ["ink=#222222"],
            ["ground=#FFFFFF", "ground:paper=#FAFAFA"],
            ["ground=#FFFFFF", "headline=#222222"],
            ["ground=#FFFFFF", "ink=#22"],
            ["ground=#FFFFFF", "ink=#22222280"],
            ["ground=#FFFFFF", "ink=#222222", "ink=#333333"],
            ["ground=#1C1612", "ink=#E4E1DB"],
            ["dark-ground=#F8F7F3", "dark-ink=#2A2420"],
        ]
        for args in cases:
            with self.subTest(args=args):
                result = run(*args)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn("error:", result.stderr)


if __name__ == "__main__":
    unittest.main()
