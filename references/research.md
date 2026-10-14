# Research: what makes a UI read as AI-generated

Compiled 2026-10-14. Two inputs: a browse of Figma Community (landing-page, SaaS and Figma Make
galleries) and the published critiques listed under Sources. Every source below was opened, not
just seen in search results.

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
  - Use one distinctive family, used decisively with real weight contrast, or two clearly
    distinct ones.
  - Examples given: IBM Plex, Bricolage Grotesque, Newsreader, Crimson Pro, Fraunces,
    Source Serif.
  - Treat any example list as a starting point, not a new default.
- **Layout.**
  - Open with the most characteristic thing of the subject.
  - Use left-aligned or uneven splits (7+5, 8+4) and real product screenshots.
  - Vary radius by role: inputs 4–6px, cards 8–16px.
- **Motion.** One orchestrated moment, or motion that answers a user action.
- **Restraint.** Remove one element that doesn't serve the brief before shipping.

## Sources

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
