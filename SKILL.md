---
name: ui-anti-slop
description: Use when designing, building, restyling or reviewing any visual design - web apps, landing pages, dashboards, components, HTML artifacts, slides, diagrams, emails, logos, icons, illustrations and brand assets - so every choice comes from the subject instead of AI-slop defaults, and the result is calm and comfortable to read. Walks a general process (theme and intensity, colour, type, a logo drawn as hand-written SVG, assets, layout, surfaces such as border, radius and shadow, motion and copy) over a numeric comfort floor, spending distinctiveness in one or two places. Names the defaults to avoid at each step - navy/blue-slate surfaces, indigo/purple gradients, Inter/Geist and the seeded "distinctive" fonts, AI-ring and hexagon logos, stock icon sets and Corporate Memphis art, stock SaaS layouts, the rounded-2xl card kit, generic copy - and the opposite failure of a forced, tiring design. Gives a design-brief template, a palette checker, a logo preview sheet and a self-check.
---

# UI anti-slop

Generated interfaces converge on the same few defaults: a navy or slate dark mode, indigo
buttons, purple gradients, Inter, a gradient-ring logo, a centred hero over three identical cards,
and "Unlock the power of…". They appear because, with nothing specific to draw from, a model
picks the most common option. This skill gives every choice something specific to draw from: the
subject in front of you, worked through in order from theme to copy. It also names the defaults
precisely, so they can be caught. The evidence behind every item is in
[references/research.md](references/research.md).

Avoiding defaults on every axis at once has its own failure: a beige page, an unfamiliar body
face, a tension grid and a saturated field together feel forced and tire the eyes. So the skill
keeps the reading surfaces calm, on a numeric comfort floor, and lets the subject show at full
strength in one or two places.

Applies whenever I design or style any interface or brand asset: apps, landing pages, dashboards,
components, HTML artifacts, slides, diagrams, emails, logos, icons. The brief's own words win, and
so does a project's established design system: if either asks for something listed here, use it.
These rules govern every axis the brief leaves free. In an existing codebase, don't add these
defaults to new work; point out the ones already there instead of silently rewriting them.

## How to use this skill

- **Read the project's `DESIGN.md` first** if it exists, and treat it as the established design
  system. For a new product or brand, save the confirmed brief there, so later sessions build on
  the same decisions.
- **Scale it to the job:**
  - **A component or restyle inside an existing design system:** use the system. Apply colour,
    type and surfaces only where it leaves gaps, and point out the defaults already there.
  - **A new screen in a product with no system:** steps 1–3 and 5–8, briefly.
  - **A new product, site or brand:** every step, including the logo.
- **Work in order.** Each step feeds the next, and every later choice cites one line of the
  Direction from step 1.
- **Open a step's reference file when you reach that step,** not all at once, and keep
  [references/comfort.md](references/comfort.md) open throughout.
- **Names and values in the references are evidence or worked examples, not defaults.** If you
  are reaching for the same font, palette, logo shape or layout as last time, choose again.

## Calm by default: the comfort floor

[references/comfort.md](references/comfort.md)

- **Two layers.** The *reading surfaces* (ground, body text, forms, tables, navigation, controls,
  spacing, grid) stay calm and familiar. The *signature* (the logo, plus 1–2 of: a display face, a
  bold accent, imagery, one layout gesture, one pattern) is where the subject shows at full
  strength.
- **Intensity:** Calm (default) / Balanced / Bold sizes the signature, never the floor. If the
  brief doesn't say, ask one question; if you can't ask, use Calm.
- **Precedence:** the novelty test applies to the signature and identity; the comfort test
  applies everywhere and wins any conflict.
- **Headline numbers** (OKLCH; heuristics; the colour bands are checked by
  [scripts/palette-check.py](scripts/palette-check.py)):
  - light ground L 0.96–1.00, C ≤ 0.015 (warm tints under 0.008); large areas C ≤ 0.02; ink
    L 0.18–0.35, not `#000` on `#FFF`;
  - body text ≥ 7:1 (APCA Lc 75+), secondary ≥ 4.5:1 by colour, not opacity;
  - 2–3 core colours + 1 accent (C ≤ 0.20, ≤ 5 % of a view); no vibrating saturated pairs;
  - dark: ground L 0.15–0.24, C ≤ 0.02; text L 0.88–0.94; light mode unless the subject is dark;
  - body 16–18px, line height 1.5, measure 55–75ch; at most 4–6 sizes and 3 weights per screen;
  - a regular grid, at most 3–4 alignment edges per view, 4–6 spacing values per screen;
    familiar placements for logo, navigation, search and actions;
  - most elements flat; 2–3 radii per screen; UI motion 80–250ms by role, ease-out.
