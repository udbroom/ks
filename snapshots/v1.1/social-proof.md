# Social Proof

> **Quick summary:** A single testimonial/highlight card combining an image with either a heading-and-body text block or a pull-quote, plus a subtle scroll-driven zoom animation — used to spotlight a customer story, quote, or key stat alongside supporting imagery. Authored as two rows: Row 1 holds the text (and an optional background-color cell), Row 2 holds the media. No author-facing variation classes — the pull-quote layout is triggered simply by formatting Cell 1's text as a blockquote. Row 2's media cell is read without a null-check, so a missing media item will throw at author-time rather than fail silently.

## Authoring instructions

The block is authored as **two rows**.

| Row | Content |
|---|---|
| Row 1 (text + optional background color) | **Cell 1**: the text content — either (a) a heading (any level) followed by body paragraph(s) and optional buttons, or (b) a blockquote (author applies "Quote"/blockquote formatting to a paragraph in your doc tool) — see Variations below for how the blockquote changes the layout. **Cell 2 (optional)**: plain text naming a background color (e.g. `#1E1E1E` or a CSS color keyword) applied to the whole card. Leave empty for no custom background. |
| Row 2 (media) | One cell containing a single image or video — this becomes the card's photo/video panel. |

## Variations

This block has no author-facing modifier classes. The only structural choice authors make is content-driven, not a class:

| Choice | Effect | How to author |
|---|---|---|
| Blockquote content | Instead of a heading + body layout, the text renders as a pull-quote: the quote text is styled as a large heading (with any leading curly opening-quote character hung outside the text block), and any additional lines in the blockquote become a caption (e.g. attribution name, title) below it. | Format the text in Cell 1 as a blockquote in your authoring tool; put the quote as the first line and attribution details as additional lines within the same blockquote. |

## Example

Headline + body:

```
| Social Proof |     |
| --- | --- |
| ## 40% faster turnaround<br>Since switching to Creative Cloud, our team ships campaigns in half the time. |     |
| ![customer-photo.jpg](customer-photo.jpg) |
```

Pull-quote variant with background color:

```
| Social Proof |     |
| --- | --- |
| > "This is the first tool that actually keeps up with our creative team."<br>Jamie Lee<br>Creative Director, Acme Co. | #1E1E1E |
| ![customer-photo.jpg](customer-photo.jpg) |
```

## Notes

- If Row 1 is missing entirely, the block renders nothing — Row 1 is required.
- Row 2's media cell isn't checked for emptiness before the block tries to style it, so an empty or missing Row 2 will cause an error when the page loads — always include a media item in Row 2.
- Supports Milo's mobile/tablet/desktop content-override rows (same viewport-delimiter pattern described in [rich-content.md](./rich-content.md)'s Notes).
- The card has a scroll-linked "stretch" and content-enter animation built into the CSS; this is automatic and not configurable per instance, and is disabled under `prefers-reduced-motion: reduce`.
- Video gotcha (Row 2 media): pair the video link with its poster image as two adjacent cells/lines — Milo grabs the poster from whichever image sits next to the video link, and won't show one otherwise. For the video to autoplay only while scrolled into view (instead of finishing during page load), the video link's hash needs both `autoplay` and `viewportplay`, e.g. `#autoplay|viewportplay`. Using `#autoplay` alone plays the video immediately on page load — by the time it's visible it has already finished, so visitors just see its frozen last frame.
