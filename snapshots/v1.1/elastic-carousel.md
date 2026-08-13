# Elastic Carousel

> **Quick summary:** A row of compact cards (typically around 5) that elastically expand on hover/focus to reveal more of a video or image, then settle back down, with scroll-driven stacking on mobile — used for a horizontal showcase of linked items like feature highlights or tutorial teasers. Authored as one row per card, each with two columns: a text column read positionally as icon, heading, link name, then description (which must contain the link), and a media column (image or `.mp4` link). No author-facing variations — behavior only changes automatically for RTL pages. Gotcha: the whole card is one big link, so avoid adding a second link elsewhere in the card.

## Authoring instructions

The block is authored as **one row per card (slide)**, each row having exactly **two columns**: a text column (left) and a media column (right).

Each row is treated as one slide. Within the left column, the code reads the **first four child elements in order** — icon, heading, link name, description — and looks for the link *inside the last of those four (the description)*.

| Row (= one card) / Column | Content |
|---|---|
| Left column, item 1 — Icon | A small icon image (rendered at 24×24). Required as the first item. |
| Left column, item 2 — Heading | A heading (any level) shown at the top of the card, above the media. |
| Left column, item 3 — Link name | Short label text shown in the card's footer, above the description (e.g. "Watch now"). |
| Left column, item 4 — Description | Descriptive text shown in the footer under the link name. **This paragraph must contain the link** — that link's `href` becomes the destination for the entire card (the whole card is one big clickable link). |
| Right column — Media | A single image, or a link to an `.mp4` video (Milo's standard video-link authoring — Milo converts a plain link to a video file into an inline video automatically). On mobile, videos autoplay/rewind as they scroll into and out of view; on desktop, they play on hover/focus. |

## Variations

This block has no author-facing modifier classes — there are no variant checks in the code, and the only classes it manages are internal state (added/removed automatically as the visitor hovers, scrolls, etc.), not something you author.

The only behavioral change driven by authoring context is document direction: on right-to-left (RTL) pages, slide order is reversed and hover-arrow/underline decorations flip automatically — this is inherited from the page's text direction setting, not something added to the block name.

## Example

```
| Elastic Carousel                                                                                          |
| ---------------------------------------------------------------------------------------------------------- |
| ![icon](https://www.adobe.com/federal/assets/svgs/experience-cloud-logo.svg)                                                                                     |
| ## Generative Fill                                                                                          |
| Watch now                                                                                                    |
| See how Generative Fill extends and edits images in seconds. [Watch the demo](https://www.adobe.com/videos/gen-fill-demo.mp4) | ![Generative Fill demo preview](/gen-fill-poster.jpg) |
| ------------------------------------------------------------------------------------------------------------ |
| ![icon](https://www.adobe.com/federal/assets/svgs/experience-cloud-logo.svg)                                                                                      |
| ## Firefly for video                                                                                          |
| Learn more                                                                                                    |
| Bring AI-generated effects into your video timeline. [Explore Firefly video](https://www.adobe.com/firefly-video.html) | ![Firefly video effects preview](/firefly-video-thumb.jpg) |
```

## Notes

- The left column's first four items are read **positionally** — you cannot omit the icon or reorder heading/link-name/description; if a slide is missing one of them, later items will shift into the wrong role (e.g. the description's link will be searched for in whatever content actually lands in that fourth slot).
- Because the entire card is a single link, don't add a second link elsewhere in the card — only the link found inside the fourth (description) item is used, but any other links will be visually inert or confusing since clicks anywhere on the card navigate via the card's own link.
- Five cards is the assumed/default layout width (the sizing math is tuned around five); adding more or fewer will still work, but the elastic hover-grow width and gaps are tuned around five cards.
- On the first slide, the accessible label read to screen readers includes the carousel's name, derived from the link's text split on a pipe character (`Label | Carousel Name`) — if you don't include a pipe in the first slide's link text, the whole link text is used and "Adobe slides" is used as a fallback name.
- Row order in the doc table is the slide order shown left-to-right (or right-to-left, reversed automatically, on RTL pages).
- The label paragraph's text is also reused for analytics tracking and for building the carousel's accessible name, which the code expects in a `Category|Label` pipe-delimited format (e.g. `Adobe Express|Learn more`) — if you omit the pipe, the carousel's accessible label falls back to the generic string "Adobe slides".
- SVG images (icon or media) are automatically rewritten to Milo's federated (shared, cross-site) asset URL; no special authoring is needed beyond using a normal image.
- Video slides only get their real playback, autoplay/rewind-on-hover, and mobile auto-play-in-view behavior if the media cell resolves to an actual video element via Milo's standard video-link authoring — a plain video *file link* pasted the normal Milo way is what triggers this; a video embedded via an unsupported method will just render as a static link/image.
- Video gotcha: the poster image (shown in the example above) must sit immediately next to the video link — Milo grabs the poster from whichever image is adjacent to the link, and won't show one otherwise. For the mobile auto-play-in-view behavior above to actually kick in, the video link's hash needs both `autoplay` and `viewportplay`, e.g. `#autoplay|viewportplay`. Using `#autoplay` alone plays the video immediately on page load — by the time it scrolls into view it has already finished, so visitors just see its frozen last frame.
