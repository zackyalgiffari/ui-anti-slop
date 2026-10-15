# Step 5: Assets

Decides the icons, illustration, photography, patterns and textures, and the generated images
(favicon, social preview). It takes the Direction's material nouns, the colour tokens and the
logo's geometry, and hands layout a small, consistent set of assets. Fewer, better assets beat a
library of generic ones.

## Method

1. **Ask whether each asset needs to exist.** "Icons are punctuation." If a feature can be shown
   (a screenshot, the real product, a real photo, the real data), show it instead of symbolising
   it. A feature grid that explains itself with a rocket, a lightbulb and a shield is a sign that
   nobody knew what to write.
2. **Icons: choose deliberately, then make the set your own.**
   - **Choosing.** If a library fits the Direction, choose it for a reason: its weight, corners
     and terminals, not because it was already installed. The 24px / 2px / round-cap family
     (Lucide, Feather, Heroicons, Untitled UI) all read alike, so swapping one for another changes
     nothing.
   - **Making it your own.** Change what stock sets fix: stroke weight, cap and join (butt or
     square caps for a technical subject, round for a soft one), corner radius, a solid or duotone
     weight, or a strict pixel grid. Phosphor's weight family and Pixelarticons show how far a
     single grammar can go.
   - **Custom icons.** For icons the product owns, draw a small custom set as SVG on a written
     spec derived from the logo. Lucide's design guide is a good template for the spec:

     ```
     canvas      24×24, ≥1px padding (live area 22×22)
     stroke      one width for the whole set (e.g. 1.5 or 2), centred
     caps/joins  one choice for the set (round | square | butt+miter)
     corners     radius rule, e.g. 2px on shapes ≥8px, 1px below
     spacing     ≥2px between separate elements
     weight      match the visual weight of a reference circle and square
     colour      currentColor, so icons follow text colour
     ```

   - **Never mix two icon sets** on one screen.
   - **Sizing:** icons sit beside text at the text's size (often 1–1.25em), not in coloured
     circles above every heading.
3. **Illustration: build it from the brand's own shapes.**
   - Use the logo's geometry, the icon rules (stroke, corners) and 2–3 palette tokens. An
     illustration made from the same parts as the mark looks like it belongs to the brand.
   - Keep the style to one: flat shapes, line drawing, cut paper, or engraving-like hatching. Pick
     the one the material world suggests.
   - If the subject has real things (products, places, people, documents), photograph or draw
     those, not metaphors.
4. **Photography: write a direction before choosing or generating any image:**

   ```
   subject   who / what is in frame, doing what (real staff, real product, real place)
   light     time of day, hard or soft, direction
   place     where, with which details visible
   crop      tight / environmental / overhead; where the space for text goes
   grade     warm / neutral / cool, contrast, grain, taken from the palette
   ```

   - Use real photos of the actual people and things whenever they exist. Nielsen Norman Group's
     eyetracking shows people ignore generic stock people and decorative "feel-good" images, but
     look at real staff photos.
   - Prefer no image to a decorative one.
   - One strong, real image is often the best signature: it carries the subject so the type,
     colour and layout around it can stay calm. Text over a photo is checked at its worst spot,
     with a scrim if needed.
5. **Patterns and textures: from the material nouns.** Woven, printed, stamped, engraved, tiled,
   painted. Draw them as an SVG `<pattern>` or a small tiled SVG, with tokens for colours. Use one
   pattern, at full strength in one place (it then counts as a signature item), or faintly (about
   APCA Lc 15 or less against the ground) behind content that isn't body text. Never behind
   paragraphs, forms or tables, and not everywhere.
6. **Generated assets:**
   - the favicon and app-icon set (see [logo-svg.md](logo-svg.md#favicon-and-app-icon-set));
   - a social preview image (1200×630) built from the real headline, the logo and one brand
     element, not a gradient with a slogan;
   - empty-state and error illustrations from the same kit as the rest.
7. **Write the asset kit into the brief:** the icon source and spec; the illustration style and
   its building blocks; the photo direction; the pattern; and which assets this screen actually
   uses.

## Slop to avoid

- **Icons:**
  - a stock 24px / 2px / round-cap set used as shipped for everything, including decorative
    feature icons;
  - two icon sets mixed together;
  - an icon in a coloured circle or rounded square above every heading;
  - rainbow icon chips;
  - emoji used as icons;
  - the ✨ sparkle for "AI".
- **Illustration:**
  - Corporate Memphis / "Alegria" figures: flat, long limbs, small heads, purple or blue skin,
    high-fiving or watering plants;
  - unDraw-style scenes with one recolourable accent, which match every brand and so belong to
    none;
  - Notion-style line people;
  - people gathered under a giant lightbulb for "ideas";
  - empty states as a pale blue blob behind an envelope, magnifier or card;
  - glossy or clay 3D figures and emoji;
  - frosted-glass or iridescent 3D icons;
  - isometric workspace scenes;
  - abstract gradient meshes and blurred blobs standing in for a hero image.
- **Photography:**
  - decorative stock photos of generic people that carry no information;
  - AI-generated photos with waxy skin, lettering that falls apart, light that doesn't match
    between subject and background, repeated crowd or foliage detail, or wrong grips on objects.
- **Backgrounds:** grid or dot backgrounds, aurora blobs and glow orbs (see the guardrails in
  `SKILL.md`).

A brief or an established brand that uses one of these wins; a design system's own icon set is
used as is.

## Checks

- **Swap test:** could each asset appear unchanged on a competitor's site? If yes, make it
  specific or remove it.
- **Consistency:** are all icons on one grid with one stroke, cap and corner rule? Is all the
  illustration in one style?
- **Necessity:** does every image either show something real or carry information?
- **Licences:** are photo, illustration and icon licences recorded?

Evidence: [research.md → Assets](research.md#assets).
