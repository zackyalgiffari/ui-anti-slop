# Step 2: Colour

Decides 4–6 named colour tokens with roles, their tints and shades, a dark theme if one is
needed, and the status colours. It takes the Direction's material nouns and reference, and hands
named tokens to type, logo, assets and surfaces.

## Method

1. **Sample, don't invent.** For each material noun, find its real colour: from a photograph of
   the thing if you have one (eyedrop it), otherwise from what the object actually looks like.
   - Indigo vat water is not `#4F46E5`.
   - Dried wax is not `#FFFFFF`.
   - Name each token after its source: `vat`, `wax`, `rack`, `copper`; not `primary-500`.
2. **Give every token a role:**

   | Role | Job |
   |---|---|
   | ground | the page |
   | surface | raised or grouped areas, if different from the ground |
   | ink | body text and icons |
   | primary | the main action, one per view |
   | accent | a budgeted highlight |
   | signal | status: success, warning, danger, info |

   Not every role needs its own hue; ink and primary can share one.
3. **Choose a dominant colour and budget the accent.** One colour owns most of the area (often the
   ground or a large brand field). The accent gets a budget, e.g. "one element per viewport" or
   "under 5 % of the area". A palette spread evenly across five hues reads as timid and generic.
4. **Tint the neutrals toward the brand hue, not toward blue.** Greys with a little of the
   dominant hue (OKLCH chroma around 0.005–0.02) feel related; Tailwind `gray` and `slate` are
   tinted blue. Check the hue of every neutral you write.
5. **Build ramps in OKLCH.** Keep the hue, step the lightness evenly, and lower the chroma toward
   the very light and very dark ends, where high chroma clips or looks garish:
   `oklch(96% 0.02 60)` … `oklch(28% 0.05 60)`. Generate only the steps you use.
6. **Check contrast as you go** (WCAG 2.2):
   - body text ≥ 4.5:1;
   - large text (24px+, or 18.66px+ bold) ≥ 3:1;
   - UI component edges and focus indicators ≥ 3:1 against what's next to them (1.4.11).
7. **Make the dark theme from the subject, if one is wanted.**
   - Choose a dark that exists in the material world: forest, oxblood, umber, olive, aubergine,
     soot, or graphite with zero blue. Not navy.
   - Don't invert. Lift surfaces as they rise (higher = lighter, Atlassian), lower the chroma of
     bright accents, and avoid pure `#000` grounds and pure `#FFF` body text.
   - A different dark for each project.
8. **Tune the status colours to the palette.** Shift success, warning and danger toward hues and
   chroma that sit with the brand, then check contrast.
   - Don't ship stock emerald/amber/rose.
   - Never use colour alone for meaning (WCAG 1.4.1): pair it with an icon, text or shape.
9. **Chart colours**, if there are charts: derive categorical colours from the palette, keep them
   distinguishable for colour-blind readers, and use a single-hue ramp for sequential data.
10. **Write the token table** into the brief:

```
token     hex       role              on wax   source in the subject
wax       #EFE8D8   ground            —        dried resist wax on cambric
soot      #2A2420   ink               12.5:1   the canting's blackened copper tip
soga      #8A4B22   primary           5.5:1    soga-brown bark dye
vat       #3D5E86   accent (≤1/view)  5.5:1    indigo-dyed cloth, used small
rack      #6F7A3A   success           3.8:1    bamboo drying rack (icons, large text only)
```

That table is a worked example for one fictional subject (a Pekalongan batik workshop). It shows
the method, not values to reuse. A different subject must produce a different table.

## Slop to avoid

- **Navy and blue-slate** as page, surface, sidebar, card, hero or dark-mode colour: hue about
  200–260°, lightness under about 25 %, any saturation.
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
- **Pure black or grey shadows** on a coloured ground; see [surfaces.md](surfaces.md).

A brief that names one of these colours, or an established brand that uses one, wins. A brand
whose real colour is indigo dye keeps it, used as an accent with its budget, not as a navy
ground.

## Checks

- **Greyscale test:** convert a screenshot to greyscale. Do hierarchy and the primary action
  still read?
- **Hue check:** read the hue of every neutral. Is any of them drifting blue without the brand
  being blue?
- **Contrast:** run every text/ground pair you actually use.
- **Swap test:** would this table fit a competitor? If yes, go back to the material list.

Evidence: [research.md → Colour](research.md#colour),
[the second wave](research.md#the-second-wave).
