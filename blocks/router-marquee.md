# Router Marquee

> **Quick summary:** A full-viewport-height, auto-advancing hero carousel with a bottom tab-nav strip (icon + label per slide), used as a page's top hero for several rotating full-bleed slides a visitor can also jump between manually — e.g. a product-line router ("Photography", "Video", "Design", ...). Authored as a flat sequence of viewport-delimiter rows (`mobile-viewport` required, `tablet-viewport`/`desktop-viewport` optional) followed by one 2-cell slide row per slide (text cell: eyebrow, heading, tab icon+label, body, CTA; media cell: image or video). There are no author-facing modifier classes — content varies only by viewport delimiters. Note: adding a Section Metadata `starting-marquee` key reorders which slide plays first, and a `parallax move up fast` class on the *next* section makes this block reposition its nav controls automatically.

## Authoring instructions

The block is authored as a flat sequence of rows: a single-cell **viewport delimiter row**, followed by one **slide row per slide** for that viewport. At minimum you need a `mobile-viewport` delimiter and its slides — `tablet-viewport` and `desktop-viewport` delimiters are optional. Breakpoint is screen width: mobile = below 768px, tablet = 768–1279px, desktop = 1280px and up.

| Row | Content |
| --- | --- |
| Viewport delimiter | A row with a single cell containing `mobile-viewport`, `tablet-viewport`, or `desktop-viewport`. Marks the start of that viewport's set of slides. Bare `mobile`/`tablet`/`desktop` still works but is a legacy fallback being phased out — use the `-viewport` form in new authoring. Only `mobile-viewport` is strictly required. |
| Slide row (2 cells) | **Cell 1 (text):** an optional eyebrow paragraph, then a heading (H1 or H2 — becomes the slide title), then a small tab-icon paragraph (a link/image pointing to an `.svg` file), then immediately after it a label paragraph containing the link+text that becomes that slide's nav card (label text + destination URL), then any remaining body paragraph(s), then an optional CTA paragraph. **Cell 2 (media):** a background image, or an embedded video (it is automatically muted, looped, and lazy-loaded as the slide's animated background). |

Within cell 1, order matters because the script identifies pieces structurally, not by label:
- **Eyebrow** = the paragraph immediately before the heading (any short line of text works, no special markup).
- **Title** = the first `<h1>` or `<h2>` found.
- **Tab icon + label** = a paragraph linking to an `.svg` asset (the nav card's icon), immediately followed by a paragraph containing a link (its text becomes the card's visible label, its href becomes the card's destination). Both paragraphs are removed from the slide body — they only render as the bottom nav card.
- **CTA** = a paragraph containing italicized (`_..._`) links: a bold link (`**[text](url)**`) becomes the primary filled button, a plain link becomes the secondary outline button, e.g. `_**[Learn more](#)** [See plans](#)_`.
- **Body** = any other paragraphs left in the cell.

## Variations

This block has no author-facing modifier classes (nothing added in parentheses after the block name). Content variation is controlled entirely by the viewport delimiter rows described above:

| Behavior | Effect | How to author it |
| --- | --- | --- |
| Only `mobile-viewport` defined | Same slides shown at every screen size. | Omit `tablet-viewport`/`desktop-viewport` delimiter rows entirely. |
| `tablet-viewport`/`desktop-viewport` defined with fewer slides than `mobile-viewport` | That viewport only shows the slides you explicitly listed (slide *count* is not inherited, only cell content is). | Add the delimiter row and only as many slide rows as you want for that viewport. |
| A slide's text or media cell left blank in `tablet-viewport`/`desktop-viewport` | That specific cell inherits content from the same-position slide in the next-lower defined viewport. | Leave the cell empty in the table for that slide. |
| Reorder which slide plays first | Moves a given slide to the front of the rotation, across all viewports. | Add a **[Section Metadata](./section-metadata.md)** block in the same section with key `starting-marquee` and the 1-based slide number as the value. |

## Example

```
| Router Marquee |
| --- | --- |
| mobile-viewport |
| ## Photography <br> [](icons/photography.svg) <br> [Photography](/photography/) <br> Edit and organize every shot. <br> _**[Explore](#)** [Learn more](#)_ | ![](/media/photo-bg-mobile.jpg) |
| ## Video <br> [](icons/video.svg) <br> [Video](/video/) <br> Cut, color, and publish faster. <br> _**[Explore](#)** [Learn more](#)_ | ![](/media/video-bg-mobile.jpg) |
| desktop-viewport |
| ## Photography <br> [](icons/photography.svg) <br> [Photography](/photography/) <br> Edit and organize every shot. <br> _**[Explore](#)** [Learn more](#)_ | ![](/media/photo-bg-desktop.jpg) |
| ## Video <br> [](icons/video.svg) <br> [Video](/video/) <br> Cut, color, and publish faster. <br> _**[Explore](#)** [Learn more](#)_ | ![](/media/video-bg-desktop.jpg) |
```

## Notes

- Slides auto-advance every 5 seconds, are swipeable on touch, and pause automatically whenever a visitor interacts with a link/button in the slide or scrolls to the next section; there's a visible pause/play control and a screen-reader hint announcing that autoplay is on. None of this is author-configurable.
- If `prefers-reduced-motion` is set, autoplay starts paused and slide transitions/staggered text animation are skipped — no authoring needed, this is automatic.
- Because slide count can legitimately differ between mobile and desktop (see Variations table), double-check each viewport's nav-card strip after publishing — a mismatched count is easy to introduce by accident when only editing one viewport's rows.
- The icon paragraph must link directly to an `.svg` file path; other image formats won't be picked up as the tab icon.
- Video gotcha (media cell): pair the video link with its poster image as two adjacent cells/lines — Milo grabs the poster from whichever image sits next to the video link, and won't show one otherwise. For the video to autoplay only while scrolled into view (instead of finishing during page load), the video link's hash needs both `autoplay` and `viewportplay`, e.g. `#autoplay|viewportplay`. Using `#autoplay` alone plays the video immediately on page load — by the time it's visible it has already finished, so visitors just see its frozen last frame.
- **[Section Metadata](./section-metadata.md) `layout`/`style` interaction:** if you add `parallax move up fast` (→ class `parallax-move-up-fast`) to the Section Metadata `layout`/`style` row of the *section immediately after* this Router Marquee (e.g. so that next section animates up and covers the marquee as the visitor scrolls), Router Marquee's own CSS detects that adjacent class and repositions its bottom nav-card controls to make room. You only need to add the class to the following section — Router Marquee reacts to it automatically. This is part of Milo's shared scroll-animation system (see [section-metadata.md](./section-metadata.md)), not a Router Marquee variant of its own.
