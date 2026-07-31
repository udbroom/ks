# Floating CTA

> **Quick summary:** A sticky, single-button CTA that slides/fades into view as the reader scrolls. Authored as 1 row, 1 cell containing exactly two paragraphs (an icon image, then a link/text for the button). No named variations, but the link type (plain vs. a commerce/checkout link) changes runtime behavior. Important: the CTA is invisible by default and only appears via a required companion Section Metadata `custom-hide` row — without it, the block never shows up.

---

A single call-to-action (CTA) button that sticks to the bottom of the viewport and slides/fades into view once its section is in view. Use it when you want a persistent "Buy now" / "Get started" style button that follows the reader down the page (or on/off, based on which section is currently visible) instead of a CTA that scrolls away with the content.

## Authoring instructions

The block only reads its **first row, first cell**, and that cell must contain exactly two paragraphs, in order:

| Row | Content |
|---|---|
| 1 (only row), paragraph 1 | An image (the icon shown to the left of the button text, e.g. a small product/app icon). |
| 1 (only row), paragraph 2 | The button text, as a link. Format: `[Get Adobe Photoshop](https://...)`. To set a different accessible name (the text read aloud by screen readers) than the visible text, add `\| aria label text` after the visible text, e.g. `Get Photoshop \| Get Adobe Photoshop, starting at $9.99/month` — the part before `\|` is shown, the part after becomes the accessible name. If there is no link (plain text only), the plain text is used as both the button label and a placeholder destination. |

Both paragraphs are required — if the block only has one paragraph, or the first paragraph has no image, nothing renders.

The block automatically:
- Appends a right-pointing arrow icon after the button text (not authored).
- Converts any relative (root-relative, starting with `/`) image path to a federated/absolute URL.

### Optional: auto-hide based on another section

Floating CTA can hide itself while a specific section is in view and reappear once the reader scrolls past it. To enable this, add a **[Section Metadata](./section-metadata.md)** block to the *same section* as the Floating CTA with a row:

| Key | Value |
|---|---|
| custom-hide | A CSS selector for the section to watch, e.g. `.hero` or `#pricing` |

When the referenced section is in view, the CTA is hidden (not visible, not keyboard-focusable); once it scrolls out of view, the CTA becomes active/visible again.

**This [Section Metadata](./section-metadata.md) row is effectively required, not optional.** The CTA is authored invisible and non-interactive by default, and the `custom-hide` behavior above is the only thing that ever makes it appear. If you skip the Section Metadata block, the Floating CTA will render in the page but stay permanently invisible — nothing else makes it show up.

## Variations

This block has no modifier classes added to the block name (no "Floating CTA (dark)" style variants). However, the **kind of link** you author changes runtime behavior:

| Authoring choice | Effect |
|---|---|
| Plain/standard link | Renders a normal floating anchor button with icon + text + arrow, linking to the given URL. |
| Merch/commerce (checkout) link — a link that Milo's commerce tooling upgrades into a live checkout link | The block waits for that link to finish its commerce upgrade, then reuses the live checkout link itself so "Add to cart"/checkout behavior keeps working. If the upgrade times out (10 seconds) or errors, the whole block removes itself from the page. |

## Example

```
| Floating CTA           |
|-------------------------|
| ![icon](https://www.adobe.com/federal/assets/svgs/experience-cloud-logo.svg) |
| [Get Photoshop \| Get Adobe Photoshop, starting at $9.99/month](https://www.adobe.com/products/photoshop.html) |
```

## Notes

- Respects reduced-motion accessibility settings: the slide/fade transition is removed for visitors who have requested reduced motion in their system settings.
- Image paths are only rewritten to an absolute URL if they start with `/` (root-relative); already-absolute URLs are left as-is.
