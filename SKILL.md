---
name: ui-anti-slop
description: Use when designing, building, restyling or reviewing any user interface (web apps, landing pages, dashboards, components, HTML artifacts, slides, diagrams, emails) to avoid AI-slop defaults - navy/blue-slate surfaces, indigo/purple gradients, default fonts such as Inter and Geist, stock SaaS layouts, template chrome and generic copy. Gives the bans, what to do instead, a design-plan template and a self-check.
---

# UI anti-slop

Generated interfaces converge on the same few defaults. These are a navy or slate dark mode,
indigo buttons, purple gradients, Inter, a centred hero over three identical cards, and "Unlock
the power of…". This skill names those defaults precisely and replaces them with choices taken
from the subject in front of you. The evidence behind every item is in
[references/research.md](references/research.md).

Applies whenever I design or style any interface: apps, landing pages, dashboards, components,
HTML artifacts, slides, diagrams, emails. The brief's own words win, and so does a project's
established design system: if either asks for something listed here, use it. These rules govern
every axis the brief leaves free. In an existing codebase, don't add these defaults to new work;
point out the ones already there instead of silently rewriting them.

## Never: navy
Navy and blue-slate are banned as page, surface, sidebar, card, hero or "dark mode" colours.
- By the numbers: hue ≈ 200–260°, lightness under ~25 %, any visible saturation. Examples:
  #0F172A #020617 #1E293B #0B1120 #0A0F1F #0F1326 #161B33 #111827 #1F2937 #0D1117.
- Tailwind/shadcn: slate-800/900/950, gray-800/900/950 (Tailwind gray is blue-tinted),
  blue/indigo/sky-950 surfaces, shadcn's "slate" base colour.
- The light-mode twin: blue-tinted greys as the page colour (#F8FAFC #F1F5F9 #F5F6FA,
  slate-50/100, gray-50).
- The combos: navy + gold/amber "premium", navy + electric-blue/cyan glow, navy + indigo gradient.
A dark theme that is actually wanted gets a dark taken from the subject (forest, oxblood, umber,
olive, aubergine, graphite with zero blue) and a different one each project.

## Other colour defaults to avoid
- Indigo/violet primaries (#6366F1 #4F46E5 #7C3AED #8B5CF6 #5E6AD2), purple→blue or violet→cyan
  gradients (#667EEA→#764BA2), neon/cyan glows on dark, gradient text.
- Tailwind/shadcn palettes used as shipped (blue-500 primary, stock emerald/rose/amber statuses).
- Rainbow icon chips: every card or KPI gets its own coloured rounded square.
- The second wave, which is where models go when told "no purple": cream (#F4F1EA) + high-contrast
  serif + terracotta (#D97757); near-black (#0B0B0B/#111) + one acid-green or vermilion accent.
  Fine when the brief calls for it, never as the fallback.
Instead: 4–6 named hex tokens taken from the subject's world (its materials, photography, industry,
place). One dominant colour and one accent with a budget; neutrals tinted toward the brand hue,
not toward blue; WCAG AA contrast for text.

## Typography
- Don't default to Inter, Geist, Roboto, Arial, Open Sans, Lato, Poppins, Montserrat or the
  system-ui stack, nor to the "distinctive" repeat picks: Space Grotesk, Plus Jakarta Sans,
  DM Sans, Outfit, Manrope, Sora, Playfair Display + Inter.
- Tells: gradient-text headlines; one word in a headline set italic or in the accent colour; a
  tracked ALL-CAPS eyebrow above every heading; tracking-tight bold on every heading; Title Case
  Everywhere; a giant centred hero headline by default.
Instead: one family or two clearly distinct ones chosen for this subject, a real type scale,
deliberate weights and widths, lines under ~80 characters.

## Layout, components, effects
- The stock landing page: centred hero, "✨ New" pill, two buttons, logo row, three identical
  feature cards with an icon in a circle, testimonial grid, pricing with "Most popular", CTA band.
- The SaaS card kit: everything boxed in identical rounded-2xl cards with one radius, shadow-lg
  everywhere, nested cards, cards with a coloured left border.
- The stock dashboard: navy sidebar, four KPI cards with icon chips and "+12.5% ↑" badges.
- Glassmorphism, blurred gradient orbs or aurora blobs, grid/dot backgrounds, glow shadows,
  sparkle emoji, emoji as icons.
- Template chrome: 01/02/03 markers on things that aren't a sequence, "A · B · C" meta strings,
  "→" on every link, monospace micro-labels.
- Motion: fade-and-slide-up on every section, hover:scale on every card, pulsing dots,
  transition-all.
Instead: open with the most characteristic thing of the subject (its photo, its product, a live
demo, its real data). Asymmetric or left-aligned grids; radius and shadow that vary by role; one
memorable element and everything else quiet.

## Copy
Unlock, Elevate, Empower, Seamless, Supercharge, Revolutionize, "all-in-one platform", "the future
of X", "feels like magic", invented round stats (10,000+, 99.9 %), John Doe/Acme, "Get Started" or
"Learn More" repeated. In Indonesian the same: "Tingkatkan produktivitas", "Solusi all-in-one",
"Revolusi …", "Wujudkan …". Use real content; a button says what happens.

## Design plan before code

Write this down, show it, and get it confirmed before writing UI code. Each line carries its reason.

```
Subject:   what the product is, who uses it, the one job of this screen
Palette:   4–6 named hex tokens with roles, e.g.
           paper #F3F4EF (page) · ink #1C2420 (text) · chalk #F5A524 (primary action) …
           where each colour comes from in the subject's world
Type:      family/families and roles, the scale (sizes, weights, widths)
Layout:    a one-sentence concept plus a small ASCII sketch; alignment (left/centre/justified)
Signature: the one memorable element; everything else stays quiet
```

Then test the plan: would I have produced the same palette, type and layout for any similar brief
(another SaaS, another dashboard)? If yes, that part is a default, so revise it and say what
changed. Check every token against the bans above.

## Self-check after building

1. Screenshot every screen you touched, in light and dark if both exist. Ask whether it would look
   the same for a different product. If yes, change the part that would.
2. Search the diff for the usual suspects:
   `slate-(800|900|950)`, `gray-(800|900|950)`, `indigo-`, `violet-`, `purple-`,
   `bg-gradient`/`bg-linear`, `bg-clip-text`, `backdrop-blur`, `shadow-(lg|xl|2xl)`,
   `rounded-(2xl|3xl)`, `#0F172A`, `#1E293B`, `#111827`, `Inter`, `Geist`.
3. Check text contrast (WCAG AA: 4.5:1 for body text, 3:1 for large text and UI parts).
4. If the `ui-slop-check` PostToolUse hook is installed, it already reports navy, blue-grey,
   slate/indigo classes, gradient text and default fonts as you write. Fix each note, or say why
   the brief or the project's design system requires it.

## References

- [references/research.md](references/research.md): Figma Community observations, the full tell
  catalogue with reasons, the second-wave warning, recommended alternatives and sources.
