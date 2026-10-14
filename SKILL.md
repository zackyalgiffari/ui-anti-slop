---
name: ui-anti-slop
description: Use when designing, building, restyling or reviewing any visual design - web apps, landing pages, dashboards, components, HTML artifacts, slides, diagrams, emails, logos, icons, illustrations and brand assets - so every choice comes from the subject instead of AI-slop defaults. Walks a general process (theme, colour, type, a logo drawn as hand-written SVG, assets, layout, surfaces such as border, radius and shadow, motion and copy) and names the defaults to avoid at each step - navy/blue-slate surfaces, indigo/purple gradients, Inter/Geist and the seeded "distinctive" fonts, AI-ring and hexagon logos, stock icon sets and Corporate Memphis art, stock SaaS layouts, the rounded-2xl card kit and generic copy. Gives a design-brief template, a logo preview sheet and a self-check.
---

# UI anti-slop

Generated interfaces converge on the same few defaults: a navy or slate dark mode, indigo
buttons, purple gradients, Inter, a gradient-ring logo, a centred hero over three identical cards,
and "Unlock the power of…". They appear because, with nothing specific to draw from, a model
picks the most common option. This skill gives every choice something specific to draw from: the
subject in front of you, worked through in order from theme to copy. It also names the defaults
precisely, so they can be caught. The evidence behind every item is in
[references/research.md](references/research.md).

Applies whenever I design or style any interface or brand asset: apps, landing pages, dashboards,
components, HTML artifacts, slides, diagrams, emails, logos, icons. The brief's own words win, and
so does a project's established design system: if either asks for something listed here, use it.
These rules govern every axis the brief leaves free. In an existing codebase, don't add these
defaults to new work; point out the ones already there instead of silently rewriting them.

## How to use this skill

- **Scale it to the job:**
  - **A component or restyle inside an existing design system:** use the system. Apply colour,
    type and surfaces only where it leaves gaps, and point out the defaults already there.
  - **A new screen in a product with no system:** steps 1–3 and 5–8, briefly.
  - **A new product, site or brand:** every step, including the logo.
- **Work in order.** Each step feeds the next, and every later choice cites one line of the
  Direction from step 1.
- **Open a step's reference file when you reach that step,** not all at once.
- **Names and values in the references are evidence or worked examples, not defaults.** If you
  are reaching for the same font, palette, logo shape or layout as last time, choose again.

## The process

### 1. Theme: write the Direction
[references/theme.md](references/theme.md)
- Inventory the subject in nouns and verbs: what it is, who uses it, where, which era, what it is
  made of.
- Choose three adjectives as "X, not Y", set the personality sliders near the ends, and list 5–8
  material-world nouns.
- Add one era/place/culture reference and 2–3 principles that settle trade-offs.
- Never use "modern, clean, minimal, sleek" as direction words.
- When browsing is available, look at Figma Community files in the subject's own category, never
  "AI SaaS". Note what makes them specific; copy nothing.

### 2. Colour
[references/colour.md](references/colour.md)
- 4–6 named tokens sampled from the material nouns, each with a role: ground, ink, primary,
  accent, signal.
- One dominant colour, and an accent with a budget.
- Neutrals tinted toward the brand hue, not toward blue; ramps built in OKLCH.
- A dark theme taken from the subject (forest, oxblood, umber, olive, aubergine; never navy).
- WCAG AA contrast on every pair actually used.

### 3. Type
[references/typography.md](references/typography.md)
- Subject (era, material, voice, reading mode) → a classification → three candidates from at
  least two sources, outside the most popular → Google's type checklist → a test with the real
  copy, including long Indonesian words.
- Record why the winner won.
- One family, or two that differ in structure.
- A scale ratio set by the product; measure under 80ch; tabular figures for data.
- Check the licence.

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
- Show the real thing (product, place, people, data) before symbolising it.
- **Icons:** a set chosen and modified on purpose, or custom icons drawn to a written spec derived
  from the logo.
- **Illustration:** built from the logo's geometry and 2–3 tokens.
- **Photography:** a written direction (subject, light, place, crop, grade).
- **Pattern:** one, drawn from the material world.
- A social image and favicons from the same kit.

### 6. Layout
[references/layout.md](references/layout.md)
- **Content-out:** list the screen's real content by importance, and open with the most
  characteristic thing of the subject.
- **Grid:** derive it from the content's fixed sizes, with asymmetric splits by default.
- **Spacing:** a scale with more steps near the origin.
- **Density:** set by the product type.
- **Composition:** one focal point per view, unequal sizes for unequal importance, and planned
  responsive changes.

### 7. Surfaces: border, radius, shadow, elevation, focus
[references/surfaces.md](references/surfaces.md)
- **Radius:** a scale by role. Nested corners stay concentric (inner = outer − padding).
- **Borders:** 1px, in translucent ink.
- **Separation:** one method per relationship, in order of preference: space, fill, border,
  shadow.
- **Shadows:** one light source, layered, tinted with the ink. In dark mode, elevation comes from
  lighter surfaces.
- **Focus:** a 2px concentric ring at 3:1.

### 8. Motion and copy
[references/motion-and-copy.md](references/motion-and-copy.md)
- **Motion** only where it has a job: animate `transform` and `opacity`, and respect
  `prefers-reduced-motion`.
- **Copy:** real content, a voice taken from the Direction's adjectives, and buttons that say what
  happens.

