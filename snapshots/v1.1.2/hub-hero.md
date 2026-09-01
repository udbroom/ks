# Hub Hero

> **Quick summary:** A large scroll-driven hero with a fading header, a parallax image grid, and a horizontal carousel of slides that appear to "rise" out of the grid as you scroll — used as the top-of-page hero for hub/landing pages wanting a cinematic, scroll-linked reveal instead of a static hero. Authored as a strict, fixed sequence of 8 rows (header, image-grid rows, carousel header, slide rows). By default the carousel takes exactly 4 slides across a 5-column grid; the `slides-3` variation switches to exactly 3 slides across a 3-column grid instead — pick one carousel size and match your row count to it. Other variations: `dark` (knockout color treatment) and the text-sizing modifier classes `heading-<1–6>`, `body-<sm|md|lg|xl>`, `button-<sm|md|lg|xl>`. Important gotcha: content is located by row position, not markers, so adding/removing/reordering rows (or authoring a slide count that doesn't match whichever layout you're using) breaks the layout.

## Authoring instructions

This block has a **strict row order** — it always expects exactly 8 rows, in this exact sequence. Which rows are "image grid" rows vs. "carousel slide" rows depends on whether you're using the default 4-slide layout or the `slides-3` variation (see Variations) — getting the row count, order, or slide count wrong for whichever layout you're using will break the scroll math and column mapping.