- **Both failures:** *forced different* (three or more distinctive axes at once) and *sterile
  default* (flat white, grey borders, a generic font, nothing of the subject).

## The process

### 1. Theme: write the Direction
[references/theme.md](references/theme.md)
- Inventory the subject in nouns and verbs: what it is, who uses it, where, which era, what it is
  made of.
- Choose three adjectives as "X, not Y", place the personality sliders (they set the voice and the
  signature, not the reading surfaces), and list 5–8 material-world nouns.
- Add one era/place/culture reference and 2–3 principles that settle trade-offs.
- **Choose the intensity and name the signature** within its budget.
- Never use "modern, clean, minimal, sleek" as direction words.
- When browsing is available, look at Figma Community files in the subject's own category, never
  "AI SaaS". Note what makes them specific; copy nothing.

### 2. Colour
[references/colour.md](references/colour.md)
- Sample each token's *hue* from the material nouns; set its lightness and chroma by role, inside
  the comfort bands.
- 2–3 core colours + 1 accent with a budget; the dominant colour owns the area as a low-chroma
  tint.
- Neutrals tinted toward the brand hue, not toward blue; ramps built in OKLCH.
- Status colours stay in their green/amber/red/blue families.
- A dark theme only when wanted: a near-neutral dark tinted from the subject (never navy).
- Body text ≥ 7:1; run `scripts/palette-check.py` on the tokens.

### 3. Type
[references/typography.md](references/typography.md)
- Choose two jobs separately: a **text face** for legibility (familiar is fine; the named bans
  still apply; `system-ui` allowed for app UI with a reason) and, if needed, a **display face** for
  the signature, found outside the most popular families.
- Subject (era, material, voice, reading mode) → a classification → three candidates from at
  least two sources → Google's type checklist → a test with the real copy, including long
  Indonesian words.
- Record why each winner won. One family, or two that differ in structure.
- Body 16–18px, line height 1.5, measure 55–75ch; at most three weights; tabular figures for
  data. Check the licence.

### 4. Logo, drawn by hand as SVG
[references/logo-svg.md](references/logo-svg.md) and
[assets/logo-preview.html](assets/logo-preview.html)
- Always write the logo as SVG paths yourself. Never use a font in `<text>`, an icon from a
  library, an emoji or a bitmap.
- **Concept:** one sentence, from the subject. A symbol only with a reason; otherwise a wordmark
  with custom details.
- **Exploration:** three concepts, then the shelf test against the category.
- **The master:** on a `0 0 256 256` grid, fills only, with optical corrections.
- **Variants:** one colour via `currentColor`, reversed, lockups and a favicon set.
- **Test** it in the preview sheet.
- Skip this step when the brand already has a logo.

### 5. Assets
[references/assets.md](references/assets.md)
- Show the real thing (product, place, people, data) before symbolising it. One strong real image
  is often the best signature.
- **Icons:** a set chosen and modified on purpose, or custom icons drawn to a written spec derived
  from the logo.
- **Illustration:** built from the logo's geometry and 2–3 tokens.
- **Photography:** a written direction (subject, light, place, crop, grade).
- **Pattern:** one, drawn from the material world; never behind body text.
- A social image and favicons from the same kit.

### 6. Layout
[references/layout.md](references/layout.md)
- **Content-out:** list the screen's real content by importance, and open with the most
  characteristic thing of the subject.
- **Grid:** a regular grid fitted to the content's fixed sizes; asymmetry only where the content
  is unequal. At most 3–4 alignment edges per view.
- **Spacing:** a scale with more steps near the origin; 4–6 values per screen; groups tight,
  gaps between groups at least twice as wide.
- **Placement:** logo, navigation, search and primary actions where users expect them.
- **Composition:** one focal point per view and one signature element; honest charts, tables and
  empty states; three planned responsive states.

### 7. Surfaces: border, radius, shadow, elevation, focus
[references/surfaces.md](references/surfaces.md)
- **Radius:** a scale by role, 2–3 values per screen. Nested corners stay concentric (inner =
  outer − padding).
- **Borders:** 1px, in translucent ink; the width stays the same across states.
- **Separation:** most elements sit flat. One method per relationship, in order of preference:
  space, fill, border, shadow.
- **Shadows:** only on things that float; one light source, layered, tinted with the ink. In dark
  mode, elevation comes from lighter surfaces.
- **Focus:** a 2px concentric ring at 3:1.

