# Step 3: Type

Decides one family, or two clearly different ones, with roles, a scale, weights, widths and the
numeric and language features the content needs. It takes the Direction (era, material, voice,
intensity) and the real copy, and hands type tokens to layout, the logo's wordmark and the assets.

Type has two jobs, chosen separately:
- **The text face** sets body copy, UI labels, forms and tables. It is chosen for legibility, and
  it may be familiar: people read it for minutes at a time.
- **The display face**, if there is one, sets headlines at 24px and above. It is part of the
  signature, and it is where the subject's era and material show.

One family can do both. When it can't, the display face carries the character and the text face
stays quiet.

There is deliberately no "recommended fonts" list here. Every list of distinctive fonts becomes the
next default: the families that prompting guides suggested in 2024–25 (Space Grotesk, Fraunces,
Crimson Pro, Clash Display, Satoshi, Cabinet Grotesk, IBM Plex, Bricolage Grotesque, Newsreader)
are now themselves the tell. Candidates come from the method, each time.

## Method

1. **Read the subject for type.**
   - **Era:** when its world was formed.
   - **Material:** how its marks are made: pen, brush, chisel, stencil, press, screen.
   - **Voice:** formal, plain, loud.
   - **Reading mode:** long reading, scanning data, short signage, or code.
2. **Map that to a classification** before looking at any family. The table steers the display
   face. The text face usually comes from the calmer neighbours (humanist or grotesque sans,
   transitional or garalde serif), whatever the subject:

   | The subject's world | Classification to try |
   |---|---|
   | pen, brush, handwriting, the humane | humanist sans, garalde serif |
   | industry, transport, public signage | grotesque, neo-grotesque |
   | drafting, modernist programmes | geometric sans (a slop zone; only with a reason) |
   | 19th-century posters, machinery, print shops | slab, Clarendon |
   | law, government, newspapers, reference | transitional serif |
   | fashion, engraving, luxury print | didone, display sizes only with optical sizes |
   | stone, wine labels, architecture, monuments | glyphic, incised |
   | code, tabular data, terminals | monospace, only where there is real code or data |
   | hand-painted shop signs, menus | script or brush, display only |

3. **Find three candidates for each face from at least two sources:**
   - **Text face:** judge it on the legibility criteria below. Popularity doesn't disqualify a text
     face; a well-made, widely used family that sets long Indonesian copy comfortably beats a rare
     one. The ban list below still applies.
   - **Display face:** go outside the obvious. Skip the Google Fonts top 100 by popularity (when
     online, check the `popularity` field at `https://fonts.google.com/metadata/fonts`), and skip
     everything on the ban list.
   - Prefer families with real optical sizes (`opsz`) or widths (`wdth`) when the scale is wide,
     and true italics if the copy needs emphasis.
   - **App, dashboard and tool UI** may use the platform's `system-ui` stack as the text face when
     the brief says why (native feel, speed, dense data). The character then lives in the logo and
     the display face. Not for marketing or brand pages.
