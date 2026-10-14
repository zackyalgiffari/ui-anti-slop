# UI: no AI-slop defaults

Applies whenever I design or style any interface or brand asset: apps, landing pages, dashboards,
components, HTML artifacts, slides, diagrams, emails, logos, icons. The brief's own words win, and
so does a project's established design system: if either asks for something listed here, use it.
These rules govern every axis the brief leaves free. In an existing codebase, don't add these
defaults to new work; point out the ones already there instead of silently rewriting them.

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
- Nor the second wave that prompting guides seeded: Instrument Serif, Fraunces, Bricolage
  Grotesque, Newsreader, Crimson Pro, IBM Plex, Satoshi, General Sans, Clash Display, Cabinet
  Grotesk, Switzer, Söhne.
- Tells: gradient-text headlines; one word in a headline set italic or in the accent colour; a
  tracked ALL-CAPS eyebrow above every heading; tracking-tight bold on every heading; Title Case
  Everywhere; a giant centred hero headline by default; serif display + grotesk body + mono labels;
  mono on text that isn't code; variable axes maxed out for effect.
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
- Surfaces: pure-black or grey shadows on a coloured ground, the same radius on a parent and its
  child, border + fill + shadow on one card, `outline: none` with nothing in its place.
- Motion: fade-and-slide-up on every section, hover:scale on every card, pulsing dots,
  transition-all.
Instead: open with the most characteristic thing of the subject (its photo, its product, a live
demo, its real data). Asymmetric or left-aligned grids; radius and shadow that vary by role; one
memorable element and everything else quiet.

## Logos and assets
- Logos are hand-written SVG paths drawn from a one-sentence concept in the subject, and work in
  one colour at 16 px. Never: the AI ring (gradient circle, central opening, radiating parts), the
  swirling hexagon or vortex, radiating dots or orbits, overlapping circles, the ✨ sparkle, a
  robot face with dot eyes, an infinity loop, a letter in a rounded square, swoosh/globe/rising
  bars, a gradient carrying a weak form, live `<text>`.
- Icons: a stock 24px/2px round-cap set (Lucide, Heroicons, Feather) used as shipped for
  everything, two sets mixed, an icon in a circle above every heading.
- Illustration and photos: Corporate Memphis figures, one-accent unDraw-style scenes, glossy/clay/
  glass 3D, isometric workspaces, decorative stock or AI-generated photos.
Instead: show the real product, place, people or data; draw icons and illustration from the logo's
geometry and the palette.

## Copy
Unlock, Elevate, Empower, Seamless, Supercharge, Revolutionize, "all-in-one platform", "the future
of X", "feels like magic", invented round stats (10,000+, 99.9 %), John Doe/Acme, "Get Started" or
"Learn More" repeated. In Indonesian the same: "Tingkatkan produktivitas", "Solusi all-in-one",
"Revolusi …", "Wujudkan …". Use real content; a button says what happens.

## Process
1. Before writing UI code, state the Direction (subject, three "X, not Y" adjectives, material
   nouns), palette (named hex tokens), type, logo concept, assets, layout and surfaces, each with
   the reason it fits this subject, and check none of it is on this page. Load the `ui-anti-slop`
   skill for the full process, and `frontend-design`.
2. After building, screenshot it and ask: would this look the same for a different product? If
   yes, change it.
3. A "UI slop check" note from the PostToolUse hook means fix it, or say why the brief or the
   project's design system requires it.
