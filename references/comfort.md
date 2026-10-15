# The comfort floor (applies at every step)

Decides what stays calm, readable and familiar however distinctive the Direction is. Every other
step works inside it: theme sizes the signature, and colour, type, layout, surfaces and motion
take their numbers from here. When a Direction choice and this floor disagree, the floor wins.

Banning the defaults on every axis at once doesn't make a design specific. It makes it strange:
a beige page, an unfamiliar body face, a tension grid and a saturated field all on one screen.
People read for minutes at a time, so the reading surfaces must be comfortable. The subject shows
at full strength in one or two places, and the rest is quiet.

## Two layers

| Layer | What it covers | Rule |
|---|---|---|
| **Reading surfaces** | ground, body text, forms, tables, navigation, controls, spacing, grid | the numbers below; familiar is good here |
| **The signature** | the logo, plus 1–2 of: a display face, a bold use of the accent, imagery or illustration, one layout gesture, one pattern | where the subject shows at full strength |

- The subject reaches the reading surfaces only as a hue tint, the voice of the copy and a
  well-chosen text face. Never as saturation, a novel layout or a display face.
- **Precedence:** the novelty test ("would this look the same for another product?") applies to
  the signature and the identity choices. The comfort test ("could someone read this for ten
  minutes without strain?") applies everywhere, and wins any conflict.

## Intensity

Pick one and write it in the brief. It sizes the signature and decides how much may vary between
sections; it never loosens the floor's numbers.

| | Calm (default) | Balanced | Bold |
|---|---|---|---|
| signature items besides the logo | 1 | 2 | 2 |
| saturated colour fields | none; the accent only | 1 per page | 1 per view |
| type scale ratio (the product sets it, this caps it) | up to 1.25 | up to 1.333 | any, plus one display line |
| section rhythm | uniform | two variants | varied |
| motion | feedback and state changes | plus one orchestrated moment | plus scroll choreography |

- **Calm** suits apps, dashboards, tools, public services and most business sites. **Bold** suits
  portfolios, campaigns, events and brands whose subject is loud.
- If the brief doesn't say, ask one question ("calm and familiar, or bold and expressive?"). If
  you can't ask, use Calm.

## Colour

Values are OKLCH. The bands are heuristics triangulated from Material, Radix, Primer and
Hallmark, not a standard. [scripts/palette-check.py](../scripts/palette-check.py) checks the ones
it can measure: lightness and chroma by role, contrast, palette size, blue tints and vibrating
pairs. Text-colour counts and status hue families are yours to check.

- **Light ground:** L 0.96–1.00, C ≤ 0.015, tinted toward the brand's hue. Pure white is fine.
  Warm tints stay under C 0.008: a beige or cream page (hue ~60–100 at C 0.008 or more) is the
  second-wave tell unless the brief asks for it.
- **Surfaces:** a lightness step of 0.02–0.06 from the ground, either way, C ≤ 0.02.
- **Large areas** (anything over about a quarter of the viewport: ground, surfaces, sections,
  sidebars) stay at C ≤ 0.02. A full-strength colour field is a signature item, counted against
  the intensity (none at Calm, one per page at Balanced, one per view at Bold), and never sits
  behind body text.
- **Ink:** L 0.18–0.35, C ≤ 0.03. Not `#000` on `#FFF`; maximum contrast glares for some readers.
- **Text contrast:**
  - body text ≥ 7:1 and APCA Lc 75 or more, 90 preferred (Apple asks to "strive for 7:1");
  - secondary text ≥ 4.5:1, Lc ≥ 60, made by colour, not by lowering opacity;
  - at most three text colours;
  - no grey text on a coloured ground; tint it from that ground instead.
- **Palette size:** 2–3 core colours + 1 accent. Neutrals and status colours don't count.
- **Accent:** C 0.07–0.20 (enough to stand out from the neutrals, not more), covering ≤ 5 % of a
  view. It marks action, focus and selection, not
  headings or decoration. One saturated hue per view, plus the status colours.
- **No vibrating pairs:** never put two saturated hues (C > 0.12) of opposite temperature side
  by side, or one as text on the other. Saturated red next to blue is the classic case.
- **Status colours** stay in the green, amber, red and blue families people already read. Tune
  their lightness and chroma to the palette, never their hue family.
- **Dark theme:**
  - Light mode is the default; use dark when the subject or brief calls for it (night use, media,
    terminals), and follow `prefers-color-scheme` when both exist.
  - Ground L 0.15–0.24, C ≤ 0.02. "Forest" means a hint of green, not a green page.
  - Each elevation step is L +0.03–0.05 lighter.
  - Body text L 0.88–0.94, not `#FFF`; secondary text still Lc 60.
  - Accents lighter and calmer: L ≥ 0.70, C ≤ 0.14.

## Type

- **Body size:** 16–18px; 17–20px on reading-heavy screens. Nothing someone has to read under
  14px; captions and legal text 12–13px at the least. Inputs on mobile ≥ 16px, or iOS zooms in.
- **Line height:** body 1.5 (1.45–1.6); single-line UI text 1.3–1.45; headings 1.1–1.25;
  display 1.0–1.1. Space between paragraphs ≥ 0.75em.
- **Measure:** 55–75 characters.
- **Sizes per screen:** at most 4–5 in an app, at most 6 on a marketing page.
- **Weights:** at most three. Body 400, emphasis 500–700, nothing lighter for text except the
  light-on-dark step below. Build hierarchy with size, space and colour before weight.
- **Tracking:** 0 for body; −0.01 to −0.03em for display sizes; +0.02 to +0.06em for caps and
  small labels.
- **Light text on dark** looks heavier: give it a little more line height, and in a variable face
  drop body text to about 350–375; a static face stays at 400.
- **Setting:**
  - emphasis in bold, not italic, underline or caps;
  - left-aligned, ragged right, never justified;
  - `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs.
- **Faces:** the text face is chosen for legibility and may be familiar; the display face is
  where character lives. See [typography.md](typography.md).

## Layout

- **Grid:** a regular grid by default. Asymmetry only where the content's parts are unequal, such
  as a reading column beside an index.
- **Alignment:** each view lines up on at most 3–4 vertical edges, and body text keeps one left
  edge. Centre only short single items.
- **Spacing:**
  - a scale on a 4px base, using 4–6 values per screen;
  - space between groups at least twice the space within a group;
  - space above a heading 1.5–2× the space below it;
  - at Calm, one section rhythm per page type ([Intensity](#intensity) sets how much it may
    vary).
- **Familiar placements** (Jakob's law: users spend most of their time on other sites): logo top
  left, navigation along the top or the left, search at the top, primary actions where the
  platform puts them. A novel placement only as the signature.
- **Focus:** one focal point per view, and at most one element at signature strength per
  viewport. Start with generous white space and take it away.

## Surfaces

- **Elevation:** one language per surface, a tone step, a border or a shadow, never stacked. Most
  elements sit flat; only things that float get a shadow.
- **Radius:** 2–3 values per screen.
- **Borders:** the width stays the same across states, so nothing jumps.
- **Glass and glow:** on one element at most, never by default.

## Motion

- Durations by role with a firm ease-out: micro-feedback 80–150ms, menus and small UI
  150–250ms, large panels up to 400ms. Exits run about 75 % of the entrance time.
- Travel 8–16px; no bounce.
- Nothing animates on actions people repeat all day.
- `prefers-reduced-motion` means fewer and gentler movements, not none.

## Craft floor

The browser's own surfaces, finished:
- `::selection` and `caret-color` tinted from the palette;
- a `:focus-visible` ring, 2px with a 2px offset;
- `color-scheme` and `<meta name="theme-color">` set;
- `text-underline-offset` around 0.15–0.2em on links;
- `tabular-nums` on numbers that line up;
- curly quotes, a real `…`, and a non-breaking space between a number and its unit;
- hover styles only under `@media (hover: hover) and (pointer: fine)`;
- no weight change on hover.

## Slop to avoid: both ends

- **Forced different:**
  - three or more distinctive axes at once (an unusual body face, a tinted page, an asymmetric
    grid and a loud accent together);
  - a display or era face set as body text;
  - grids chosen for "tension";
  - saturated or muddy grounds;
  - trend-stacking: glass, glow, mesh, mono labels, grid backgrounds and big radii together.
- **Sterile default:** flat white, thin grey borders, a generic font, no accent, nothing of the
  subject. Calm is not empty: the signature still has to be there.

## Checks (the comfort audit)

1. **Palette:** run `python3 scripts/palette-check.py 'ROLE[:name]=#HEX' …` on the tokens, both
   themes (the path is relative to this skill's folder; installed, it is `~/.claude/skills/ui-anti-slop/scripts/palette-check.py`). Fix every FAIL; fix each WARN or say why the brief needs
   it.
2. **Blur test:** blur the screenshot or squint. Exactly one thing should pop.
3. **Reading test:** read a real paragraph for two minutes on a phone and on a laptop, in light
   and dark. Does anything glare, vibrate or look muddy?
4. **Counts per view:** colours, type sizes, weights, radii and alignment edges, against the
   limits above. Count alignment edges on blocks (headings, paragraphs, tables, panels, the nav),
   not table columns or text inset inside a padded box.
5. **Large areas:** none above C 0.02, except the signature fields the intensity allows.
6. **Zoom:** at 200 %, nothing clips or overlaps.

Evidence: [research.md → Comfort](research.md#comfort).
