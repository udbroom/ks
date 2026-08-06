# Hub Hero

> **Quick summary:** A large scroll-driven hero with a fading header, a 5-column parallax image grid, and a horizontal carousel of exactly 4 slides. Authored as a strict, fixed sequence of 8 rows (header, 2 image-grid rows, carousel header, 4 slide rows). Variations are text-sizing modifier classes: `heading-<1–6>`, `body-<sm|md|lg|xl>`, `button-<sm|md|lg|xl>`. Important gotcha: content is located by row position, not markers, so adding/removing/reordering rows (or using anything other than exactly 4 carousel slides) breaks the layout.

---

A large scroll-driven landing hero: a header (eyebrow/heading/body/CTA) that fades as you scroll, a 5-column parallax image grid, and a horizontal carousel of exactly 4 large slides that appear to "rise" out of the image grid as you scroll further. Use it as the top-of-page hero for hub/landing pages that want a cinematic, scroll-linked reveal instead of a static hero.

## Authoring instructions

This block has a **strict row order** — it expects exactly 8 rows, in this exact sequence. Getting the row count or order wrong will break the scroll math and column mapping.

| Row | Content |
|---|---|
| 1 — Header | One cell containing (in order): an optional eyebrow line, a heading (`h1`–`h6`), body paragraph(s), and a CTA paragraph with an inline icon image + link, e.g. `![icon](https://www.adobe.com/federal/assets/svgs/experience-cloud-logo.svg)` followed by `[Explore now \| Explore Creative Cloud plans](https://...)`. Same `text \| aria-label` pipe convention as Floating CTA: text before `\|` is shown, text after becomes the link's `aria-label`. |
| 2 — Image grid, row A | Up to 5 cells, each with one image — the "top" image for parallax columns 1–5 respectively. |
| 3 — Image grid, row B | Up to 5 cells, each with one image — stacks under the matching column from row 2 (column 1 image in row 3 goes under column 1 image in row 2, etc.). Columns 2 and 4 automatically get a 3rd image cloned from carousel slide 2's and slide 4's image — don't add a 3rd image yourself for those columns. |
| 4 — Carousel header | One cell, text only (no image) — the small heading shown above the horizontal carousel, e.g. "Explore what's new." This row is identified by *not* having an image, so keep it image-free. |
| 5–8 — Carousel slides (exactly 4 rows) | Each slide row needs **2 cells**: |
| ...cell 1 (left) | An eyebrow line, a heading, then a link paragraph, e.g. `[See details](https://...)`. Only the eyebrow and heading are visually rendered on the slide — the link paragraph is *not* shown; only its `href` is used, to make the whole slide clickable. The link text (before a `\|`, if present) is also used to build the carousel's accessible name on the first slide. |
| ...cell 2 (right) | One media item: an image, or a video (paste a video/MP4 link — Milo's standard video authoring converts it automatically). |

## Variations

Add modifier classes to the block name cell to override default text sizing (these are read from the block's own class list, e.g. "Hub Hero (heading-2, body-md, button-sm)"):

| Class | Effect | Default |
|---|---|---|
| `heading-<1–6>` | Size of the header's heading. | `heading-1` |
| `body-<sm\|md\|lg\|xl>` | Size of the header's body text. | `body-lg` |
| `button-<sm\|md\|lg\|xl>` | Size of the header CTA button. | `button-lg` |

## Example

```
| Hub Hero (heading-1, body-lg, button-lg)                                    |
|-------------------------------------------------------------------------------|
| Eyebrow text  \n ## Discover what's possible  \n Body copy about the hub.  \n ![icon](https://www.adobe.com/federal/assets/svgs/experience-cloud-logo.svg) [Explore now \| Explore Creative Cloud plans](https://adobe.com/cc) |
| ![grid1a](/g1a.png) | ![grid2a](/g2a.png) | ![grid3a](/g3a.png) | ![grid4a](/g4a.png) | ![grid5a](/g5a.png) |
| ![grid1b](/g1b.png) | ![grid2b](/g2b.png) | ![grid3b](/g3b.png) | ![grid4b](/g4b.png) | ![grid5b](/g5b.png) |
| ### Explore the latest releases |
| Eyebrow 1 \n #### Photoshop \n [See details](https://adobe.com/ps) | ![slide1](/s1.png) |
| Eyebrow 2 \n #### Illustrator \n [See details](https://adobe.com/ai) | ![slide2](/s2.png) |
| Eyebrow 3 \n #### Premiere Pro \n [See details](https://adobe.com/pr) | ![slide3](/s3.png) |
| Eyebrow 4 \n #### Lightroom \n [See details](https://adobe.com/lr) | ![slide4](/s4.png) |
```

(The pipe-table mockup above simplifies multi-paragraph cells with `\n` — in the actual authoring doc each cell is a normal table cell containing multiple paragraphs/lines.)

## Notes

- This is one of the most fragile authoring contracts in the codebase: the JS locates rows by **position** (`div:first-child`, `nth-child(2)`, `nth-child(3)`, "not first & no image" for the carousel header, and "last 4 rows" for slides), not by explicit markers. Adding, removing, or reordering rows will misassign content.
- Exactly 4 carousel slides are expected (`--slides: 4` and column-offset math assume 4). Fewer or more will visually break the scroll animation.
- The block is heavily scroll/animation driven (CSS `animation-timeline`), with full `prefers-reduced-motion` fallbacks and a `@supports not (animation-timeline: view())` fallback for browsers without scroll-driven animation support (e.g. Firefox) — no extra authoring is needed for these, they're automatic.
- On mobile, video slides autoplay/rewind based on scroll position via `IntersectionObserver`; this is automatic once a video is present in a slide's media cell.
- The first slide gets a unique, more descriptive `aria-label` (built from its link text) since assistive tech announces it as the start of the carousel; the rest just get "N of 4."
