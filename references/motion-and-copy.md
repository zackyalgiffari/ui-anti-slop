# Step 8: Motion and copy

Decides what moves, when and how, and what every piece of text says. It takes the Direction (the
adjectives and the voice), the layout and the real content, and finishes the design.

## Motion

### Method

1. **Give motion a job.** Motion that answers a user action (opening, moving, confirming,
   loading), or one orchestrated moment that shows the product, is worth having. Motion on every
   section is not.
2. **Pick the moments,** at most a few per screen:
   - state changes: opening, closing, expanding;
   - feedback: press, saved, error;
   - spatial continuity: where something came from, where it went;
   - one signature moment, if the Direction asks for one.
3. **Set durations and easing by role.** The intensity sets how much moves
   ([comfort.md → Intensity](comfort.md#intensity)): at Calm, only feedback and state changes.

   | Role | Duration | Easing |
   |---|---|---|
   | micro-feedback (press, toggle) | 80–150ms | ease-out |
   | small UI (menus, tooltips) | 150–250ms | enter with ease-out, exit faster with ease-in |
   | large moves (panels, page sections) | 250–400ms | |

   Name the curves as tokens. The adjectives can tune them: "precise, not clinical" wants short,
   firm curves; "playful, not childish" can take a small overshoot on one element.
   - Exits run about 75 % of the entrance time.
   - Things travel 8–16px, not 40px. No bounce on UI.
   - Actions people repeat all day (typing, toggles, list navigation, menus opened by keyboard)
     don't animate at all.
4. **Animate `transform` and `opacity`, not layout properties.** List the properties being
   transitioned; never use `transition: all`.
5. **Respect `prefers-reduced-motion: reduce`.** Fewer and gentler, not zero: replace movement
   with an instant change or a short fade, and stop autoplaying loops.
6. **Nothing that loops forever for decoration:** no pulsing dots, floating blobs or shimmer on
   static content.

### Slop to avoid

- **Fade-and-slide-up on every section** as it scrolls into view.
- **`hover:scale` on every card,** `transition-all`, pulsing "live" dots that mean nothing.
- **Effects:** parallax blobs, cursor-follow glows, spotlight gradients.
- **Typewriter or gradient-shimmer headlines.**

## Copy

### Method

1. **Write with the real content.** Real product names, real numbers, real places, real people
   (with permission). If content is missing, ask for it or mark it plainly as a placeholder
   ("[client quote]"). Don't invent stats or testimonials.
2. **Write the voice from the Direction's adjectives,** with "X, not Y" (Mailchimp): "plain, not
   blunt", "warm, not chummy".
3. **Headlines say what the thing is or does, for whom,** in the user's words. A headline that
   could sit on any product's page says nothing.
4. **Buttons say what happens:** "Book the 07:40 ferry", "Download the invoice (PDF)", "Pesan
   kain". Not "Get Started" or "Learn More" repeated.
5. **Use sentence case for headings and buttons** unless the brand has a rule. Don't let a
   heading repeat its own subtext.
6. **Write labels, errors and empty states as instructions:** what happened, and what to do next.
7. **For bilingual products,** write each language natively; don't translate the slop. Indonesian
   UI copy can be short and direct ("Simpan", "Kirim ulang kode").

### Slop to avoid

- **Verbs:** Unlock, Elevate, Empower, Transform, Supercharge, Revolutionize, Streamline,
  Harness.
- **Phrases:** "seamless", "all-in-one platform", "the future of X", "feels like magic", "at
  scale", "built for teams of all sizes", "your all-in-one solution", "take X to the next level".
- **In Indonesian:** "Tingkatkan produktivitas", "Solusi all-in-one", "Revolusi …",
  "Wujudkan …", "Era baru …", "Satu platform untuk semua kebutuhan".
- **Fake data:** invented round stats (10,000+, 99.9 %, 4.9★), "John Doe" or "Jane Smith"
  testimonials, "Acme" or "Lorem Corp" placeholders, stock logo rows of companies that aren't
  customers.
- **Repeated CTAs:** "Get Started" or "Learn More" three or more times; CTAs that don't say what
  happens.
- **Headings** that are a slogan with no information.

## Checks

- Turn off motion (`prefers-reduced-motion`). Does everything still work and make sense?
- Can you name the job of every animation?
- Read the copy aloud. Could a competitor use it unchanged? Is every number real?
- Does every button say what it does?

Evidence: [research.md → Catalogue of tells](research.md#catalogue-of-tells).
