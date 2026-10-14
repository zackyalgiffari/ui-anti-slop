# Step 7: Surfaces (border, radius, shadow, elevation, focus)

Decides how regions and components are separated and how they sit in depth. That covers:
- the radius scale;
- the border widths and colours;
- when to use a border, a fill or a shadow;
- the shadow recipe;
- the elevation levels in light and dark;
- the focus ring.

It takes the colour tokens (shadows and borders are tinted from them), the density and the
Direction, and hands components their finish.

## Method

1. **Write a radius scale by role,** not one radius for everything. The scale's character comes
   from the Direction: a technical or civic subject may want 0–4px; a soft consumer subject,
   larger radii. Most screens need 3–5 steps. Atlassian's scale shows the idea:

   | Token | Value | Use |
   |---|---|---|
   | xs | 2px | badges, checkboxes |
   | s | 4px | tags, tooltips, compact buttons |
   | m | 6px | buttons, inputs, nav items |
   | l | 8px | cards, menus |
   | xl | 12px | dialogs, tables, panels |
   | full | 999px | avatars, and only the pills that are really pills |

   Primer (3/6/12px/full), Polaris (2–30px) and Material 3 (0–48dp) differ, and that's the
   point: choose the steps for this subject.
   - **Nested corners:** a rounded element inside a rounded container uses inner radius = outer
     radius − the padding between them, so the curves stay concentric. This is a rule of thumb.
     Equal radii on parent and child look wrong.
2. **Set a border policy:**
   - **1px default;** 2px for selected and focused states; an optional hairline (about 0.5–0.66px,
     or 1px at a low alpha) for dense tables.
   - **Colour:** a translucent tint of the ink (e.g. the ink colour at 12–20 % alpha), so one
     token works on every surface.
3. **Choose one separation method per relationship**, in this order of preference:
   1. **Space:** group by proximity first; often nothing else is needed.
   2. **A fill:** a slightly different surface for a region.
   3. **A border:** for flat cards on the page, inputs, and sticky headers over scrolled content.
   4. **A shadow (raised):** only for things that move or float, such as draggable cards, menus,
      popovers and dialogs.

   Don't put a border, a fill and a shadow on the same card. Don't use a shadow to group content
   when a border or space would do (Atlassian).
4. **Write the shadow recipe:**
   - **One light source for the whole UI:** the vertical offset is about 2× the horizontal, or
     purely vertical.
   - **Layer 2–5 shadows per level;** as elevation rises, offset and blur grow and opacity drops
     (Josh Comeau).
   - **Tint the shadow with the palette's own ink**, never pure black, and never toward blue unless
     the brand is blue. Real systems tint with their ink (Primer, Polaris, Atlassian). A
     two-layer pattern, with `--ink-rgb` set to the ink colour's RGB:

   ```css
   --shadow-raised:  0 1px 1px rgb(var(--ink-rgb) / .25), 0 0 1px rgb(var(--ink-rgb) / .31);
   --shadow-overlay: 0 8px 12px rgb(var(--ink-rgb) / .15), 0 0 1px rgb(var(--ink-rgb) / .31);
   ```

   The second layer works as a hairline edge.
5. **Define the elevation levels:** usually flat, raised and overlay, plus a scrim behind
   dialogs. In dark mode, shadows almost disappear, so elevation comes from lighter surfaces:
   higher means lighter. A dark overlay may add a faint light ring (`0 0 0 1px` at about 12 %
   alpha of a light neutral).
6. **Design the focus ring.** It's part of the look, not an afterthought.
   - **WCAG 2.4.13:** at least a 2 CSS px perimeter with 3:1 contrast between the focused and
     unfocused states. At AA, 2.4.7 requires focus to be visible and 1.4.11 requires 3:1
     contrast.
   - **Shape:** a 2px outline offset by 2px, with radius = the element's radius + 2px so it stays
     concentric, or an inset 2px ring for dense controls.
   - **Trigger:** use `:focus-visible`. Never `outline: none` without a replacement.
7. **Write the surface tokens into the brief:** the radius scale with roles, border widths and
   colour, the separation rule, the shadow levels and the focus ring.

## Slop to avoid

- **The SaaS card kit:**
  - everything boxed in identical `rounded-2xl` cards with one radius;
  - `shadow-lg` everywhere;
  - nested cards (cards inside cards);
  - cards with a thick coloured left border, called "the single most recognisable signature".
- **Pure-black shadows:** `rgba(0,0,0,.1)` grey shadows on a coloured ground; shadows with no
  common light source.
- **Glow effects:** glow shadows such as `0 0 80px rgba(120,80,200,.6)`; neon outlines.
- **Glassmorphism:** `backdrop-blur` panels over blurred blobs.
- **Stacked separation:** border + fill + shadow on the same element.
- **Radius mistakes:** the same radius on a parent and its child; pill-shaped everything.
- **Dark mode:** light-mode shadows reused in dark mode, where they vanish.
- **Focus:** square focus rings on rounded controls; `outline: none` with nothing in its place.
- **Motion on surfaces:** `transition-all` and `hover:scale` on every card.

## Checks

- Can you name the role of every radius value in use? Fewer than 6 distinct values?
- Is anything separated by more than one method at once?
- Do the shadows share one light source, and are they tinted from the ink?
- Tab through the page: is focus always visible, concentric and 3:1?
- In dark mode, does elevation still read?

Evidence: [research.md → Surfaces](research.md#surfaces).