### 8. Motion and copy
[references/motion-and-copy.md](references/motion-and-copy.md)
- **Motion** only where it has a job: mostly 150–250ms, ease-out, short travel, nothing on actions
  repeated all day; animate `transform` and `opacity`, and respect `prefers-reduced-motion`.
- **Copy:** real content, a voice taken from the Direction's adjectives, and buttons that say what
  happens.

## Guardrails: never as a default

Each step's reference has the full list with reasons.

- **Comfort:**
  - forced different: an era or display face as body text, a coloured or beige page, a tension
    grid and a loud accent all at once; trend-stacking (glass, glow, mesh, mono labels, grid
    backgrounds);
  - sterile default: flat white, thin grey borders, a generic font and nothing of the subject;
  - `#000` text on `#FFF`; text dimmed with opacity; two saturated hues vibrating side by side.
- **Colour:**
  - navy or blue-slate surfaces (hue about 200–260°, lightness under 25 %: `#0F172A` `#1E293B`
    `#111827`, `slate`/`gray`-800–950), and their blue-grey light twin (`#F8FAFC` `#F1F5F9`);
  - indigo or violet primaries (`#6366F1` `#7C3AED`); purple→blue gradients; gradient text; neon
    glows;
  - Tailwind or shadcn palettes used as shipped; rainbow icon chips;
  - the second wave: cream + serif + terracotta, or near-black + one acid accent.
- **Type:**
  - Inter, Geist, Roboto, Arial, Open Sans, Lato, Poppins, Montserrat; the system-ui stack outside
    app UI;
  - Space Grotesk, Plus Jakarta Sans, DM Sans, Outfit, Manrope, Sora;
  - the seeded second wave: Instrument Serif, Fraunces, Bricolage Grotesque, Newsreader, Crimson
    Pro, IBM Plex, Satoshi, General Sans, Clash Display, Cabinet Grotesk, Switzer, Söhne;
  - serif display + grotesk body + mono labels; one italic or accent-coloured word in a headline;
    a tracked caps eyebrow on every heading.
- **Logo:**
  - the AI ring, the swirling hexagon or vortex, radiating dots or orbits, overlapping circles;
  - the ✨ sparkle; a robot face with dot eyes; an infinity loop; a letter in a rounded square;
  - a swoosh, globe or rising bars;
  - a gradient carrying a weak form; live `<text>`.
- **Assets:**
  - a stock 24px/2px icon set used as shipped; icons in circles; emoji as icons;
  - Corporate Memphis; one-accent unDraw-style scenes; glossy, clay or glass 3D; isometric
    scenes;
  - decorative stock or AI photos; grid or dot backgrounds; blurred blobs.
- **Layout:**
  - the stock landing page: centred hero + pill + two buttons + logo row + three identical cards
    + testimonials + pricing + CTA band;
  - section kits by habit: a bento grid, a fake terminal window, a pill repeating the headline,
    three steps and three tiers whatever the content, the four-column footer;
  - the stock dashboard: dark sidebar + four KPI cards with "+12.5% ↑";
  - template chrome: 01/02/03 markers, "A · B · C" strings, "→" on every link, mono micro-labels.
- **Surfaces:**
  - identical `rounded-2xl` cards with `shadow-lg`; nested cards; coloured left borders;
  - pure-black shadows; glassmorphism; glow shadows; the ghost card (border + wide soft shadow);
  - the same radius on parent and child; `outline: none` with no replacement.
- **Motion and copy:**
  - fade-and-slide-up on every section; `hover:scale` on every card; `transition-all`; pulsing
    dots;
  - Unlock, Elevate, Empower, Seamless, Supercharge, "all-in-one platform";
  - invented stats; John Doe or Acme; "Get Started" repeated;
  - in Indonesian: "Tingkatkan produktivitas", "Solusi all-in-one", "Revolusi …", "Wujudkan …".

## Design brief before code

Write this down, show it, and get it confirmed before writing UI code. For a small change, write
only the lines that apply. Each line carries its reason. For a new product or brand, save the
confirmed brief as `DESIGN.md` at the project root.

```
Direction:  subject (what, who, where, the one job of this screen)
            3 adjectives as "X, not Y"; 5–8 material nouns; one era/place reference;
            2–3 principles
Intensity:  Calm / Balanced / Bold, and why
Signature:  the logo + the 1–2 items where the subject shows at full strength;
            everything else stays on the comfort floor
Palette:    4–6 named hex tokens plus status colours, with roles, OKLCH and ratios, each tied to a
            material noun; palette-check result
Type:       text face and why it reads well; display face (if any) and why it fits
            (cite the Direction); scale ratio, sizes, weights, features
Comfort:    ground and ink lightness; body size / line height / measure; sizes and
            weights per screen; alignment edges; spacing values
Logo:       the concept in one sentence; symbol or wordmark, and why; variants needed
Assets:     icon source and spec; illustration style; photo direction; pattern
Layout:     a one-sentence concept plus a small ASCII sketch; grid; density; focal point
Surfaces:   radius scale by role; border policy; separation rule; shadow levels; focus ring
```

