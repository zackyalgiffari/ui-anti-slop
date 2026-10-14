# Step 6: Layout

Decides the grid, the spacing scale, density, the order and composition of what's on each screen,
and how it changes across widths. It takes the content itself, the Direction's principles and the
type scale, and hands surfaces a set of regions to separate.

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
3. **Choose the grid.** A 12-column centred container is a default, not a decision.
   - **Asymmetric splits** suit most content pages: 7+5, 8+4, 2+7+3, or a narrow index column
     beside a wide reading column.
   - **Odd column counts** (5, 7, 9) create tension; a modular grid suits catalogues; a single
     measured column suits reading.
   - **Ratios:** Carbon's 2x grid uses the aspect ratios 1:1, 2:1, 2:3, 3:2, 4:3 and 16:9 for
     boxes. When users want more items, add columns; when they want more detail per item, keep
     the columns and enlarge the boxes.
   - **Alignment:** pick left-aligned, centred or justified once, for a reason. Left-aligned is
     the norm for reading.
4. **Choose a spacing scale with more steps near the origin.** Not a linear 4-8-12-16…:
   - Atlassian: 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80;
   - Utopia: multipliers 0.25, 0.5, 0.75, 1, 1.5, 2, 3, 4, 6 on a fluid base, with
     `clamp()` between a mobile and a desktop size.

   Snap containers to the scale (a hard grid), or just the space between elements (a soft grid).
   Use a 4px baseline for text if the type scale allows. Related things sit closer than unrelated
   things. Not every section gets the same padding.
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
   - **unequal sizes for unequal importance:** not three identical cards because there happen to
     be three things;
   - **real hierarchy,** made from size, weight, position and space before colour;
   - **one memorable element** (the Signature) with everything else quiet.
7. **Plan the responsive behaviour,** don't just stack:
   - what reflows;
   - what collapses into a disclosure;
   - what changes order;
   - what gets its own mobile layout (tables often do);
   - touch targets of at least 24×24 CSS px (WCAG 2.5.8), and 44px for primary touch actions.
8. **Sketch it.** Put a small ASCII sketch of the layout in the brief, with the grid split and the
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
- **Grids:** a 12-column centred container with identical section padding everywhere; one density
  for every product.
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
- Do sizes reflect importance, or did things get equal boxes because they're equal in number?
- Does it hold at 320px, at a tablet width and at a wide desktop? No horizontal scroll?
- Is there one focal point per view?

Evidence: [research.md → Layout systems](research.md#layout-systems).
