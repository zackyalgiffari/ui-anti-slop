# Step 4: Logo, drawn as SVG

Decides the mark, its concept, and the files that carry it. It takes the Direction (subject,
material nouns, reference), the colour tokens and the type decision. It hands on:
- a master SVG;
- one-colour and reversed versions;
- lockups;
- a favicon set;
- for a brand job, a one-page usage sheet.

**Always draw the logo by hand as SVG code:** paths you write and reason about, on a grid. Never
use a font in a `<text>` element, an emoji, an icon from a library, or a generated bitmap. Writing
the geometry yourself is what makes the mark specific, and it keeps the file small, sharp and
editable.

Not every job needs a new logo. If the brand has one, use it as supplied. If the brief only needs
a placeholder, say so and draw a plain wordmark rather than inventing a symbol.

## Method

1. **Write the concept in one sentence, from the subject.** For example: "the canting's spout
   drawing a single wax line that becomes the W". The concept can come from:
   - the name's meaning or sound;
   - the product's own shape or action;
   - the place, a material, or a founder's story.

   If you can't write the sentence, you don't have a concept yet. "A modern, clean mark that
   conveys innovation" is not a concept.
2. **Decide symbol or wordmark.** A symbol needs a reason (Sagi Haviv): a long name, sub-brands
   to unite, or the need for a small shorthand such as an app icon. Without a reason, make a
   wordmark: the name, set well and given one or two custom details. Most small projects want a
   wordmark plus a monogram for the favicon.
3. **Explore three different concepts as rough SVG,** not three colourings of one idea. Render
   them small, side by side, in one colour. Drop the weakest, and say why.
4. **Run the shelf test.** List what the category already uses: search "[category] logo" if you
   can browse, or recall the obvious ones. If your mark could sit on that shelf unnoticed, change
   it. Also check it against the cliché list below.
5. **Build the master on a grid.**
   - **Canvas:** `viewBox="0 0 256 256"` for a symbol; for a lockup, keep the height and vary
     the width (e.g. `0 0 960 256`).
   - **Snapping:** snap the key points to 8 or 16 units, and keep coordinates as integers or at
     most 2 decimals.
   - **One logic, applied everywhere:** one stroke weight, one corner radius (or none), and one
     terminal style (flat, round or angled).
   - **Exact angles:** 0, 15, 30, 45, 60 and 90°. An edge 1–3° off a clean angle looks like a
     mistake.
   - **Smallest detail:** no detail smaller than about 1/48 of the mark; it will vanish at 16px.
6. **Make the optical corrections.** Geometry that is mathematically equal looks unequal:
   - **Overshoot:** round shapes and points overshoot the baseline and cap line by about 1–3 %, or
     they look smaller than the flat shapes.
   - **Horizontals:** draw them slightly thinner than verticals.
   - **Triangles:** sit them slightly lower, or they look like they float.
   - **Reversed versions:** for white on dark, thin the strokes a little, because they look
     heavier.
   - **Centring:** centre by visual mass, not the bounding box.
7. **Finalise the geometry.**
   - **Outline every letter:** no `<text>`; keep the outlining script, or a note of the font and
     settings, so it can be redone.
   - **Expand strokes into filled shapes:** no `stroke` in the master.
   - **Merge touching same-colour shapes** so no hairline seams appear.
   - **Close every path** with `Z`.
8. **Make the variants:**
   - **Full colour:** at most 2–3 colours, each one a palette token.
   - **One colour:** `fill="currentColor"`, so CSS `color` sets it.
   - **Reversed:** for dark grounds, adjusted optically, not just recoloured.
   - **Lockups:** horizontal (mark + wordmark) and stacked. Align the mark to the wordmark's cap
     height or x-height by eye, not to the bounding box.
   - **Favicon mark:** simplified for 16–32px, dropping details that won't survive. Hand-tune a
     separate 16px drawing if the scaled one blurs.
   - **Clear space:** in units of the mark itself, e.g. "half the mark's height on every side".
     Also set a minimum size.
