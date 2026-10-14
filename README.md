# ui-anti-slop

A Claude Code skill, rule and hook that stop generated UIs and brand assets from falling back on
AI-slop defaults. The skill walks any design job through a general process, scaled to the job:

**theme → colour → type → logo (hand-drawn SVG) → assets → layout → surfaces → motion → copy**

Each step comes with a method and the defaults to avoid. The main target is the navy / blue-slate
dark mode and its blue-tinted grey light twin. The rest of the family is covered too:
- indigo and purple gradients
- Inter, Geist and the "distinctive" fonts prompting guides seeded (Instrument Serif, Fraunces,
  Satoshi…)
- AI-ring and hexagon logos, and the ✨ sparkle
- stock icon sets and Corporate Memphis illustration
- the centred hero over three identical cards, and the rounded-2xl card kit
- glassmorphism, glow orbs and pure-black shadows
- template chrome
- "Unlock the power of…" copy

The rules come from Figma Community, published critiques of vibe-coded design, and the tokens of
real design systems (Atlassian, Primer, Polaris, Carbon). See
[references/research.md](references/research.md).

## What's inside

| Path | Component | When it acts |
|---|---|---|
| `rules/ui-anti-slop.md` | Always-on rule | Loaded into every Claude Code session from `~/.claude/rules/`. It holds the bans and what to do instead, so they apply even while discussing a design before any file exists. |
| `SKILL.md` | Skill | Loaded when Claude works on UI or brand assets. The step-by-step process, the guardrails, a design-brief template and a self-check. |
| `references/` | Skill references | One file per step (`theme`, `colour`, `typography`, `logo-svg`, `assets`, `layout`, `surfaces`, `motion-and-copy`), opened when Claude reaches that step, plus `research.md` with the evidence and sources. |
| `assets/logo-preview.html` | Logo preview sheet | A self-contained page. Claude pastes an SVG logo in and screenshots it: sizes 16–256 px, the real 16/32 px rasterisation, one-colour and reversed versions, mirrored and rotated, a grid overlay, a favicon in browser tabs, and a lint panel for the SVG rules. |
| `scripts/ui-slop-check.py` | PostToolUse hook | Runs after every `Write`/`Edit`. Checks only the text just written and reports any defaults back to Claude. Warns, never blocks. |
| `tests/` | Tests for the hook | `python3 -m unittest discover -s tests -v` |

The three work together: the rule sets the bar every session, the skill gives the process when UI
work starts, and the hook catches what slips through.

Claude draws logos by hand as SVG paths, never as a font in `<text>`, a library icon or a
bitmap. It then checks them in the preview sheet: a mark that dies at 16 px, reads wrong when
mirrored, or depends on strokes, filters or live text gets fixed before it ships.

## Install

Everything is installed by copying. The repo and `~/.claude` are independent, so after editing
something here, copy it again.

```bash
# Skill
mkdir -p ~/.claude/skills/ui-anti-slop
cp -R SKILL.md references assets ~/.claude/skills/ui-anti-slop/

# Always-on rule
mkdir -p ~/.claude/rules
cp rules/ui-anti-slop.md ~/.claude/rules/

# Hook script
mkdir -p ~/.claude/hooks
cp scripts/ui-slop-check.py ~/.claude/hooks/
```

Then register the hook in `~/.claude/settings.json`, merged into any existing `hooks` key:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 -I \"$HOME/.claude/hooks/ui-slop-check.py\""
          }
        ]
      }
    ]
  }
}
```

The command uses the macOS system Python (`/usr/bin/python3`, 3.9) so it does not depend on
pyenv or a virtualenv. The script uses the standard library only.

Check the install in a new session:
- `/context` lists `ui-anti-slop.md` under memory files.
- `/skills` lists `ui-anti-slop`.
- `/hooks` shows the PostToolUse entry.

## How the hook decides

It runs only on UI files and only on the text Claude just wrote: `content` for `Write`,
`new_string` for `Edit`.

- **Files checked:** `.css .scss .sass .less .html .htm .jsx .tsx .js .ts .mjs .cjs .vue .svelte
  .astro .mdx .svg` and `tailwind.config.*`. SVG is included so logos and icons get the same
  colour and font checks.
- **Files skipped:** `node_modules/`, `dist/`, `build/`, `.next/`, `.git/`, `schema.d.ts` and
  minified files.

**Colours.** Every colour literal is converted to HSL: `#rgb`, `#rrggbb`, `rgb()`, `hsl()`,
`oklch()`, and shadcn-style bare HSL tokens such as `--background: 222.2 84% 4.9%`.
- **Navy / blue-slate:** hue 195–265°, saturation above 12 %, lightness below 28 %.
- **Blue-tinted grey:** hue 200–250°, saturation above 15 %, lightness above 93 %.
- **Known defaults** are flagged by value: `#667EEA`, `#764BA2`, `#6366F1`, `#4F46E5`, `#7C3AED`,
  `#8B5CF6`, `#5E6AD2`.

**Tailwind classes.**
- `bg|from|via|to|border|ring|fill|stroke|divide|outline` with `slate|gray` 800–950
- `bg|from|via|to` with `blue|indigo|sky` 900–950
- `from|via|to` with `indigo|violet|purple|fuchsia`
- `bg-clip-text` combined with `text-transparent` (gradient text)

**Fonts.**
- **Flagged:** Inter, Geist, Poppins, Roboto, Montserrat, Space Grotesk, Plus Jakarta Sans, DM
  Sans, Outfit, Manrope and Sora; also the seeded second wave that critiques name: Instrument
  Serif, Fraunces, Satoshi, Clash Display and Cabinet Grotesk.
- **Only on lines that are about fonts:** `font-family`, `@fontsource/…`, `next/font`, Google
  Fonts URLs, and Fontshare URLs (`f[]=satoshi`).
- **Rule only, not the hook:** the rule bans a longer list as defaults. The hook stays narrow to
  keep false positives low.

**Output.** Up to 10 findings with file line, value and reason, returned as `additionalContext`.
Claude then either fixes them or says why the brief requires them. The edit itself always goes
through, and the script swallows its own errors so a bug can't get in the way of an edit.

**Opt out for one project.** For a project whose brand really is navy, add this to the project's
`.claude/settings.json`:

```json
{ "env": { "UI_SLOP_CHECK": "off" } }
```

## Precedence

The rule and the skill govern only what the brief leaves open:
- If the user, the brief or a project's established design system asks for something listed
  here, that wins.
- In an existing codebase, Claude does not add these defaults to new work. It points out the
  ones already there instead of silently rewriting them.

## Tests

```bash
/usr/bin/python3 -m unittest discover -s tests -v
```

The tests pipe sample PostToolUse payloads into the script, the same way Claude Code runs it. They
must pass on Python 3.9.

## Layout

```
ui-anti-slop/
├── SKILL.md
├── references/
│   ├── theme.md
│   ├── colour.md
│   ├── typography.md
│   ├── logo-svg.md
│   ├── assets.md
│   ├── layout.md
│   ├── surfaces.md
│   ├── motion-and-copy.md
│   └── research.md
├── assets/logo-preview.html
├── rules/ui-anti-slop.md
├── scripts/ui-slop-check.py
└── tests/test_ui_slop_check.py
```