Then test the brief twice:
- **Novelty, for the signature and identity:** would I have produced the same palette, display
  face, logo or layout for any similar brief (another SaaS, another dashboard, another café)? If
  yes, that part is a default, so revise it and say what changed. Check every token against the
  guardrails.
- **Comfort, for everything:** does every number sit on the comfort floor, and is anything other
  than the named signature distinctive? If so, calm it.

## Self-check after building

1. **Screens.** Screenshot every screen you touched, in light and dark if both exist, at desktop
   and at 375px. Ask whether it would look the same for a different product. If yes, change the
   signature, not the reading surfaces.
2. **Comfort audit** ([references/comfort.md → Checks](references/comfort.md#checks-the-comfort-audit)):
   - `python3 scripts/palette-check.py 'ROLE[:name]=#HEX' …` on the tokens (the path is
     relative to this skill's folder): no FAIL, every WARN fixed or explained;
   - the blur test: exactly one thing pops;
   - read a real paragraph for two minutes on a phone and a laptop; nothing glares, vibrates or
     looks muddy;
   - count colours, sizes, weights, radii and alignment edges per view against the limits.
   - Comfort wins any conflict with novelty.
3. **Logo.** Render it in [assets/logo-preview.html](assets/logo-preview.html) and screenshot the
   sheet. Fix every lint `fail`, and anything that is lost in the 16 px pixel view or reads wrong
   when mirrored or rotated.
4. **Diff search.** Search the diff for the usual suspects:
   `slate-(800|900|950)`, `gray-(800|900|950)`, `indigo-`, `violet-`, `purple-`,
   `bg-gradient`/`bg-linear`, `bg-clip-text`, `backdrop-blur`, `shadow-(lg|xl|2xl)`,
   `rounded-(2xl|3xl)`, `rgba(0,0,0,`/`rgb(0 0 0`, `transition-all`, `outline: none`/
   `outline-none`, `100vh`/`h-screen`, `#0F172A`, `#1E293B`, `#111827`, `Inter`, `Geist`,
   `Instrument Serif`. Also check `lucide-react`/`@heroicons`: is the set used as shipped, or
   chosen and adjusted?
5. **Contrast and focus.** Body text 7:1 as the target and 4.5:1 as the floor, large text 3:1, UI
   parts and focus indicators 3:1. Tab through the page: focus must always be visible.
6. **Hook.** If the `ui-slop-check` PostToolUse hook is installed, it reports navy, blue-grey,
   slate/indigo classes, gradient text and default fonts as you write, including inside `.svg`
   files. Fix each note, or say why the brief or the project's design system requires it.

## References

| File | Step |
|---|---|
| [references/comfort.md](references/comfort.md) | every step: two layers, intensity, the comfort floor's numbers, the comfort audit |
| [references/theme.md](references/theme.md) | the Direction: subject inventory, adjectives, material nouns, references, intensity, signature |
| [references/colour.md](references/colour.md) | tokens, roles with lightness/chroma bands, OKLCH ramps, dark themes, status colours |
| [scripts/palette-check.py](scripts/palette-check.py) | checks tokens: OKLCH, WCAG ratio, APCA Lc, the comfort floor |
| [references/typography.md](references/typography.md) | text face vs display face, the classification method, pairing, numbers, licensed sources |
| [references/logo-svg.md](references/logo-svg.md) | concept → master SVG → variants → favicon set, SVG rules, outlining fonts |
| [assets/logo-preview.html](assets/logo-preview.html) | the preview sheet: sizes, pixel truth, colourways, stress tests, grid, lint |
| [references/assets.md](references/assets.md) | icons, illustration, photography, patterns, generated images |
| [references/layout.md](references/layout.md) | content-out composition, grids, spacing, placement, honest app content, responsive behaviour |
| [references/surfaces.md](references/surfaces.md) | radius, borders, separation, shadows, elevation, focus |
| [references/motion-and-copy.md](references/motion-and-copy.md) | motion with a job; copy from real content |
| [references/research.md](references/research.md) | the evidence: Figma Community, critiques, design systems, other skills, sources |