| Row | Default (4 slides) | With `slides-3` |
|---|---|---|
| 1 — Header | One cell containing (in order): an optional eyebrow line, a heading (`h1`–`h6`), body paragraph(s), and a CTA paragraph with an inline icon image + link, e.g. `![icon](https://www.adobe.com/federal/assets/svgs/experience-cloud-logo.svg)` followed by `[Explore now \| Explore Creative Cloud plans](https://...)`. Same `text \| aria-label` pipe convention as Floating CTA: text before `\|` is shown, text after becomes the link's `aria-label`. | Same |
| 2 — Image grid, row A | Up to 5 cells, each with one image — the "top" image for parallax columns 1–5. | Up to 3 cells, image or video — the "top" media for columns 1–3[^slides-3-video]. |
| 3 — Image grid, row B | Up to 5 cells, each with one image — stacks under the matching column from row 2. Columns 2 and 4 automatically get a 3rd image cloned from carousel slide 2's and slide 4's image — don't add a 3rd image yourself for those columns. | Up to 3 cells, stacks under row 2's columns. Columns 1 and 3 automatically get a 3rd image cloned from carousel slide 2's and slide 3's image instead[^slides-3-video].|
| 4 — Image grid, row C | *(not used — only 2 grid rows in the default layout)* | Up to 3 cells — a third stacked image row per column (the default layout only has 2 grid rows; `slides-3` adds this one). |
| 4 (default) / 5 (`slides-3`) — Carousel header | One cell, text only (no image) — the small heading shown above the horizontal carousel, e.g. "Explore what's new." This row is identified by *not* having an image, so keep it image-free. | Same, just one row later. |
| 5–8 (default) / 6–8 (`slides-3`) — Carousel slides | Exactly **4** slide rows. | Exactly **3** slide rows. |
| ...cell 1 (left) | An eyebrow line, a heading, then a link paragraph, e.g. `[See details](https://...)`. Only the eyebrow and heading are visually rendered on the slide — the link paragraph is *not* shown; only its `href` is used, to make the whole slide clickable. The link text (before a `\|`, if present) is also used to build the carousel's accessible name on the first slide. | Same. |
| ...cell 2 (right) | One media item: an image, or a video (paste a video/MP4 link — Milo's standard video authoring converts it automatically). Optionally, a second paragraph/image after the media becomes a small icon overlay on the slide — but this overlay currently only has visual styling in the `slides-3` layout; adding it in the default 4-slide layout has no defined position/appearance yet. | Same, and the icon overlay is fully styled here (positioned top-left of the slide media, fades in on scroll). |

Either way, the block always totals exactly 8 rows — `slides-3` just redistributes them (3 grid rows + 3 slides instead of 2 grid rows + 4 slides).

## Variations

Add modifier classes to the block name cell (these are read from the block's own class list, e.g. "Hub Hero (heading-2, body-md, button-sm, slides-3)"):

| Class | Effect | Default |
|---|---|---|
| `slides-3`[^slides-3] | Switches the carousel from 4 slides/5-column grid to 3 slides/3-column grid — see Authoring instructions for the row-count differences. Also enables the slide-media icon overlay's visual styling. | Off (4-slide layout) |
| `dark`[^slides-3] | Knockout color treatment: dark background, gray-900 slide/header/footer/media backgrounds, and subheading-colored text throughout the carousel. | Off (light) |
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

- This is one of the most fragile authoring contracts in the codebase: the JS locates rows by **position** (`div:first-child`, `nth-child(2)`, `nth-child(3)`, "not first & no image" for the carousel header, and "last N rows" for slides), not by explicit markers. Adding, removing, or reordering rows will misassign content.
- Slide count must match the layout you're using: exactly 4 for the default layout, or exactly 3 with `slides-3`[^slides-3] (the column-offset math and grid-row count assume whichever one you picked). Fewer or more will visually break the scroll animation.
- The block is heavily scroll/animation driven (CSS `animation-timeline`), with full `prefers-reduced-motion` fallbacks and a `@supports not (animation-timeline: view())` fallback for browsers without scroll-driven animation support (e.g. Firefox) — no extra authoring is needed for these, they're automatic.
- On mobile, video slides autoplay/rewind based on scroll position via `IntersectionObserver`; this is automatic once a video is present in a slide's media cell.
- Video gotcha: pair the video link with its poster image as two adjacent cells in the same row — Milo grabs the poster from whichever image sits next to the video link, and won't show one otherwise. For the scroll-triggered play/pause above to actually kick in, the video link's hash needs both `autoplay` and `viewportplay`, e.g. `#autoplay#viewportplay`. Using `#autoplay` alone plays the video immediately on page load — by the time it scrolls into view it has already finished, so visitors just see its frozen last frame.
- With `slides-3`[^slides-3-video], video in either the image grid or the carousel slides autoplays purely on scroll position (playing once ~50% visible, pausing when it scrolls out) — the `#autoplay#viewportplay` hash convention above isn't needed for these. This only kicks in for videos **5.1 seconds or shorter**; longer videos are left paused on their poster frame instead of autoplaying. Reduced-motion visitors never get autoplay here either way.
- In most deployments, a slide's accessible name is built from its own eyebrow and heading text — there's no special first-slide treatment and no generic "N of &lt;slide count&gt;" announcement. In one deployment the older behavior remains: the first slide gets a distinct label built from its link text, and every other slide is announced only as "N of &lt;slide count&gt;." Either way this is automatic. A slide whose link opens a modal is also announced as a button rather than a link in most deployments; one deployment always announces it as a link.[^a11y-label]

[^slides-3]: [#6406](https://github.com/adobecom/milo/pull/6406) — Denys Fedotov, 2026-08-05
[^slides-3-video]: [#6469](https://github.com/adobecom/milo/pull/6469) — Ryan Clayton, 2026-08-20
[^a11y-label]: [#6177](https://github.com/adobecom/milo/pull/6177) — 2026-06 (reached this branch's other deployment 2026-08-25)

## GTK

### Video Flags and Attributes

Add one or more of these to the end of the video's link URL, after a `#`. To combine more than one, put each behind its own `#`, e.g. `#autoplay#viewportplay` — don't use `|` to join them: `|` is also how a poster image's embedded video URL is separated from its own alt text (see the video gotcha above), so a `|` inside the video's hash breaks that split.

| Flag | Effect |
| --- | --- |
| `autoplay` | Plays automatically, muted, and loops. Used alone, playback starts as soon as the page loads — if the video isn't visible yet, it can finish before a visitor scrolls to it. Pair with `viewportplay` to avoid that. |
| `autoplay1` | Same as `autoplay`, but plays once instead of looping. |
| `viewportplay` | Delays playback until the video scrolls into view, and pauses it again once it scrolls out. Combine with `autoplay` (`#autoplay#viewportplay`) so it doesn't finish before becoming visible. |
| `hoverplay` | No autoplay — instead, the video is muted and plays only while a visitor hovers over or focuses it, pausing otherwise. |
| `_hide-controls` | Skips the pause/play accessibility control overlay that autoplay/hoverplay videos normally get layered on top of them — use for purely decorative video where a visible, keyboard-focusable pause button doesn't add value. When combining with another flag, put it first, e.g. `#_hide-controls#autoplay`. |

Note: with `slides-3`, video autoplays purely from scroll position and doesn't need these flags at all (see Notes above) — this table applies to the default (non-`slides-3`) carousel/grid video.
