# Split Aside Grid

> **Quick summary:** A feature-list-plus-media block — a clickable vertical list of features paired with a stacked deck of matching images/videos, expanding the description and swapping the front card on click (desktop) or swipe (mobile). Authored as one row per feature/slide, each with two cells: content (heading, body, optional link) and media. Variations: `dark`, `mobile-carousel` (an alternate mobile swipe interaction). `mobile-carousel` is only available in the expanded deployment of this block; a simpler deployment only supports `dark`.

---

A feature-list-plus-media block: a vertical list of clickable feature items on one side and a stacked "card deck" of matching images/videos on the other. On desktop, clicking a list item expands its description and swaps the front card in the stack. On mobile it becomes a swipeable interaction with prev/next controls and slide dots — by default a card-stack where the current card flies off-screen as you swipe (see Variations for an alternative mobile interaction). Authors use it to walk through several related features, each with its own illustration.

## Authoring instructions

The block is authored as **one row per feature/slide**, each row with exactly two cells.

| Row | Content |
|---|---|
| Each row = one slide | **Cell 1 (content)**: a heading (any level — on desktop this heading is hidden by CSS regardless of expanded/collapsed state, with the toggle text as the only visible label there, while on mobile the heading is the slide's visible caption), body paragraph(s) for the expanded description, and optionally one paragraph containing only a link (the link text must equal the whole paragraph's text) to render a standalone "learn more" arrow-link instead of a button. Wrapping the link in bold/italic instead produces a normal button. **Cell 2 (media)**: one image or video for that slide's card. |

Author as many rows as you have features; each becomes one card in the stack and one row in the list, in document order (first row = first/front slide).

## Variations

| Variation | Effect | How to author |
|---|---|---|
| `dark`[^dark] | Removes the block's own background color (use when the block already sits on a dark-background section). | Add `dark` to the block name, e.g. `Split Aside Grid (dark)`. |

In an expanded version of this block, a second variation is available:

| Variation | Effect | How to author |
|---|---|---|
| `mobile-carousel`[^mobile-carousel] | Changes the mobile (below-tablet) interaction from a swipe-off/fly-away card stack to a horizontal sliding carousel track — slides sit side-by-side at a 16:9 aspect ratio and translate into view (with cloned first/last slides for a seamless loop), instead of the default card literally flying off-screen and rotating. Desktop behavior (click-to-expand list) is unaffected. | Add `mobile-carousel` to the block name, e.g. `Split Aside Grid (mobile-carousel)`. |

[^dark]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^mobile-carousel]: [`60dcb44`](https://github.com/adobecom/milo/commit/60dcb44) — Ratko Zagorac, 2026-07-16

In a simpler deployment of this block, `mobile-carousel` is not available — mobile interaction is always the fly-off card-swipe stack, and `dark` is the only author-facing variation.

## Example

```
| Split Aside Grid |     |
| --- | --- |
| ### Real-time co-editing<br>Work on the same file with your team, live, with no version conflicts. | ![coedit.jpg](coedit.jpg) |
| ### Cloud-native assets<br>Every asset syncs automatically across your devices.<br>[See supported formats](https://example.com/formats) | ![assets.jpg](assets.jpg) |
| ### One-click sharing<br>Send a link, not a file — reviewers see your latest version instantly. | ![share.mp4](https://example.com/share.mp4) |
```

Where available, with the mobile carousel variant:

```
| Split Aside Grid (mobile-carousel) |     |
| --- | --- |
| ### Real-time co-editing<br>Work on the same file with your team, live, with no version conflicts. | ![coedit.jpg](coedit.jpg) |
| ### Cloud-native assets<br>Every asset syncs automatically across your devices. | ![assets.jpg](assets.jpg) |
```

## Notes

- The first row's slide is active by default (front of the stack, expanded on desktop).
- If a row has no media cell, that slide is filtered out of the interactive stack; if **no** rows have media, the whole block silently does nothing — always include a media item in every row.
- The mobile interaction is swipe-driven (pointer drag) with an aria-live region announcing "Slide X of Y" for screen-reader users; desktop is a plain click-to-expand accordion-style list — no author configuration changes this beyond the `mobile-carousel` variant where available, it's otherwise purely responsive.
- Supports Milo's `mobile-viewport`/`tablet-viewport`/`desktop-viewport` content-override rows (same viewport-delimiter pattern as [Rich Content](./rich-content.md), including the 768px/1280px breakpoint split) if you need to vary slide content per breakpoint.
- Where `mobile-carousel` is available, the code clones the first and last slide to create a seamless-loop illusion when swiping past the ends — this is automatic and requires no extra authoring.