9. **Test in the preview sheet** (`assets/logo-preview.html`; see below). Fix what fails, then
   test again.
10. **For a brand job, write a one-page usage sheet:**
    - the concept sentence;
    - the primary logo and its alternates;
    - scaling, clear space and minimum size;
    - the colourways, with the logo on each palette colour;
    - co-branding next to a partner's logo, if that will happen;
    - 4–6 misuses: stretched, recoloured off-palette, on a busy photo, rotated, outlined, given
      effects.

## SVG authoring rules

```svg
<!-- Structure only. The shape is a placeholder: replace it, don't reuse it. -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256"
     role="img" aria-labelledby="logo-title">
  <title id="logo-title">Name of the brand</title>
  <!-- one colour: fill inherits CSS `color` -->
  <path fill="currentColor" fill-rule="evenodd"
        d="M48 48H208V208H48Z M112 112V144H144V112Z"/>
</svg>
```

- **Root and accessibility:**
  - `xmlns` and a square integer `viewBox`;
  - no `width`/`height` in the master (the embedding context sizes it), and no `x`/`y` on the
    root;
  - `role="img"` with a `<title>`, referenced by `aria-labelledby`, or an `aria-label` (not both);
  - if the visible brand name sits right next to the mark, use `aria-hidden="true"` instead.
- **Fills, not strokes:** explore with strokes if that's faster, then expand them into outlines
  for the master. A mark meant to read at 24px needs strokes of at least about 8 % of its width.
- **Counters:** holes such as the inside of an O use `fill-rule="evenodd"`, or an inner subpath
  wound the opposite way.
- **Overlapping shapes in one path:** under the default `nonzero` rule, subpaths that overlap must
  wind the same way (all clockwise), or the overlap becomes an accidental hole. Under `evenodd`,
  *every* overlap becomes a hole. So either:
  - draw all outer shapes clockwise and every counter anticlockwise, with `nonzero`; or
  - put overlapping shapes in separate `<path>` elements.

  The preview sheet's lint flags overlapping subpaths that cancel out.
- **Curves:** use arcs (`A`) for true circular segments. For a quarter circle as a cubic, put the
  handles at 0.5523 × the radius. Put anchor points at the curve's extremes (top, bottom, left,
  right) with horizontal or vertical handles, as type designers do. Fewer anchors means smoother
  curves.
- **Computed geometry:** when the geometry is rotated, repeated or derived (a ring of 7 cuts, a
  shape on a 30° grid), compute the points with a short script and paste the rounded numbers,
  rather than eyeballing them.
- **Keep the master plain:**
  - no `filter`, blur, drop shadow, `mask` or `clipPath`;
  - no `<image>`, external `href` or `<style>` that the mark depends on;
  - no embedded fonts or scripts.

  A gradient may exist only as an optional variant, beside a flat master. A gradient that is
  needed to make the mark look good means the form is weak.
- **Size:** a symbol is usually 1–6 paths and a few dozen anchors. Hundreds of anchors means
  traced or over-detailed artwork; simplify it.
- **Strict profile, when the logo goes into email/BIMI:** SVG Tiny P/S, which means
  `baseProfile="tiny-ps"`, a `<title>` of 64 characters or fewer, square, no scripts or external
  references, and under 32 KB.

### Outlining a wordmark from a font

Start from a family whose licence allows use in a logo. OFL does; check anything else. Then
modify it: a cut terminal, a joined pair, adjusted spacing. To get the outlines as paths, use
Python `fontTools` (`pip install fonttools` in a virtualenv):

```python
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

font = TTFont("Family-Bold.ttf")
glyphs = font.getGlyphSet()   # variable font: font.getGlyphSet(location={"wght": 650})
cmap = font.getBestCmap()
x, parts = 0, []
for ch in "Name":
    name = cmap[ord(ch)]
    pen = SVGPathPen(glyphs, ntos=lambda n: "%g" % round(n, 1))
    glyphs[name].draw(TransformPen(pen, (1, 0, 0, -1, x, 0)))  # flip y; advance x
    parts.append(pen.getCommands())
    x += glyphs[name].width
print(" ".join(parts))   # font units, baseline at y=0, so set viewBox to fit
```

