# Step 2: Colour

Decides 4–6 named colour tokens plus the status colours, with roles, their tints and shades, a dark theme if one is
needed, and the status colours. It takes the Direction's material nouns, reference and intensity,
and hands named tokens to type, logo, assets and surfaces. The lightness and chroma limits come
from the [comfort floor](comfort.md#colour).

## Method

1. **Sample the hue from the material; set lightness and chroma by role.** For each material
   noun, find its real colour: from a photograph of the thing if you have one (eyedrop it),
   otherwise from what the object actually looks like.
   - Indigo vat water is not `#4F46E5`.
   - Dried wax is not `#FFFFFF`.
   - Name each token after its source: `vat`, `wax`, `rack`, `copper`; not `primary-500`.
   - The sample gives the *hue*. The role decides how light and how saturated the token is: a
     sampled oxblood becomes a near-neutral ground tinted toward oxblood, or a small accent at
     full strength, never an oxblood page.
2. **Give every token a role,** inside the comfort bands (OKLCH, light theme):

   | Role | Job | Lightness | Chroma |
   |---|---|---|---|
   | ground | the page | 0.96–1.00 | ≤ 0.015 |
   | surface | raised or grouped areas, if different from the ground | ground ± 0.02–0.06 | ≤ 0.02 |
   | ink | body text and icons | 0.18–0.35 | ≤ 0.03 |
   | muted | secondary text | ≥ 4.5:1 on the ground | low |
   | primary | the main action, one per view | ≥ 3:1 on the ground | moderate |
   | accent | a budgeted highlight | ≥ 3:1 on the ground | 0.07–0.20 |
   | signal | status: success, warning, danger, info | ≥ 3:1 on the ground | moderate |

   Not every role needs its own hue; ink and primary can share one.
3. **Keep the palette small and budget the accent.** 2–3 core colours + 1 accent; neutrals and
   status colours don't count. The dominant colour owns most of the area *as a low-chroma tint*
   (the ground or the surfaces); its full-strength version is a signature item. The accent gets a
   budget: "one element per viewport" or "under 5 % of the area", used for action, focus and
   selection, not headings or decoration.
4. **Tint the neutrals toward the brand hue, not toward blue.** Greys with a little of the
   dominant hue (OKLCH chroma around 0.005–0.015) feel related; Tailwind `gray` and `slate` are
   tinted blue. Check the hue of every neutral you write.
5. **Build ramps in OKLCH.** Keep the hue, step the lightness evenly, and lower the chroma toward
   the very light and very dark ends, where high chroma clips or looks garish:
   `oklch(97% 0.01 60)` … `oklch(26% 0.02 60)`. Generate only the steps you use.
6. **Check contrast as you go:**
   - body text ≥ 7:1 and APCA Lc 75+ (90 preferred); WCAG's 4.5:1 is the floor, not the target;
   - secondary text ≥ 4.5:1 (Lc 60), by colour, not by opacity; at most three text colours;
   - large text (24px+, or 18.66px+ bold) ≥ 3:1;
   - UI component edges and focus indicators ≥ 3:1 against what's next to them (1.4.11).
7. **Avoid vibrating pairs.** Two saturated hues (C > 0.12) of opposite temperature at similar
   lightness shimmer when they touch, and more so on dark grounds. Don't put them side by side or
   one as text on the other; separate them with a neutral, or calm one of them.
8. **Make the dark theme from the subject, if one is wanted.** Light is the default; dark is for
   subjects used at night or in the dark (media, terminals, night shifts) or when the brief asks.
   - A near-neutral dark tinted toward something in the material world: forest, oxblood, umber,
     olive, aubergine, soot, or graphite with zero blue. Not navy. OKLCH L 0.15–0.24, C ≤ 0.02:
     "forest" means a hint of green, not a green page.
   - Don't invert. Lift surfaces as they rise (L +0.03–0.05 per step), lighten and calm the
     accents (L ≥ 0.70, C ≤ 0.14), and avoid pure `#000` grounds and pure `#FFF` text (body text
     L 0.88–0.94).
   - A different dark for each project.
9. **Keep status colours in their families.** Success stays green, warning amber, danger red,
   info blue, because people already read them that way. Tune only their lightness and chroma to
   sit with the palette, then check contrast.
   - Don't ship stock emerald/amber/rose.
   - Never use colour alone for meaning (WCAG 1.4.1): pair it with an icon, text or shape.
10. **Chart colours**, if there are charts: derive categorical colours from the palette, keep them
    distinguishable for colour-blind readers, and use a single-hue ramp for sequential data.
11. **Run the palette check** on the tokens, both themes:

    ```
    python3 scripts/palette-check.py 'ground:wax=#F8F7F3' 'ink:soot=#2A2420' …
    ```

    The path is relative to this skill's folder (installed:
    `~/.claude/skills/ui-anti-slop/scripts/palette-check.py`). Quote the tokens if your shell
    treats `#` specially. It prints each token's OKLCH, its contrast ratio and APCA Lc on the
    ground (both rounded down), and the findings.
    Fix every FAIL; fix each WARN or say why the brief needs it.
