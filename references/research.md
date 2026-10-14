# Research: what makes a UI read as AI-generated

Compiled 2026-10-14 in three passes.

- **First pass:** a browse of Figma Community (the landing-page, SaaS and Figma Make galleries)
  plus published critiques of AI-generated UI.
- **Second pass, the same day:** went deeper on direction, logos, fonts, assets, layout and
  surfaces. Its sources were:
  - Figma Community, read through its public search API, because the community pages returned 403
    to plain fetches;
  - published critiques;
  - the token packages of real design systems.
- **Third pass, the same day:** a visual check in a regular Chrome session, where Figma Community
  pages and thumbnails load normally. It also reopened the sources that had returned 403 to the
  headless browser. Findings from this pass are marked *(visual check)*.

Every source under Sources was opened, not just seen in search results. Claims that could not be
checked are marked **unverified**.

## Figma Community

### Templates that read as designed

Their identity comes from the subject, not from a "tech" palette.

- **Saltmere** (boutique hotel): sea green with a serif-italic headline ("Where the tide sets the
  pace"), photography of the place.
- **Hale & Ward** (law firm): paper and ink, a large serif headline ("Clear counsel when the
  matter can't wait"), one black CTA, a real photo of people at work.
- **Langus Burgers** (restaurant): cream and red display type, the food itself as the hero.
- **Flora**, **Varenne**, **Arché**: patterned stripes, oxblood, stone and photography; each
  palette is borrowed from the product's material world.
- **Liftoff** (SaaS): black with a single orange accent, but the hero is the actual product
  dashboard, not an abstract glow.

### Templates that read as generic

They are almost all in the "AI SaaS" category.

- **Sutro** ("Keep the final say"), **Cyberheads**, **Cybersecurity X**: navy background with a
  blue glow. This is the navy look the rule bans.
- **Skysoft**, **Axion**: purple gradients.
- **Builderflow** ("Build AI that feels like magic"): pastel 3D blobs.
- **Aeonex**, **Aoutive**: a centred "Build AI workflows that run your business" hero over a
  pale gradient.

### Figma Make (AI-generated projects)

- **Most liked:** small, specific and interactive things, such as the eye-following card, the
  shader reminder, the fortune cookie and the minimalist sidebar.
- **The forgettable ones:** the dashboards. Four KPI cards with rainbow icon chips, slate/navy
  panels (MIDI Controller, ATS Resume Analyzer), and centred "Build consistent design systems at
  scale" heroes.

## Why models converge

- **Distributional convergence.** Without direction a model picks the most probable choice, which
  is the most common one in its training data: purple gradients on white, Inter, centred layouts
  (Anthropic cookbook).
- **Tailwind's legacy.** Tailwind UI made `bg-indigo-500` the default button colour, tutorials
  copied it, and models learned it. Adam Wathan later apologised for it (reported by prg.sh).
- **shadcn's legacy.** Slate is the most popular shadcn/ui base colour, so `slate-900`
  (`#0F172A`) and `slate-950` (`#020617`) anchor a large share of SaaS dashboards
  (designrevision).

## Catalogue of tells

### Colour

- `slate-900` with `indigo-600`, purple-to-blue hero gradients, and glows behind cards (codemyspec).
- Violet `#7C3AED` fading to blue `#3B82F6`; cyan `#00D4FF` on near-black (pixelslop).
- `linear-gradient(135deg, #667EEA, #764BA2)`; glow shadows such as `0 0 80px rgba(120,80,200,.6)`
  (Laith0003 ban list).
- The "Linear aesthetic": a dark hero, `#5E6AD2` and aurora backgrounds (dev.to/jaainil).

### Typography

- **Families:** Inter, Roboto, Arial, Open Sans, Lato and system fonts. Anthropic's guidance says
  never use them, and notes that models then converge on Space Grotesk instead.
- **Inter and Geist** are named as the faces that make unrelated products look alike
  (impeccable.style).
- **Treatments:**
  - gradient text on headings
  - one word of a headline in italic or the accent colour
  - a tracked ALL-CAPS eyebrow above every heading
  - Title Case everywhere
  - weights limited to 400/500

### Layout and components

- **Stock page order:** centred hero, pill badge, two buttons, logo row, three feature cards,
  pricing, CTA (capitalandcompute, codemyspec).
- **Cards:** `rounded-2xl` with `shadow-lg p-6` on every card; an icon in a coloured circle above
  every heading; emoji used as icons (codemyspec, pixelslop).
- **Card decoration:** nested cards, multicoloured left borders, and status dots that mean
  nothing (Fountain Institute). The thick coloured left border is called "the single most
  recognisable signature" (noqta.tn).
- **Hero metric:** a big number with a small label and a gradient accent (Anthropic SKILL.md).

### Effects and motion

- **Surfaces:** glassmorphism, blurred orbs, grid/dot backgrounds and spotlight glows.
- **Uniformity:** one radius and one padding everywhere.
- **Motion:** fade-and-slide-up on every section, hover-scale on every card, `transition-all`,
  pulsing dots.

Sources: pixelslop, impeccable.style, kostac, Anthropic SKILL.md.

### Copy

- **Verbs:** Unlock, Elevate, Empower, Transform, Supercharge.
- **Phrases:** "Seamless integration", "all-in-one platform", "the future of work".
- **Fake data:** invented round stats, "John Doe" testimonials, "Acme" placeholders.
- **CTAs:** "Get Started" or "Learn More" repeated three or more times, and headings that repeat
  their own subtext.

Sources: Laith0003, codemyspec, capitalandcompute, kostac, pixelslop.

## The second wave

Once a model is told "no purple", it drifts to a new set of defaults. Anthropic's current
frontend-design skill bans these too:

- a warm cream background (about `#F4F1EA`) with a high-contrast serif and a terracotta accent
  (about `#D97757`);
- a near-black background (`#0B0B0B`, `#111`) with one acid-green or vermilion accent;
- broadsheet layouts with hairline rules and zero radius;
- template chrome: middle-dot meta strings, "→" on every link, and monospace micro-labels.

The same thing happened to fonts. Anthropic's prompting cookbook suggested, by category:
- Code: JetBrains Mono, Fira Code, Space Grotesk.
- Editorial: Playfair Display, Crimson Pro, Fraunces.
- Startup: Clash Display, Satoshi, Cabinet Grotesk.
- Technical: IBM Plex, Source Sans 3.
- Distinctive: Bricolage Grotesque, Obviously, Newsreader.

It also suggested "display + monospace" and "100/200 vs 800/900 weights, size jumps of 3x+".
Models now reach for exactly these. An earlier version of this file even recommended IBM Plex,
Bricolage Grotesque, Newsreader, Crimson Pro and Fraunces as alternatives. Any named list of
"distinctive" fonts turns into the next default, so the skill gives a method instead (see
[Fonts](#fonts)).

The rule therefore bans these as fallbacks, not just the first-wave purple and navy.

## What designers recommend instead

- **Palette.**
  - Use 4–6 named hex tokens with roles, chosen from the brief's own world.
  - Use dominant colours with sharp accents rather than "timid, evenly-distributed palettes".
  - Treat accent colour as a budget for the whole page.
  - A worked example: petrol teal `#146B68`, bronze `#97652B` and sage `#556A38` on `#FDFCF9`
    (codemyspec).
- **Dark themes.** Use deep greens, petrol blues or warm neutrals built from one brand seed, not
  slate (dev.to/jaainil).
- **Type.**
  - Use one family used decisively, or two that differ in structure.
  - Choose them from the subject (era, material, voice, reading mode) through a classification,
    not from a list. The lists critics give become the next defaults; see [the second
    wave](#the-second-wave).
- **Layout.**
  - Open with the most characteristic thing of the subject.
  - Use left-aligned or uneven splits (7+5, 8+4) and real product screenshots.
  - Vary radius by role: inputs 4–6px, cards 8–16px.
- **Motion.** One orchestrated moment, or motion that answers a user action.
- **Restraint.** Remove one element that doesn't serve the brief before shipping.

## Direction methods

- **Style tiles** (Samantha Warren, A List Apart):
  - Gather adjectives with metaphor questions ("if your website was a vehicle, what vehicle would
    it be?") and opposing word pairs, each end tied to a reference.
  - Count and rank the adjectives that come back.
  - Turn each adjective into one visual decision. In the Washington Examiner example:
    - "patriotic" became red, white and blue;
    - "patriotic" plus the paper's history became slab serifs;
    - "strong" became brushed aluminium and stars.
  - A tile has no layout. Three tiles were shown and merged into an approved fourth.
- **Personality sliders** (GV Brand Sprint):
  - elite ↔ mass appeal, serious ↔ playful, conventional ↔ rebel, friend ↔ authority, classic ↔
    young;
  - "true brand personality often lies at the ends of these spectrums".
- **"X but not Y"** (Mailchimp voice guide): "weird but not inappropriate", "smart but not
  snobbish".
- **Hike One design direction:** up to three named themes, each described in words, then a
  moodboard with a written rationale per theme, then a style tile.
- **Figma Community:**
  - Moodboard Kit 3.0 (Mixpanel, about 113k uses): layout only, no method.
  - Moodboard Template: 8 Category Direction Board (Heles Ofalius): references split into
    culture, photography, lighting, design style, mood, texture, colour and composition.
  - Style Tile Examples (Julie), Brand Sprint (Igor Silkin), Brand Strategy Workshop (Arek
    Dvornechuck), The Brand Design System (Open Session).
- **Inference, not sourced:** "modern / clean / minimal / sleek" fit every brand, so they decide
  nothing.

## Logos

### Figma Community logo and brand files

- **Real brands' kits:**
  - Obsidian Logo and App Icons (Steph Ango): the concept comes from the name; obsidian is the
    volcanic rock "used since the dawn of humanity to make arrowheads". The brand page says the
    whole logomark is "either black or white".
  - Figma Brand Book; Monad Brand Guidelines.
- **Construction:**
  - Logo Grid For Product icons uses Material's 400 % method: a 192×192 canvas with keylines,
    exported at 48dp.
  - Logo Blueprint and App Logo – Builder Template.
- **Briefs tied to a subject** *(visual check)*:
  - **Kokoro Branding** (Yuliia Hrabynska, about 2.7k uses), a fictional Tokyo coffee shop:
    - identity: a wordmark only, with no symbol, in a heavy condensed lowercase sans;
    - palette: pale matcha-yellow and black;
    - imagery: real photographs of the café, cups and packaging do most of the work.

    The file's own description is slop copy ("Indulge in the essence…", "a fusion of tradition
    and innovation", "a journey of flavor discovery"): crafted visuals don't protect the words.
  - **Waybill Brand Guidelines Template** (Abdulsamad Umar, about 4k uses, CC BY 4.0), a
    fictional Nigerian logistics firm. Oxblood and pink, not a "tech" palette. The deck runs:
    - brand foundation, including an archetype ("The Caregiver") and a tagline;
    - logo;
    - colour;
    - typography;
    - real photography of people;
    - verbal identity ("approachable, friendly, humorous");
    - elements;
    - applications.

    The logo section alone covers primary logo, alternates, scaling, minimum size, clear space,
    co-branding with partners, the logo on each colour, and misuse.
  - Ramen House was named by the second pass but not opened.
- **Generic:**
  - Abstract 99+ Logo Pack ("72 placeholder logos… 9 categories", including AI);
  - Kenja Brand Design Kit – AI Branding, which styles a category, not a subject;
  - Noisy Mesh Gradient Logos, where the effect is the idea;
  - Open Logo (about 73k uses) and Untitled UI's 180+ placeholder logos.

  Inference: placeholder packs like these are the "startup logo average" that models learn from.
- **What the generic packs contain** *(visual check)*:
  - **Open Logo:** white-on-black placeholder marks, including a burst of radiating lines, a
    stacked-triangle tree and interlocking letter shapes.
  - **"Logos" by Paco** (about 20k uses): monoline geometric letters and an eye/ring.
  - **VectorStock's "100 Free Logo Design Templates":** almost entirely initials in circles or
    shields, leaves, lotuses, house roofs, swooshes, fox heads and crowns.
  - **"AI Network Logo Template":** a square mesh of dots joined by lines, in an indigo→blue
    gradient. It is the neural-node cliché, literally.
- **AI-company logos side by side** *(visual check)*: "AI logos – ChatGPT, Perplexity, Claude…"
  (ByeWind, about 9.5k uses) shows 12 real AI-product marks.
  - 6 are rings, knots or rosettes with radial symmetry.
  - 6 use multi-stop pink→blue or purple gradients, one of them the four-point sparkle.
  - The ones that stand apart come from a name or an idea: a sailboat line drawing, and a
    letter pair on a flat tile.

  A second file, "AI Product Logos", uses a ✨ cluster and purple gradient text on its own
  cover.
- **What a guidelines deck contains:**
  - Corbault's deck (about 11k uses): logo, logo in situations, moodboard, colours, size and
    white space, type, logo on background, pattern.
  - Spotify's guidelines give real values:
    - minimum size 70px (21px for the icon alone);
    - clear space of half the icon's height;
    - fixed colour versions;
    - a misuse list (rotate, stretch, recolour, put on busy or low-contrast backgrounds).

### Clichés

- **The "AI ring"** (velvetshark): a circle, often gradient-filled, with a central opening and
  elements radiating from the centre. The fixes it gives: sharp angles, negative space, no radial
  symmetry, "skip the gradient".
- **The swirling hexagon** (James I. Bowie, Fast Company, April 2023; opened in the third pass):
  - From USPTO trademark data, hexagons are "4.6 times more likely to appear in AI logos than in
    logos as a whole", close to the figure for crypto logos (5.4×).
  - OpenAI's mark is a "stylized hexagon". Implied rotation around a central point (a vortex) is
    "becoming a hallmark": DeepMind, Stability AI and Synthesia.
  - Other AI-logo habits it names:
    - minimalist little robots with "a pair of dark eyes staring rather blankly";
    - crossbar-less As;
    - infinity symbols, shared with crypto logos.
  - 1980s AI logos used abstract human heads instead.
- **The convergence catalogue** (braindetox):
  - rings, rings with a break, overlapping circles;
  - rounded hexagons with empty centres;
  - dots or lines radiating or converging (iris, orbit, hub);
  - purple→blue and teal→magenta gradients;
  - evenly weighted sans wordmarks.
- **The ✨ sparkle:** in Nielsen Norman Group's test "no one attributed the concept of artificial
  intelligence to the icon". People read it as save or favourite, effects, new, or rewards.
- **Generic marks** (Vistaprint, DesignCrowd): the V-shaped person, the globe, rising graphs,
  initials in a geometric shape, swooshes, "human rings", connectivity lines, and basic shapes
  used alone.
- **kaankiziltug/logo-design-skill** (MIT, an earlier Claude logo skill):
  - red flags: "generic initials in an unmodified stock font"; "gradients or shadows used to
    rescue a weak form"; more than 3 colours without a reason;
  - category clichés: chat bubbles, charts and padlocks for SaaS; coins and piggy banks for
    finance; crosses, pills and heartbeat lines for health.
- **Unverified as named logo clichés:** the lightbulb, rocket and brain. They appeared only in
  search snippets or stock listings, so the skill leaves them out of its logo lists. (The
  infinity symbol is now sourced by Fast Company, above.)

### Craft

- **Sagi Haviv's tests:** simple, appropriate, distinctive. A symbol "needs a good reason"
  (a long name, sub-brands, a need for shorthand); otherwise work on the name.
- **Shelf test:** search "[industry] logos" and avoid what you see (Vistaprint).
- **Small and plain:** works in one colour (Obsidian, Spotify) and at a 16px favicon (Inkbot).
- **Optical corrections** (Logo Geek):
  - round shapes overshoot by about 1–3 %;
  - white-on-dark versions look heavier, so thin them;
  - grids are "only a guide, and not a rule".
- **Icon geometry** (Lucide): one stroke, consistent joins and caps, gaps of at least 2 units on
  a 24-unit grid.

### SVG and favicons

- **Counters:** `fill-rule="evenodd"`, or an inner path wound the opposite way (MDN).
- **One colour:** `currentColor` takes the CSS `color` value (MDN).
- **No `<text>`:** a missing font is substituted and the spacing shifts, so outline the letters
  (zenind).
- **BIMI SVG Tiny P/S:**
  - `baseProfile="tiny-ps"`, a `<title>` of 64 characters or fewer;
  - square, no `x`/`y` on the root;
  - no scripts or external references, at most 32 KB (Valimail).
- **The favicon set** (Evil Martians):
  - `favicon.ico` at 32×32;
  - an `icon.svg` with a `prefers-color-scheme` style;
  - `apple-touch-icon.png` at 180×180 with padding and a background;
  - 192px and 512px PNGs plus a maskable 512px icon, with the logo inside a 409px safe zone.
- **Inference from kaankiziltug's skill:** a mark with hundreds of anchors is traced or
  over-detailed. Its example: 374 anchors against a median of 53.

## Fonts

- **Figma Community holds specimens, pairings and scales, not font files.**
  - Crafted ones:
    - Free Fonts in Editable Components (Tiptop Type): 100+ open-licence fonts in specimens you
      can type real copy into;
    - Usable Google Fonts (Smith & Diction): "Google has a billion typefaces. These are the ones
      that are actually usable.";
    - favorite free fonts — Feb 2026 (3 Sided Coin);
    - Carbon Type Sets (IBM);
    - Type Scale Worksheet (Headway).
  - Generic: the "100 Best Font Combinations" style listicles.
  - **Pairing files push the seeded fonts** *(visual check)*:
    - "Best Google Font Pairings for UI Design in 2025" (Matt Medley) files Fraunces / Inter
      under "Brand-Forward Expression", next to Playfair Display / Raleway and Bebas Neue /
      Heebo.
    - The cover of "A selection of Google Fonts" (Maxime, about 57k uses) leads with IBM Plex
      Sans and Source Serif.
  - **Tiptop Type's file, checked visually:** editable specimen cards in light and dark, with
    real-copy slots, for faces that aren't on Google Fonts. The tool is the useful part; its
    picks are not a list to adopt.
  - Licence red flags: shared Gilroy and SF Pro files, whose licences don't allow
    redistribution (from general knowledge, not checked in this pass).
- **Google Fonts popularity ranks** (from `fonts.google.com/metadata/fonts`, about 1,950
  families, approximate because of ties):

  | Font | Rank | Font | Rank |
  |---|---|---|---|
  | Manrope | 5 | Space Grotesk | 57 |
  | Outfit | 6 | Bricolage Grotesque | 64 |
  | JetBrains Mono | 8 | Instrument Serif | 84 |
  | DM Sans | 21 | Fraunces | 85 |
  | Playfair Display | 24 | Sora | 88 |
  | Plus Jakarta Sans | 37 | Geist | 96 |

- **Critiques that name fonts:**
  - Instrument Serif is "the default output of LLM-assisted and vibe-coded web work … Today it's
    everywhere" (Naz Hamid, May 2026). Keya Vadgama names it as part of AI brands'
    "serif-as-humanity signaling".
  - A published typography skill calls Fraunces "the indie-SaaS display serif" and says "'Clash
    Display + Satoshi body' is now a look, not a choice". It names the Fontshare starter pack
    (Satoshi, General Sans, Clash Display, Cabinet Grotesk, Switzer) and Söhne as the AI-company
    house sans.
  - Mono for "tech vibes" on text that isn't code (pixelslop).
  - Maxed variable axes, a heavy serif on every headline, and display faces under 24px
    (Laith0003).
- **Licences:**
  - **Fontshare (ITF FFL v2.0):** commercial use and self-hosting are allowed; modifying
    (including subsetting), redistributing and offering the font inside tools are not.
  - **Velvetyne:** asks for credit. Its post "Your next font choice is not on Velvetyne" pushes
    back on over-use of its own fonts.
  - **Collletttivo:** OFL.
  - **League of Moveable Type:** all OFL.
  - **uncut.wtf:** an index; check each source.
  - **Open Foundry:** includes Inter, Roboto and Poppins, and its page states no licence.
- **Indonesia and Southeast Asia:**
  - Tokotype: Plus Jakarta Sans (already on the ban list) and Mohave;
  - Lafontype: Gantari (OFL; that Lafontype is Indonesian comes from a third-party source);
  - Cadson Demak's families on Google Fonts; Be Vietnam Pro;
  - Noto for Javanese, Balinese, Sundanese, Buginese and Batak scripts;
  - Dafont and FontSpace "free" fonts are often personal-use demos.
- **Method and numbers** (Google Fonts Knowledge, WCAG 1.4.8, MDN):
  - the checklist: weights and true italics, languages, alternates, widths and optical sizes,
    spacing, licence;
  - measure 45–75 characters, at most 80;
  - line height 1.5 for body text under WCAG 1.4.8;
  - `font-variant-numeric: tabular-nums` for data; `font-optical-sizing: auto` is the default.
- **WIRED, "AI Has Come for Serif Fonts"** (John Semley, 5 June 2026). Its standfirst: AI
  companies are using serifs to project humanity, and critics call it "tasteslop". The body is
  paywalled and was not read.
- **Unverified:** Badass Libre Fonts by Womxn (the host's firewall blocks it, even from a regular
  browser) and Butterick's figures.

## Assets

- **Icons:**
  - The 24×24 / 2px / round-cap look dominates. Lucide is a Feather fork; Heroicons, Feather and
    Untitled UI Icons read as one family.
  - Figma uses: Untitled UI Icons about 380k, Heroicons about 150k across two files, Feather and
    Unicons 73k, Lucide 44k.
  - shadcn's December 2025 changelog: "all apps started looking the same… the defaults were a
    little too good". `shadcn create` now lets you choose the icon library, fonts and style.
  - iconbuddy's teardown of Linear's landing page: "icons are punctuation"; a feature grid of
    rocket, lightbulb and shield icons says "we didn't know what to write"; "show the feature,
    don't symbolize it".
  - Lucide's icon guide gives a usable spec: 24×24 with at least 1px padding, one centred stroke,
    round joins, a corner radius rule, and gaps of at least 2px.
  - Company-owned sets show the alternative: Octicons, Fluent System Icons.
- **Illustration:**
  - Corporate Memphis / "Alegria" (Buck for Facebook, 2017): critics call it "lazy" (Wired).
    Claire L. Evans says it makes Big Tech look "friendly, approachable", and Creative Bloq
    reported it in decline by 2023 from oversaturation.
  - unDraw sells "customize your main color on-the-fly", so the same art fits every brand.
  - Overused Figma files: Streamline's illustration packs (about 110k uses), Icons8 3D Business
    (about 47k), "Frosted Glass 3D", isometric workspace sets, AI-generated 3D sets.
  - **The top "illustrations" results** *(visual check)*:
    - Streamline's line people at laptops, and a "network of people" scene;
    - glossy 3D business people (Icons8);
    - "SVG Abstract Patterns" (about 102k uses): purple-pink gradient blobs and circles;
    - Stipple (about 34k): a group of people under a giant lightbulb;
    - three empty-state kits (15–45k uses each), all with the same pale blue blob behind an
      envelope, a magnifier or a card;
    - Notion-style line people.
- **Photography:**
  - Nielsen Norman Group eyetracking: "users ignore stock photos of generic people", and big
    decorative images get skipped. Real staff photos at FreshBooks drew about 10 % more viewing
    time than the bios, which took 316 % more space.
  - AI-image tells (weakly sourced; general detection guides): waxy skin, lettering that falls
    apart, light that doesn't match, repeated details, wrong grips.
  - **Unverified:** no source names the handshake or "pointing at a laptop" as clichés, so the
    skill doesn't list them.

## Layout systems

- **Content-out** (Mark Boulton via hidde.blog): "design content out, not canvas in". Find the
  fixed sizes in the content, derive a unit from them, and prefer odd column counts.
- **Grids:**
  - IBM Carbon 2x Grid: an 8px mini unit; 4, 8 or 16 columns; gutterless for related content;
    the aspect ratios 1:1, 2:1, 2:3, 3:2, 4:3, 16:9. Add columns for more items; keep the columns
    and enlarge the boxes for more detail.
  - The 8pt grid (spec.fm): a hard grid (containers snapped) vs a soft grid (spacing only), with
    a 4pt baseline for text.
  - Figma Community grid files are mostly "Responsive 12 columns" and "Bootstrap 5". The Macro
    Micro Framework (24 columns, a 4px unit) is the exception.
- **Spacing scales:**
  - Atlassian tokens: 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80.
  - Utopia: multipliers 0.25 to 6 on a fluid base, with "more options close to the origin, fewer
    further out".
- **Density:**
  - Primer control heights: 24/28/32/40/48px.
  - Material density works in 4px steps and suits lists and tables, not alerts or task flows.
  - shadcn now ships compact and generous styles.
- **Unsourced observation:** a centred 12-column container with identical section padding
  everywhere.

## Surfaces

- **Radius by role:**
  - Atlassian: 2px (badges), 4px (tags, tooltips), 6px (buttons, inputs), 8px (cards), 12px
    (modals, tables), 16px, full (avatars, pills).
  - Primer: 3/6/12px/full. Polaris: 2–30px. Material 3: 0–48dp/full.
  - **Unverified:** inner radius = outer − padding was seen only in search snippets, so the skill
    gives it as a rule of thumb.
- **Borders:**
  - Primer 1/2/4px; Atlassian 1px default and 2px for selected or focused; a Polaris hairline of
    0.66px.
  - Atlassian's border colour is translucent ink (`#0B120E24`), so one value works on every
    surface.
- **Elevation** (Atlassian):
  - flat cards get a border; "raised" is for movable cards; "overlay" is for things over other
    UI;
  - "don't use [raised] to group content when a border or white space would suffice";
  - in dark mode, higher surfaces are lighter.
- **Shadows:**
  - Josh Comeau: one light source, layered shadows, tinted to the background's hue; as elevation
    rises, offset and blur go up and opacity goes down.
  - Real systems tint with their own ink: Primer `#1f2328` at 3–24 %, Polaris
    `rgba(26,26,26,…)`, Atlassian `#1E1F21`. Atlassian's older theme used its navy `#091E42`,
    which is why the skill says to tint toward the palette's ink, not toward blue.
  - Atlassian's pattern: raised `0 1px 1px #1E1F2140, 0 0 1px #1E1F214F`; overlay
    `0 8px 12px #1E1F2126, 0 0 1px #1E1F214F`.
- **Focus:**
  - WCAG 2.4.13 (AAA): a perimeter of at least 2 CSS px, with 3:1 contrast between focused and
    unfocused.
  - Primer: an inset 2px outline. Atlassian: 2px, offset 2px, radius + 2px.

## Sources

First pass:

- Anthropic frontend-design skill: https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md
- Anthropic cookbook, prompting for frontend aesthetics: https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/coding/prompting_for_frontend_aesthetics.ipynb
- Anthropic blog, improving frontend design through skills: https://www.claude.com/blog/improving-frontend-design-through-skills
- Why your AI keeps building the same purple gradient website: https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website
- Vibe-coded websites look the same: https://codemyspec.com/blog/vibe-coded-websites-look-the-same
- Tailwind slate reference: https://designrevision.com/tools/tailwind-colors/slate
- pixelslop AI slop patterns: https://cdn.jsdelivr.net/npm/pixelslop@0.3.8/dist/skill/resources/ai-slop-patterns.md
- Anti-AI-slop ban list: https://raw.githubusercontent.com/wiki/Laith0003/ux-skill/Anti-AI-slop-ban-list.md
- impeccable.style, slop: https://impeccable.style/slop
- The AI purple problem: https://dev.to/jaainil/ai-purple-problem-make-your-ui-unmistakable-3ono
- Fix AI slop design: https://capitalandcompute.net/blog/fix-ai-slop-design/
- Signs of a vibe-coded UI: https://www.thefountaininstitute.com/blog/signs-vibe-coded-ui
- Overused AI design patterns: https://noqta.tn/en/blog/ai-design-slop-overused-ui-patterns-fix-2026
- Spot the slop: https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c
- Making a website not look AI-generated: https://21st.dev/blog/website-not-look-ai-generated
- Figma Community: https://www.figma.com/community/

Second and third passes:

- Direction:
  - https://alistapart.com/article/style-tiles-and-how-they-work
  - https://learningloop.io/plays/workshop-exercise/personality-sliders
  - https://styleguide.mailchimp.com/voice-and-tone/
  - https://playbook2.hike.one/methods/mapping/design-direction
- Logos:
  - https://www.fastcompany.com/90869029/ai-boom-logo-trend-swirling-hexagon
  - https://www.figma.com/community/file/1599596331443906590/waybill-brand-guidelines-template
  - https://www.figma.com/community/file/1340401409393638344/kokoro-branding-brand-identity-coffee-shop
  - Figma Community searches: "logo", "ai logo template", "brand guidelines"
  - https://velvetshark.com/ai-company-logos-that-look-like-buttholes
  - https://getcoai.com/news/techs-obsession-with-circular-logos-reveals-a-deeper-problem
  - https://braindetox.kr/en/posts/ai_logo_design_convergence_2026.html
  - https://www.nngroup.com/articles/ai-sparkles-icon-problem/
  - https://www.vistaprint.com/hub/generic-logos
  - https://www.designcrowd.com/help/article/generic-common-and-overused-logo-concepts-and-how-to-avoid-them
  - https://inkbotdesign.com/logo-testing
  - https://logogeek.uk/?p=2617
  - https://www.logodesignlove.com/sagi-haviv-interview
  - https://obsidian.md/brand
  - https://www.figma.com/using-the-figma-brand/
  - https://developer.spotify.com/documentation/design
  - https://github.com/kaankiziltug/logo-design-skill
- SVG and favicons:
  - https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-rule
  - https://developer.mozilla.org/en-US/docs/Web/CSS/color_value
  - https://www.zenind.com/help/post/why-fonts-break-in-svg-logos-and-how-to-fix-them
  - https://www.valimail.com/blog/bimi-compatible-logos/
  - https://evilmartians.com/chronicles/how-to-favicon-in-2021-six-files-that-fit-most-needs
- Fonts:
  - https://www.wired.com/story/ai-has-come-for-serif-fonts/ (headline and standfirst only)
  - https://www.figma.com/community/file/1540465222952841003/best-google-font-pairings-for-ui-design-in-2025
  - https://www.figma.com/community/file/1355230594764497559/free-fonts-in-editable-components
  - Figma Community search: "font pairing"
  - https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/coding/prompting_for_frontend_aesthetics.ipynb
  - https://nazhamid.com/journal/craft-is-not-culture
  - https://keyavadgama.substack.com/p/the-serif-renaissance-in-ai-branding
  - https://claudeskills.info/skills/curiositech/some_claude_skills/typography-expert/
  - https://fonts.google.com/metadata/fonts
  - https://fonts.google.com/knowledge/choosing_type/a_checklist_for_choosing_type
  - https://fonts.google.com/knowledge/choosing_type/pairing_typefaces
  - https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html
  - https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-numeric
  - https://www.fontshare.com/licenses/itf-ffl
  - https://velvetyne.alwaysdata.net/news/your-next-font-is-not-velvetyne/
  - https://www.collletttivo.it/licensing
  - https://uncut.wtf/
  - https://www.theleagueofmoveabletype.com/
  - https://luc.devroye.org/indonesia.html
  - https://www.figma.com/community/fonts-typography
- Assets:
  - Figma Community search: "illustrations"
  - https://ui.shadcn.com/docs/changelog/2025-12-shadcn-create
  - https://iconic.iconbuddy.com/p/iconic-07-how-linears-landing-page-uses-icons
  - https://lucide.dev/contribute/icon-design-guide
  - https://en.wikipedia.org/wiki/Corporate_Memphis
  - https://undraw.co/
  - https://www.nngroup.com/articles/photos-as-web-content/
- Layout:
  - https://carbondesignsystem.com/elements/2x-grid/overview/
  - https://spec.fm/specifics/8-pt-grid
  - https://utopia.fyi/blog/painting-with-a-fluid-space-palette
  - https://hidde.blog/mark-boultons-grid-system-design-workshop/
  - https://primer.style/foundations/primitives/size
- Surfaces:
  - https://atlassian.design/foundations/radius
  - https://atlassian.design/foundations/elevation
  - https://www.joshwcomeau.com/css/designing-shadows
  - https://cdn.jsdelivr.net/npm/@shopify/polaris-tokens/dist/css/styles.css
  - https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html
