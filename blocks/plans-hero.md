# Plans Hero

> **Quick summary:** A simple full-width hero banner — background image with a scrim, plus an overlaid text block (eyebrow, heading, body, CTA) — authored as one row with 2 cells (text, media). No variations. Some deployments support an optional focal-point line (e.g. `left, top`) below the image to control crop position; others always crop from center.

---

A simple full-width hero banner: a background image with a dark scrim on one side, and a text block (eyebrow, heading, body copy, CTA) overlaid on top. Use it for a plans/pricing page header where you need a media-backed hero without any of the scroll animation used by the other hero blocks.

## Authoring instructions

The block is authored as a single row with 2 cells.

| Row | Content |
| --- | --- |
| 1 (2 cells) | **Cell 1 (text):** an optional eyebrow line (short text directly above the heading), a heading (`H1`–`H6`), one or more body paragraphs, and CTA button(s) authored with Milo's standard **bold link** (filled button) / *italic link* (outline button) syntax. **Cell 2 (media):** a background image, authored as a normal `<picture>`. In some deployments of this block you can optionally add a second line of plain text below the image giving a focal point, e.g. `left, top`, to control which part of the image stays visible when it's cropped (see Notes); in a simpler deployment this option isn't available and the image always crops from the center. |

## Variations

This block has no author-facing variations. There are no modifier classes checked in the JS or CSS — the only visual changes come from the responsive breakpoints (image scrim gradient position and content max-width adjust automatically at 768px and 1440px).

## Example

```
| Plans Hero |
| --- | --- |
| Creative Cloud plans <br> ## Find the plan that's right for you <br> Get one app or the whole collection, all backed by the latest features. <br> **[See plans](https://www.adobe.com/creativecloud/plans.html)** | ![](/media/plans-hero-bg.jpg) <br> left, top |
```

## Notes

- Where the focal-point option is available: adding a second paragraph (or trailing plain text line) in the media cell — e.g. `left, top` or `30%, 70%` — sets which part of the background image stays visible when it's cropped, and that text is then removed so it doesn't render as visible copy. If you don't need custom cropping, simply omit the second line and the image behaves the same as in a deployment without this option (default centered cropping).
- If the media cell has no `<picture>`, the hero still renders with just the text content and an empty media div — no image, no scrim visible.
- If the text cell is empty/missing, the block still creates an empty content container so the layout doesn't break, but there will be no visible text.