4. **Run the candidate checklist** (from Google Fonts' "checklist for choosing type"):
   - **Weights:** the ones the scale needs, with true italics.
   - **Languages:** the subsets the copy needs.
     - Indonesian uses basic Latin.
     - Vietnamese needs the `vietnamese` subset.
     - Javanese, Balinese and Sundanese scripts need Noto.
   - **Figures:** tabular, lining and oldstyle (`tnum`, `lnum`, `onum`) if there are numbers.
   - **Features:** small caps, alternates, a slashed zero where codes appear.
   - **Spacing:** the spacing and kerning at the sizes you'll use.
   - **Licence:** web embedding and self-hosting allowed for this project, and redistribution in
     the repo if it's public.
5. **Check the text face for legibility:**
   - a medium-to-large x-height and open apertures (`c`, `e`, `a`, `s` don't close up);
   - moderate stroke contrast and a normal width, not condensed or hairline;
   - distinct `I l 1`, `0 O`, `rn m`;
   - ordinary-looking figures: a zero that is slashed or dotted by default makes prices and times
     read like code ("Rp 35.ØØØ"). Fine for booking codes; for running text and prices, check
     that a plain zero is the default or reachable with a feature;
   - a true bold and italic, and good rendering on Windows and Android at 14–16px;
   - every language the copy needs.

   Set three paragraphs at 16px on a phone and read them. If anything about the face is the first
   thing you notice, it's a display face; move it up to headlines or drop it.
6. **Test with the real copy, at real sizes, in light and dark.** Use:
   - the longest real headline;
   - a real paragraph in each language;
   - the densest numeric table;
   - the button labels.

   For Indonesian, include long affixed words ("mempertanggungjawabkan", "ketidakberdayaan") and
   reduplication ("kupu-kupu", "sebaik-baiknya") and check that hyphenation and wrapping behave.
7. **Write down why each winner won**, citing the Direction ("grotesque with squared terminals
   for the display lines, from the 1960s railway reference; a quiet humanist text face because the
   timetable is read on phones in sunlight").

## Pairing

- **Exhaust one family first:** weight, width, optical size, case, size and spacing. Many good
  systems use one family.
- **Add a second family only for a reason:** a display face for the signature, a change of
  context (editorial next to data), or a missing feature (italics, a script, real code).
- **Two families must differ in structure** (construction, stress, aperture, width), not just in
  weight. Keep a family resemblance in x-height and stroke weight, and keep their eras
  compatible.
- **At most two families.** A monospace counts as one, and only where there is real code or
  tabular data.

## Numbers

The comfort floor's type numbers ([comfort.md → Type](comfort.md#type)) apply to every Direction.

- **Body size:** 16–18px; 17–20px on reading-heavy screens. Nothing someone has to read under
  14px; captions 12–13px at the least; inputs on mobile ≥ 16px.
- **Sizes and weights per screen:** at most 4–5 sizes in an app and 6 on a marketing page; at most
  three weights. Sizes far enough apart to read as different, not 16/18/20/24/28.
- **Scale ratio by product.** The product sets the ratio; the intensity caps it (Calm up to 1.25,
  Balanced up to 1.333):

  | Product | Ratio |
  |---|---|
  | dense UI, tables | 1.067–1.125 |
  | balanced app | 1.2 |
  | marketing | 1.25 |
  | editorial | 1.333–1.414 |
  | posters only | 1.5+ |

  Generate only the steps you use.
- **Measure:** 55–75 characters for body text; never more than 80 (WCAG 1.4.8). In CSS,
  `max-width: 60ch`–`70ch`.
- **Line height:**
  - body 1.5 (1.45–1.6), more for long lines, large x-heights and diacritic-heavy languages;
  - single-line UI text 1.3–1.45;
  - headings 1.1–1.25;
  - display at 48px+ 1.0–1.1.
  - Space between paragraphs ≥ 0.75em.
- **Weights:** body 400, emphasis 500–700, nothing lighter for text (except light text on dark,
  below). Build hierarchy with size, space and colour before weight. Not 100 against 900 on every
  section.
- **Tracking:** 0 for body; −0.01 to −0.03em on display sizes; +0.02 to +0.06em on caps and small
  labels. Light text on dark: a little more line height, and in a variable face body text at
  about 350–375; a static face stays at 400.
- **Setting:** emphasis in bold, not italic, underline or caps; left-aligned and ragged, never
  justified; `text-wrap: balance` on headings and `text-wrap: pretty` on paragraphs.
- **Data:** `font-variant-numeric: tabular-nums lining-nums` for tables, prices, timers and
  counters; add `slashed-zero` for codes. Confirm the font has `tnum`.
- **Variable axes:** leave `font-optical-sizing: auto` on. Use `wdth` to fit long words or dense
  columns. Don't max out axes for effect.
- **Display faces** belong at 24px and above; below that, use the text cut.

## Where fonts come from (check the licence of each family)

- **Google Fonts** (mostly OFL): the less-used families, especially ones with `opsz` or `wdth`
  axes. This is also what Figma serves, so a design that will live in Figma stays editable there.
- **Fontshare (ITF Free Font License):**
  - **allowed:** commercial use and self-hosting on your own sites;
  - **forbidden:** modifying (subsetting or converting formats), redistributing in public repos
    or templates, and offering the font as a choice inside a SaaS or design tool;
  - some families there are OFL instead.
- **Velvetyne:** libre, credit the designer and foundry. It has itself warned against everyone
  using the same few Velvetyne faces.
- **Collletttivo** (OFL, credit asked), **The League of Moveable Type** (OFL), and **uncut.wtf**
  (an index; check each source's licence).
- **Indonesia and Southeast Asia:**
  - Lafontype: Gantari (OFL);
  - Tokotype: Mohave (OFL; the rest of the catalogue is paid);
  - Cadson Demak's Thai/Latin families on Google Fonts;
  - Be Vietnam Pro;
  - Noto for regional scripts.
- **Traps:**
  - Dafont and FontSpace "free" fonts that are personal-use demos;
  - Figma Community files that redistribute commercial fonts (Gilroy, SF Pro);
  - "free font" listicles that are really adverts for commercial families.

**Figma Community** holds specimens, pairing boards and type-scale kits, not font files. The
useful ones put real copy in editable specimens, such as Tiptop Type's "Free Fonts in Editable
Components", Smith & Diction's "Usable Google Fonts" and IBM's Carbon type sets. Use them to test
candidates, not to pick a pairing someone else made.

## Slop to avoid

- **The first-wave defaults:** Inter, Geist, Roboto, Arial, Open Sans, Lato, Poppins, Montserrat,
  the system-ui stack.
- **The "distinctive" repeats:** Space Grotesk, Plus Jakarta Sans, DM Sans, Outfit, Manrope, Sora,
  Playfair Display + Inter.
- **The seeded second wave:**
  - Instrument Serif: "the default output of vibe-coded web work";
  - Fraunces: the indie-SaaS display serif;
  - Bricolage Grotesque, Newsreader, Crimson Pro, IBM Plex;
  - the Fontshare starter pack: Satoshi, General Sans, Clash Display, Cabinet Grotesk, Switzer
    ("Clash Display + Satoshi body is now a look, not a choice");
  - Söhne as the AI-company house sans.
- **Stock combinations:** serif display + grotesk body + mono labels as a trio; an oversized
  italic serif hero, especially roman and italic mixed in one line; mono on headings or body text
  that isn't code.
- **Scale tells:**
  - 100 vs 900 weight with 3× size jumps on every section;
  - variable axes maxed for effect (`wght` 900, `opsz` 144, Fraunces SOFT/WONK);
  - display faces under 24px;
  - hero headlines wrapping to 5–6 lines.
- **Styling tells:**
  - gradient text;
  - one word of a headline in italic or the accent colour;
  - a tracked ALL-CAPS eyebrow above every heading;
  - tracking-tight bold on every heading;
  - Title Case Everywhere;
  - 0.1em tracking or all caps on running text.
- **Forced type:**
  - an era, display or novelty face set as body text;
  - a text face chosen for rarity over legibility;
  - body under 16px, line height under 1.45 on paragraphs, or more than three weights.
- **Technical failures:**
  - faux bold or italic because the real styles weren't loaded;
  - proportional figures in tables;
  - headings and body too similar to scan.

A brief or an established brand that uses one of these wins; these are bans on *defaulting*.

## Checks

- Can you say in one sentence why this family fits this subject, citing the Direction?
- Do three paragraphs of the text face at 16px on a phone read without effort?
- Would you have picked the same family for the last three briefs? If yes, it's a default.
- Real copy, longest headline and densest table all set without breaking?
- Every weight and italic used is actually loaded, with no faux styles?
- Body 16px+, line height 1.45–1.6, measure under 80ch, at most three weights; contrast passes at
  the sizes used?

Evidence: [research.md → Fonts](research.md#fonts).
