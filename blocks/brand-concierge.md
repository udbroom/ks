# Brand Concierge

> **Quick summary:** An AI chat entry point that opens a full-screen chat modal from a hero, inline section, or scroll-following floating element. Authored as a fixed, positional stack of 5 rows — Background, Header, Cards, Input, Legal — always in that order, even for floating-only variants. Key variations: `hero`, `input-first`, `floating-button`, `floating-button-only`, `floating-anchor-hide`, `floating-delay-<ms>`, `floating-anchor-delay-<ms>`, `c2-dark`, `pill-cards` (some deployments also add `dark` and `floating-input`/`floating-input-only`/`floating-input-dark`). Gotcha: rows are read positionally, so never skip or delete a row — leave it empty instead.

---

An AI chat entry point ("Ask") that lets visitors type a question or tap a suggested prompt to open a full-screen AI chat modal (a pop-up overlay). Use it as a page hero (the large, top-of-page introductory section), an inline section further down the page, or as a small floating button/bar that follows the visitor as they scroll. Choose it when a page wants to offer AI-assisted product guidance instead of (or alongside) standard marketing content.

## Authoring instructions

The block is authored as a stack of rows. Which rows are required depends on the variation (see below), but the row **order is always the same**: Background, Header, Cards, Input, Legal. The rows are read positionally by the code, so you cannot skip a row in the middle — leave it empty instead of deleting it if you don't need it (this still applies even for the "floating-only" variants, where the whole row set is discarded after being read).

| Row | Content |
|---|---|
| 1. Background | Either a solid/gradient color value as plain text (e.g. `#F5F5F5`), or an image. Leave empty for no background. |
| 2. Header | A heading (any level) for the title, and optionally one paragraph directly after it for the subtitle. If you provide plain text with no heading/paragraph markup, it's used as the subtitle. |
| 3. Cards | One or more suggested-prompt cards. Author each card as its own line/paragraph: optionally an image first (used as the card's icon/photo depending on variation), then the prompt text. Each card becomes a clickable pill/tile that pre-fills the chat input with that text and opens the chat. |
| 4. Input | Plain text used as the input field's placeholder (e.g. "Ask Adobe AI a question…"). |
| 5. Legal | Legal/disclaimer text (supports links). |

Clicking a card or submitting text in the input opens a modal containing Adobe's hosted Brand Concierge chat experience; the heading, subtitle, cards, and input placeholder you authored are passed into that chat as overrides. If a visitor isn't already signed in and takes an action that requires it, a sign-in modal opens automatically as part of the chat flow — this isn't something you author, it's built into the block.

## Variations

Add these as modifier classes on the block name cell, e.g. "Brand Concierge (hero)". Some combine.

| Variation | Effect | How to author it |
|---|---|---|
| (default — no class) | Standard inline block: background, header, cards, input, legal, in that order top to bottom. | Leave the block name plain: "Brand Concierge". |
| `hero`[^hero] | Same row order as default, but sized/spaced as a page hero (bigger heading, wider input). | "Brand Concierge (hero)" |
| `input-first`[^input-first] | Swaps the visual order of Cards and Input (input field renders above the suggested-prompt cards) in the default layout. | "Brand Concierge (input-first)" |
| `floating-button`[^floating-button] | Adds a floating pill button (in addition to the normal rows) that stays pinned to the bottom of the viewport as the visitor scrolls, opening the chat on click. | "Brand Concierge (floating-button)" |
| `floating-button-only`[^floating-button-only] | Renders **only** the floating button — background/header/cards/input/legal rows are removed from the page entirely. | "Brand Concierge (floating-button-only)" |
| `floating-anchor-hide`[^floating-anchor-hide] | Hides the floating button once the visitor scrolls past the bottom of the page's main content (instead of staying pinned). | Combine with `floating-button` or `floating-button-only`. |
| `floating-delay-<ms>` | Delays showing the floating button until the visitor has scrolled past `<ms>` pixels. | e.g. "Brand Concierge (floating-button, floating-delay-400)" |
| `floating-anchor-delay-<ms>` | Delays hiding the floating element near the bottom of the page by `<ms>` pixels. | e.g. "floating-anchor-delay-200" |
| `c2-dark`[^c2-dark] | Switches header/input/card text and chrome to a dark-mode color scheme, with larger heading sizes at wider screen widths. | "Brand Concierge (hero, c2-dark)" |
| `pill-cards`[^pill-cards] | Renders the suggested-prompt cards as compact horizontal pills instead of full tiles (tablet screens and larger). | "Brand Concierge (pill-cards)" |

[^hero]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^input-first]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^floating-button]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^floating-button-only]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^floating-anchor-hide]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^c2-dark]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23
[^pill-cards]: [#6219](https://github.com/adobecom/milo/pull/6219) — Rares Munteanu, 2026-06-23

Some deployments of this block also support:

- A plain `dark` variant — a simpler dark-mode color scheme, distinct from and less elaborate than `c2-dark` (smaller heading sizes, plainer card borders). Where both are available, treat `c2-dark` as the richer/preferred dark option and `dark` as a lighter-touch alternative.
- A `floating-input` variant, which adds a floating input bar (with the suggested-prompt cards shown as pills) that follows scroll, alongside the normal content — and a `floating-input-only` variant that renders just that floating bar, discarding the other rows the same way `floating-button-only` does. `floating-input-only` combined with `floating-anchor-hide` hides the bar once the visitor scrolls past the page's main content. A `floating-input-dark` modifier applies dark styling specifically to this floating input bar. Where this variant isn't available, use `floating-button` for a persistent scroll-following entry point instead.

## Example

```
| Brand Concierge (hero)                                    |
| ---------------------------------------------------------- |
| #F5F5F5                                                    |
| ## Ask Adobe AI anything                                    |
| Get instant answers about our products.                    |
| ![icon](https://www.adobe.com/federal/assets/svgs/experience-cloud-logo.svg) What's the difference between Photoshop and Lightroom? |
| ![icon](https://www.adobe.com/federal/assets/svgs/experience-cloud-logo.svg) Recommend a plan for a small business  |
| Ask a question…                                             |
| By using this feature you agree to the [AI Terms](https://www.adobe.com/legal/terms.html). |
```

## Notes

- This block only initializes its chat experience after the visitor has scrolled it near the viewport (or after a 3-second fallback) — the underlying chat widget is a separately-hosted script, not part of the block markup, so previewing may show a brief loading state.
- The block auto-hides itself if the visitor hasn't consented to the relevant cookie group; this is expected privacy behavior, not a bug.
- For any "-only" floating variant, you still must author all 5 rows in order (even if some are left blank) — the rows are read positionally before being discarded.
- Card icons in the default/hero card row are decorative and are hidden entirely in dark-themed variants, which rely on text alone.
- Row positions are hard-coded — do not add extra rows or leave the table short; if a row is entirely missing, later rows shift up and get misinterpreted as the wrong content type.
