# Step 6: Layout

Decides the grid, the spacing scale, density, the order and composition of what's on each screen,
and how it changes across widths. It takes the content itself, the Direction's principles and
intensity, and the type scale, and hands surfaces a set of regions to separate. The alignment,
spacing and placement limits come from the [comfort floor](comfort.md#layout).

## Method

1. **Start from the content, not from a page template.** "Design content out, not canvas in"
   (Mark Boulton).
   - List what this screen must show, in order of importance, using the real content: the
     timetable, the product photos, the form, the table.
   - The first thing on the screen is the most characteristic thing of the subject: its product,
     its photo, a live demo, its real data. Not a slogan over a gradient.
2. **Find the fixed sizes in that content:** image aspect ratios, the text measure (60–70ch), a
   table's natural width, a video's frame, the minimum width of a form field. Derive the grid
   from them, and keep their ratios.
3. **Choose the grid from the content.** A regular grid is the calm default; what matters is
   that it fits this content, not that it looks unusual.
   - **Regular columns** (4, 8 or 12, or a single measured column for reading) suit most screens.
     Uniform rhythm is a legitimate choice, especially in apps and dashboards.
   - **Asymmetric splits** (8+4, a narrow index beside a wide reading column) only where the
     content's parts really are unequal. Never asymmetry for "tension".
   - **A modular grid** suits catalogues and galleries.
   - **Ratios:** Carbon's 2x grid uses the aspect ratios 1:1, 2:1, 2:3, 3:2, 4:3 and 16:9 for
     boxes. When users want more items, add columns; when they want more detail per item, keep
     the columns and enlarge the boxes.
   - **Alignment edges:** each view lines up on at most 3–4 vertical edges, and body text keeps
     one left edge. Left-aligned is the norm for reading; centre only short single items.
4. **Choose a spacing scale with more steps near the origin.** Not a linear 4-8-12-16…:
   - Atlassian: 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80;
   - Utopia: multipliers 0.25, 0.5, 0.75, 1, 1.5, 2, 3, 4, 6 on a fluid base, with
     `clamp()` between a mobile and a desktop size.

   Snap containers to the scale (a hard grid), or just the space between elements (a soft grid).
   Use a 4px baseline for text if the type scale allows.
   - **Use 4–6 values per screen,** not the whole scale.
   - **Proximity:** space between groups is at least twice the space within a group; space above
     a heading is 1.5–2× the space below it.
   - **Rhythm:** one section rhythm per page type. At Calm, sections share their padding; vary it
     only where the content changes in kind.
5. **Set the density for the product:**

   | Product | Control height | Spacing |
   |---|---|---|
   | data, developer and admin tools | 28–32px | tight |
   | general apps | 36–40px | medium |
   | consumer and marketing | 40–48px | generous, more air between sections |

   Dense tables and lists benefit from compact density; alerts, task flows and forms for first-time
   users don't. Primer's sizes (24/28/32/40/48) and Material's 4px density steps are references.
6. **Compose each screen:**
   - **one focal point per view;**
   - **sizes that follow importance:** unequal things get unequal sizes; equal things (a list of
     products, a set of plans) get equal treatment, and that's calm, not slop;
   - **real hierarchy,** made from size, weight, position and space before colour;
   - **familiar placements:** logo top left, navigation along the top or left, search at the top,
     primary actions where the platform puts them (Jakob's law). A novel placement only as the
     signature;
   - **one signature element** with everything else quiet, and generous white space around it.
7. **Make app and dashboard content honest:**
   - a chart's title is the question it answers ("Which batches are late this week?");
   - table columns come from the decisions the user makes, not Name/Status/Date/Actions by habit;
   - empty and loading states say what happened and what to do next;
   - placeholders are real examples or plainly marked, never filler data.
8. **Plan the responsive behaviour,** don't just stack:
   - **three states,** not two: phone, a designed middle band (about 600–1024px) and wide;
     breakpoints where the content breaks, not at device widths;
   - what reflows, what collapses into a disclosure, what changes order, and what gets its own
     mobile layout (tables often do);
   - `min-width: 0` on grid and flex children, `minmax()` and `auto-fit` for repeating items, and
     no horizontal scroll at 320px;
   - full-height sections in `dvh`, not `100vh`; section padding on phones about half of desktop;
   - a compact sticky header that doesn't eat the screen; a labelled "Menu", not a bare icon;
   - space reserved for fixed bottom bars, with `env(safe-area-inset-*)` and `scroll-padding`;
   - the on-screen keyboard never covers the focused input;
   - touch targets of at least 24×24 CSS px (WCAG 2.5.8), 44px for primary touch actions, with
     gaps between them; every hover effect has a tap equivalent.
9. **Sketch it.** Put a small ASCII sketch of the layout in the brief, with the grid split and the
   focal point marked.

## Slop to avoid

- **The stock landing page,** in this order:
  - a centred hero with a "✨ New" pill and two buttons;
  - a logo row;
  - three identical feature cards with an icon in a circle;
  - a testimonial grid;
  - pricing with "Most popular";
  - a CTA band.
- **The stock dashboard:** a dark sidebar, four KPI cards with icon chips and "+12.5% ↑" badges,
  a line chart, then a table.
- **The giant centred hero headline by default;** a hero metric (big number, small label,
  gradient accent).
- **Section kits by habit:**
  - a bento grid as the default section layout;
  - a fake terminal window with traffic-light dots;
  - a pill above the headline that repeats what the headline says;
  - "How it works" in exactly three steps, three pricing tiers, a four-column
    Product/Company/Resources/Legal footer, whatever the content;
  - alternating background colours as the only difference between sections;
  - skeleton blocks or a blurred mock standing in for the product.
- **Grids:** a 12-column centred container used without looking at the content; one density for
  every product.
- **Forced layout:** asymmetry or odd column counts chosen for "tension"; more than 3–4 alignment
  edges in a view; every section a different layout; navigation or primary actions moved to
  unexpected places for novelty.
- **Trend-stacking:** glass, glow, mesh gradients, mono labels, grid backgrounds and big radii on
  one page.
- **Template chrome:**
  - 01/02/03 markers on things that aren't a sequence;
  - "A · B · C" meta strings;
  - "→" on every link;
  - monospace micro-labels;
  - a tracked ALL-CAPS eyebrow above every section.
- **Broadsheet layouts with hairline rules and zero radius** as the "not-slop" fallback.

## Checks

- Cover the logo: could this layout belong to a different product? If yes, the content isn't
  leading.
- Is the first thing on the screen specific to this subject?
- Do sizes reflect importance?
- How many vertical alignment edges and spacing values does each view use? At most 3–4 and 4–6?
- Are the logo, navigation, search and primary actions where a user would look for them?
- Does it hold at 320px, in the middle band and at a wide desktop? No horizontal scroll?
- Is there one focal point per view? Blur the screenshot: does exactly one thing pop?

Evidence: [research.md → Layout systems](research.md#layout-systems).