12. **Write the token table** into the brief:

```
token     hex       role               on ground  OKLCH L/C/h        source in the subject
wax       #F8F7F3   ground             —          0.976 0.005  95    dried resist wax, as a faint tint
cambric   #FFFFFF   surface            1.07:1     1.000 0.000   —    bleached cotton cambric
soot      #2A2420   ink                14.28:1    0.266 0.012  56    the canting's blackened copper tip
ash       #6B635B   muted              5.50:1     0.505 0.016  67    wood ash from the dye-house stove
soga      #8A4B22   primary            6.29:1     0.481 0.101  51    soga-brown bark dye
vat       #3D5E86   accent (≤1/view)   6.23:1     0.475 0.076 254    indigo-dyed cloth, used small
leaf      #467748   success            4.90:1     0.521 0.090 145    indigo-plant leaves

soot      #1C1612   dark ground        —          0.206 0.012  56    soot, as a near-neutral dark
wax       #E4E1DB   dark ink           13.71:1    0.910 0.009  85
vat       #84AFDC   dark accent        7.79:1     0.740 0.080 250    vat, lightened and calmed
```

That table is a worked example for one fictional subject (a Pekalongan batik workshop), and it
passes the palette check in both themes. It shows the method, not values to reuse. A different
subject must produce a different table.

## Slop to avoid

- **Navy and blue-slate** as page, surface, sidebar, card, hero or dark-mode colour: hue about
  200–260° (HSL), lightness under about 25 %, any saturation.
  - `#0F172A` `#020617` `#1E293B` `#0B1120` `#111827` `#1F2937` `#0D1117`
  - Tailwind `slate`/`gray` 800–950; `blue`/`indigo`/`sky`-950 surfaces; shadcn's "slate" base.
- **Navy's light twin:** blue-tinted grey pages (`#F8FAFC` `#F1F5F9` `#F5F6FA`, `slate-50/100`,
  `gray-50`).
- **The combos:** navy + gold "premium"; navy + electric blue or cyan glow; navy + indigo
  gradient.
- **Indigo and violet primaries** (`#6366F1` `#4F46E5` `#7C3AED` `#8B5CF6` `#5E6AD2`),
  purple→blue or violet→cyan gradients (`#667EEA`→`#764BA2`), neon glows on dark, gradient text.
- **Tailwind or shadcn palettes used as shipped:** a `blue-500` primary; stock emerald, rose and
  amber statuses.
- **Rainbow icon chips:** every card or KPI gets its own coloured rounded square.
- **The second wave**, where models go once told "no purple". Fine when the brief calls for it,
  never as the fallback:
  - cream (`#F4F1EA`) + high-contrast serif + terracotta (`#D97757`);
  - near-black (`#0B0B0B`, `#111`) + one acid-green or vermilion accent.
- **Forced colour:** a material colour sampled at full strength and used as the page; a beige or
  muddy ground (L under 0.96, C over 0.015, or a warm hue 60–100° at C 0.008 or more); status colours moved out of their hue family; two
  saturated hues vibrating side by side; more than one saturated hue per view.
- **Pure black or grey shadows** on a coloured ground; see [surfaces.md](surfaces.md).

A brief that names one of these colours, or an established brand that uses one, wins. A brand
whose real colour is indigo dye keeps it, used as an accent with its budget, not as a navy
ground.

## Checks

- **Palette check:** `scripts/palette-check.py` has no FAIL, and every WARN is fixed or explained.
- **Greyscale test:** convert a screenshot to greyscale. Do hierarchy and the primary action
  still read?
- **Hue check:** read the hue of every neutral. Is any of them drifting blue without the brand
  being blue?
- **Large areas:** is anything bigger than a quarter of the viewport above C 0.02, apart from the
  one signature field?
- **Swap test:** would this table fit a competitor? If yes, go back to the material list.

Evidence: [research.md → Colour](research.md#colour),
[the second wave](research.md#the-second-wave), [Comfort](research.md#comfort).