## Guardrails: never as a default

Each step's reference has the full list with reasons.

- **Colour:**
  - navy or blue-slate surfaces (hue about 200–260°, lightness under 25 %: `#0F172A` `#1E293B`
    `#111827`, `slate`/`gray`-800–950), and their blue-grey light twin (`#F8FAFC` `#F1F5F9`);
  - indigo or violet primaries (`#6366F1` `#7C3AED`); purple→blue gradients; gradient text; neon
    glows;
  - Tailwind or shadcn palettes used as shipped; rainbow icon chips;
  - the second wave: cream + serif + terracotta, or near-black + one acid accent.
- **Type:**
  - Inter, Geist, Roboto, Arial, Open Sans, Lato, Poppins, Montserrat, the system-ui stack;
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
  - the stock dashboard: dark sidebar + four KPI cards with "+12.5% ↑";
  - template chrome: 01/02/03 markers, "A · B · C" strings, "→" on every link, mono micro-labels.
- **Surfaces:**
  - identical `rounded-2xl` cards with `shadow-lg`; nested cards; coloured left borders;
  - pure-black shadows; glassmorphism; glow shadows;
  - the same radius on parent and child; `outline: none` with no replacement.
- **Motion and copy:**
  - fade-and-slide-up on every section; `hover:scale` on every card; `transition-all`; pulsing
    dots;
  - Unlock, Elevate, Empower, Seamless, Supercharge, "all-in-one platform";
  - invented stats; John Doe or Acme; "Get Started" repeated;
  - in Indonesian: "Tingkatkan produktivitas", "Solusi all-in-one", "Revolusi …", "Wujudkan …".

## Design brief before code

Write this down, show it, and get it confirmed before writing UI code. For a small change, write
only the lines that apply. Each line carries its reason.

```
Direction:  subject (what, who, where, the one job of this screen)
            3 adjectives as "X, not Y"; 5–8 material nouns; one era/place reference;
            2–3 principles
Palette:    4–6 named hex tokens with roles and contrast ratios, each tied to a material noun
Type:       family or families and why they fit (cite the Direction); scale ratio, weights,
            features (tabular figures, languages)
Logo:       the concept in one sentence; symbol or wordmark, and why; variants needed
Assets:     icon source and spec; illustration style; photo direction; pattern
Layout:     a one-sentence concept plus a small ASCII sketch; grid split; density; focal point
Surfaces:   radius scale by role; border policy; separation rule; shadow levels; focus ring
Signature:  the one memorable element; everything else stays quiet
```

Then test the brief: would I have produced the same palette, type, logo or layout for any similar
brief (another SaaS, another dashboard, another café)? If yes, that part is a default, so revise
it and say what changed. Check every token against the guardrails.

## Self-check after building

1. **Screens.** Screenshot every screen you touched, in light and dark if both exist. Ask whether
   it would look the same for a different product. If yes, change the part that would.
2. **Logo.** Render it in [assets/logo-preview.html](assets/logo-preview.html) and screenshot the
   sheet. Fix every lint `fail`, and anything that is lost in the 16 px pixel view or reads wrong
   when mirrored or rotated.
3. **Diff search.** Search the diff for the usual suspects:
   `slate-(800|900|950)`, `gray-(800|900|950)`, `indigo-`, `violet-`, `purple-`,
   `bg-gradient`/`bg-linear`, `bg-clip-text`, `backdrop-blur`, `shadow-(lg|xl|2xl)`,
   `rounded-(2xl|3xl)`, `rgba(0,0,0,`/`rgb(0 0 0`, `transition-all`, `outline: none`/
   `outline-none`, `#0F172A`, `#1E293B`, `#111827`, `Inter`, `Geist`, `Instrument Serif`.
   Also check `lucide-react`/`@heroicons`: is the set used as shipped, or chosen and adjusted?
4. **Contrast.** Body text 4.5:1, large text 3:1, UI parts and focus indicators 3:1. Tab through
   the page: focus must always be visible.
5. **Hook.** If the `ui-slop-check` PostToolUse hook is installed, it reports navy, blue-grey,
   slate/indigo classes, gradient text and default fonts as you write, including inside `.svg`
   files. Fix each note, or say why the brief or the project's design system requires it.

## References

| File | Step |
|---|---|
| [references/theme.md](references/theme.md) | the Direction: subject inventory, adjectives, material nouns, references |
| [references/colour.md](references/colour.md) | tokens, roles, OKLCH ramps, dark themes, status colours |
| [references/typography.md](references/typography.md) | the classification method, pairing, numbers, licensed sources |
| [references/logo-svg.md](references/logo-svg.md) | concept → master SVG → variants → favicon set, SVG rules, outlining fonts |
| [assets/logo-preview.html](assets/logo-preview.html) | the preview sheet: sizes, pixel truth, colourways, stress tests, grid, lint |
| [references/assets.md](references/assets.md) | icons, illustration, photography, patterns, generated images |
| [references/layout.md](references/layout.md) | content-out composition, grids, spacing, density, responsive behaviour |
| [references/surfaces.md](references/surfaces.md) | radius, borders, separation, shadows, elevation, focus |
| [references/motion-and-copy.md](references/motion-and-copy.md) | motion with a job; copy from real content |
| [references/research.md](references/research.md) | the evidence: Figma Community, critiques, design systems, sources |
