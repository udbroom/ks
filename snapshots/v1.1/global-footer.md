# Global Footer

> **Quick summary:** The shared site-wide footer (menu columns, featured products, region picker, legal links, social icons, and the Adobe logo) that appears automatically across Milo pages. The block instance on a page is normally empty — real content is authored in a separate shared footer document (default `/footer`, overridable per-page via a `footer-source` metadata key), not in the block's own rows. Only variation: `responsive-container`. Key gotcha: editing the block directly on a page does nothing — all content changes must go in the footer document.

## Authoring instructions

The `global-footer` block itself, as placed on a page, is normally just an empty block with no authored rows — it doesn't read any content you put inside it. Instead, it fetches a separate plain-HTML document (by default `<locale>/footer`, e.g. `/footer`) and builds the footer from that document's contents. This lets one footer document power every page in a locale.

If you need a page (or a set of pages) to use a *different* footer document, set the page-level metadata key `footer-source` to the path of that document.

The real authoring happens **in the footer document**, which follows this structure:

| Row / Section in the footer document | Content |
|---|---|
| Menu columns | Any number of `##` (H2) headings, each followed by a list of links (plain links become nav links; a link inside **bold** or *italic* becomes a highlighted CTA button). Each H2 starts a new column/section — put a new H2 wherever you want a new labeled group of links. |
| Featured products | A block of links where each link (and optionally a small icon image + one description line under it) is wrapped as its own "link-group" — author this as its own distinctly-styled group of items (image, link title, optional description) rather than plain bullet links; it renders as a separate row of icon+label tiles above the legal/region area. |
| Region selector | One link, authored with the "region-selector" styling, pointing either to a page fragment (renders as an expandable in-page region list) or to a URL with a `#` hash (renders as a button that opens the region-picker in a modal). |
| Social links | A set of links to known social platforms (Facebook, Instagram, X/Twitter, LinkedIn, Pinterest, Discord, Behance, YouTube, Weibo) authored with the "social" styling — each recognized platform link is swapped for its icon automatically. |
| Legal / copyright | A paragraph whose copyright sentence is wrapped in *italics* (em) — this text is stripped out and replaced with "© `<current year>` Adobe Inc. `<rest of your italic text>`" automatically. Any additional privacy links (e.g. "Do not sell my info", "Cookie preferences", "Ad choices") go in the same block, after the copyright paragraph. |

## Variations

| Variation | Effect | How to author it |
|---|---|---|
| `responsive-container`[^responsive-container] | Switches the footer's mobile/desktop layout decision from "viewport width" to "the footer's own container width" (via a resize observer), so it lays out correctly when embedded in a narrower container (e.g. a side panel) rather than the full page. | Add "responsive-container" to the `global-footer` block's name cell on the page where the block is placed, e.g. "Global Footer (responsive-container)". |

[^responsive-container]: [#5692](https://github.com/adobecom/milo/pull/5692) — Rares Munteanu, 2026-03-30

## Example

On the page (block instance — typically no rows needed):

```
| Global Footer |
| -------------- |
```

In the shared footer document (`/footer`), a minimal example:

```
## Products

[Photoshop](https://www.adobe.com/photoshop.html)
[Lightroom](https://www.adobe.com/lightroom.html)

## Support

[Help Center](https://helpx.adobe.com/)
**[Contact us](https://www.adobe.com/contact.html)**

*Choose your region*
[Change region](https://www.adobe.com/#_regionmodal)

[Facebook](https://www.facebook.com/adobe)
[Instagram](https://www.instagram.com/adobe)

*Copyright © 2026 Adobe. All rights reserved.*
[Privacy](https://www.adobe.com/privacy.html) [Terms](https://www.adobe.com/terms.html) [Ad choices](https://www.adobe.com/privacy.html#interest-based-ads)
```

## Notes

- Do not put footer content directly on ordinary pages expecting it to show up — content only comes from the footer document at the resolved path (`/footer` by default, or your `footer-source` override). Editing the block instance on a normal page has no effect on the footer's content.
- The footer only decorates once it scrolls near the viewport (or after a 3-second fallback) — during local preview it can take a moment to populate.
- If the footer document can't be fetched, the footer silently fails to render (logged as an error) rather than showing a broken block — always verify the footer document path exists and is published.
- Menu columns automatically collapse into a "stacked" 3-per-row grid on desktop if there are more than 3 columns and they don't all fit on one line — no manual layout authoring is needed for that.
- Region-selector links that include a `#` hash open in a modal (loading the region-nav block); links without a hash instead load as an inline expanding fragment. Pick the destination link type based on which behavior you want.