This ignores kerning, which is fine: space a wordmark by eye. Then edit the paths by hand for
the custom details. If no font file is available, draw the letters from construction, which
suits monoline or geometric wordmarks.

## Favicon and app-icon set

| File | Size | Notes |
|---|---|---|
| `favicon.ico` | 32×32 (+16×16 if hand-tuned) | for old browsers and tools |
| `icon.svg` | vector | `<style>@media (prefers-color-scheme: dark){…}</style>` swaps the colours |
| `apple-touch-icon.png` | 180×180 | solid background, about 20px padding |
| `icon-192.png`, `icon-512.png` | 192, 512 | referenced from the web manifest |
| `icon-maskable-512.png` | 512 | the mark inside the central 409px safe circle |

For app icons the symbol fills about 60–70 % of the tile. Rasterise with whatever is available:
`rsvg-convert`, Inkscape, ImageMagick, or a headless-browser screenshot of the SVG at the exact
size.

## The preview sheet

`assets/logo-preview.html` (next to this skill's `SKILL.md`) is a self-contained page.

1. Copy it into the project or a scratch folder.
2. Set `--ground`, `--ink`, `--brand` and `--accent` at the top to the palette tokens.
3. Paste the master into `<template id="mark">` and, optionally, the horizontal lockup into
   `<template id="lockup">`.
4. Open it and take a screenshot.

The sheet shows:
- **sizes** 16–256px;
- **pixel truth:** the real 16px and 32px rasterisation, enlarged;
- **colourways:** full colour, one colour, reversed, and on the brand colour;
- **stress tests:** mirrored, rotated 180° and a squint blur;
- **a grid overlay**, to check snapping;
- **the mark in context:** a nav bar and a browser tab;
- **a lint panel** that flags `<text>`, strokes, filters, masks, gradients, a non-square
  `viewBox`, a missing `<title>` and a high anchor count.

## Slop to avoid

Marks that read as "generic startup" or "AI company":
- **The AI ring:** a circle (often gradient-filled) with a central opening, elements radiating
  from the centre, soft organic curves.
- **Rings and circles:** rings with a break; overlapping or intersecting translucent circles.
- **The rounded or "swirling" hexagon:** often with an empty centre, or isometric as a cube.
  Hexagons are 4.6× more likely in AI logos than in logos overall (Fast Company, from USPTO
  data).
- **Implied rotation around a centre:** a vortex or whirlpool of blades or loops.
- **A little robot face:** a rounded shape with two blank dot eyes.
- **An infinity symbol,** or an A without its crossbar.
- **Dots or lines** radiating out or converging in: iris, orbit, network hub, neural nodes.
- **The ✨ sparkle or four-point star.** In Nielsen Norman Group's test, nobody read it as "AI";
  people read it as favourite, effects, new or rewards.
- **A letter in a rounded square, or initials in a basic shape,** set in an unmodified stock font.
- **The common clip-art:** the swoosh, the globe, rising bars or an arrow chart, the V-shaped
  person, the "human ring" of joined figures.
- **Category clip-art:**
  - SaaS: chat bubbles, charts, padlocks;
  - finance: coins, piggy banks, bank blue;
  - health: crosses, pills, heartbeat lines.
- **A gradient (purple→blue, teal→magenta), glow or bevel** carrying a weak form.
- **An evenly weighted geometric-sans wordmark with no detail of its own.**
- **More than three colours** without a reason.
- **Live `<text>` in an SVG logo.** A missing font gets substituted and the logo changes.

## Checks

- Can you say the concept in one sentence, and does the mark show it?
- Does it hold at 16px in the pixel-truth view? In one colour? Reversed?
- Mirrored and rotated 180°: no unintended reading?
- Shelf test: would it disappear among the category's logos?
- Is the lint panel clean: no text, strokes, filters or masks, and a reasonable anchor count?
- Does the colour come from the palette tokens, with the master still working in one colour?

Evidence: [research.md → Logos](research.md#logos).
