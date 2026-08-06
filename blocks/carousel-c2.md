# Carousel C2

> **Quick summary:** A full-width, swipeable (drag, arrow keys, or Previous/Next buttons) hero-style slide carousel with a parallax "spread" effect between slides — use it for a rotating showcase rather than a simple content-grid carousel. Unusually, slide content isn't authored inside the block — the block itself is just one row/two cells (carousel name, aria-label), and each slide is its own page section tagged with a Section Metadata `carousel` row matching that name. No author-facing variations. Gotcha: matching is by exact text, so a typo in the carousel name silently drops that slide instead of erroring — see [section-metadata.md](./section-metadata.md).

## Authoring instructions

**Step 1 — the block:** Author a "Carousel C2" block with **exactly one row, two columns**. This row is never displayed; it only names the carousel and supplies its accessible label. The block only reads this first row — the first cell becomes the carousel's internal name, the second becomes its accessible label.

| Row / Column (in the Carousel C2 block) | Content |
|---|---|
| Column 1 — Carousel name | A short identifier, e.g. `product-launch`. Not shown to visitors — it's only used to match slides to this carousel (see Step 2). Must be unique per page/fragment if you have more than one carousel. |
| Column 2 — Accessible label | The text screen readers announce for the whole carousel, e.g. "Product launch highlights, carousel." |

**Step 2 — the slides:** Create a new page **section** for each slide (use your authoring tool's section break). In each slide section, add a **[Section Metadata](./section-metadata.md)** block with a row `carousel` → `<carousel name>`, matching Column 1 above exactly. The rest of that section's content (image/background, and optionally a [Rich Content](./rich-content.md) block for text overlay) becomes the slide.

| Section Metadata row | Content |
|---|---|
| `carousel` | The same carousel name you used in Step 1, e.g. `product-launch`. |

Slides are collected in the order their sections appear on the page/fragment — there is no separate ordering field.

## Variations

This block has no author-facing modifier classes. All visual behavior (RTL mirroring, reduced-motion, animation) is automatic based on page language and OS settings.

## Example

```
| Carousel C2                    |
| ------------------------------ |
| product-launch | Product launch highlights, carousel. |
```

Then, elsewhere on the same page, as separate sections:

```
[Section break]
![New laptop on a desk](/slide-1.jpg)

| Section Metadata |
| ----------------- |
| carousel | product-launch |

[Section break]
| Rich Content |
| ------------- |
| ## Meet the new lineup                              |
| Faster, lighter, and built for creators. [Learn more](https://www.adobe.com/new-lineup.html) |

![Designer working outdoors with the new laptop](/slide-2.jpg)

| Section Metadata |
| ----------------- |
| carousel | product-launch |
```

## Notes

- The **first slide you author becomes the initially active/visible slide**. Behind the scenes the carousel repositions slides for the infinite-loop peek effect (so the last slide appears to sit just before the first), but whichever slide you authored first is always what visitors see active on load.
- Every section you want in the carousel needs its own Section Metadata `carousel` row with the matching name — a slide's section without this row will just render as a normal standalone page section and won't join the carousel.
- Because matching happens by exact text match on the carousel name, typos (extra spaces, different casing) will silently drop a slide from the carousel instead of erroring.
- Buttons, indicators, and the live-region announcement ("Slide 2 of 5, …") are all generated automatically — do not author them.
- RTL languages automatically reverse slide order and mirror the arrows; no extra authoring needed.
