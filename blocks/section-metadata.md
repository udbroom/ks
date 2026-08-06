# Section Metadata

> **Quick summary:**
> - A hidden key/value configuration table (never rendered visibly), placed at the bottom of a Section to control section-level behavior — not a visual block. Each row is a `key | value` pair, or `key | value1 | value2 | value3` for per-viewport values.
> - Six recognized keys: `style`, `layout`, `background`, `masonry`, `anchor`, `images`.
> - `style`/`layout` class values are organized further down into grouped tables by purpose (visual/structural, multi-block grid, bento, scroll-animation, single-block-only). Not every key/class is available in every deployment — see the Availability notes.
> - A dedicated "Cross-block interactions" section covers how other blocks react to specific classes — worth checking before you add a class expecting an effect elsewhere.

## Authoring instructions

Section Metadata is a table where **the first cell of each row is a key name** and the remaining cell(s) in that row are its value(s). The block itself is hidden (`display: none`), so none of this renders visibly.

| Row (key) | Content |
| --- | --- |
| `style` | One or more CSS class names, comma-separated (e.g. `divider, rounded-corners`), applied directly to the containing section. Put 1 cell to apply the same classes at all breakpoints, or 2 cells (mobile \| tablet+desktop) or 3 cells (mobile \| tablet \| desktop) to swap which classes are active per breakpoint (classes are added/removed live as the viewport changes). See "Which values go under which key" and "Multi-block grids" below. |
| `layout` | Same mechanism and cell structure as `style` (also class names, same 1/2/3-cell viewport logic) — functionally identical, just a separate key so authors can organize layout-only classes separately from cosmetic ones if they want. Using either accomplishes the same thing; don't use both on the same section. |
| `background` | One cell per background layer. Each cell holds either an image, a video link, or plain color text (e.g. `#1E1E1E`). 1 cell = same background at all sizes. 2 cells = mobile \| tablet+desktop. 3 cells = mobile \| tablet \| desktop. Adds a background-present flag to the section and inserts an absolutely-positioned background layer behind the content. For an image cell, a second line of text under the image (e.g. `left, top`) sets its focal point/object-position. |
| `masonry` | Defines the grid span of each direct child block in the section, for use with `bento` or masonry grids. Value is written as one line per child block, `span N` (or comma-separated spans per row for multi-column masonry rows), e.g.: line 1 `span 8`, line 2 `span 4, span 4` — also accepts `full width`/`half width`. Use 1 cell for a fixed layout, or 2–3 cells for mobile/tablet/desktop variants (same viewport rules as `style`). Adds a masonry-layout class to the section. Like `product-grid`, this works with *any* block placed in the section — it's not tied to a specific one. It's most commonly used to arrange a mix of differently-sized promo/card blocks ([Base Card](./base-card.md), [Explore Card](./explore-card.md), [Product Marquee Grid](./product-marquee-grid.md), and similar) into an uneven bento-style layout rather than a strict even grid. |
| `anchor` | A single word/phrase used as the section's jump-to `id` (lowercased, spaces converted to hyphens) — pair with [Rich Content](./rich-content.md)'s `jump-link` variant or any in-page anchor link. |
| `images` | A comma-separated list of picture-optimization hints applied to every `<picture>` in the section: a resolution multiplier (`1x`, `2x`, `3x`) and/or an encoding hint (`photography` → AVIF, `product` → WebP). Use `off` to explicitly skip this optimization. |

These six keys (`style`, `layout`, `background`, `masonry`, `anchor`, `images`) are recognized everywhere this block is used. Any other key/value row is silently ignored by this block's own code — though other blocks may read their own keys directly out of the same table (see "Custom keys read by other blocks" below).

## Variations

Section Metadata has no author-facing modifier classes on the block itself — it is always just `Section Metadata`, and all behavior comes from which key rows you include.

### Which values go under which key

Only **`style`/`layout`** accept freeform CSS class names — that's what the rest of this section documents. The other four keys each have their own fixed value type instead of a class list:

| Key | Value type | Where documented |
| --- | --- | --- |
| `style` / `layout` | CSS class names, grouped below by what they do | This section |
| `background` | Image, video, or color | Authoring instructions table above |
| `masonry` | Grid-span sizes (`span N`, `full width`, `half width`) | Authoring instructions table above |
| `images` | Optimization-hint keywords (`1x`/`2x`/`3x`, `photography`/`product`, `off`) | Authoring instructions table above |
| `anchor` | Plain text (becomes the jump-link id) | Authoring instructions table above |

### `style` / `layout` classes, grouped by purpose

Any class name is technically accepted (it's just added to the section), but only these have matching CSS. A typo (e.g. `countainer`) is silently accepted and does nothing — spelling isn't validated. All of the classes below go under **either** `style` or `layout` — the two keys are interchangeable (see Notes), so which one you pick doesn't change anything.

**Visual & structural** — standalone, no pairing required:

| Class | Effect | Availability |
| --- | --- | --- |
| `divider` | Bottom border line under the section. | All deployments |
| `vertical center` | Centers content vertically within the section. | All deployments |
| `rounded corners` / `rounded corners top` / `rounded corners bottom` | Rounds all 4 corners / only top / only bottom. | All deployments |
| `container` | Makes the section a grid container; pair with a `grid width 6`/`8`/`10` class to constrain its content width. | All deployments |
| `grid width 6` / `8` / `10` | Constrains grid content width to 6/8/10 of 12 columns (desktop only). Pairs with `container`. | All deployments |
| `scrim` | Adds a dark gradient overlay over the section's background image/video (gradient direction/stops are cosmetic details that vary slightly). | All deployments |

**Multi-block grid** — must be combined together (full detail in "Multi-block grids" below):

| Class | Effect | Availability |
| --- | --- | --- |
| `product grid` + a `-up` class | Turns the section into a multi-block grid. | All deployments |

**Bento layout:**

| Class | Effect | Availability |
| --- | --- | --- |
| `bento` | Enables a bento-style grid layout; several other blocks (e.g. [Explore Card](./explore-card.md), [Rich Content](./rich-content.md)'s `grid-full-width`) have extra CSS for sections carrying this class. | Most deployments |
| `bento` + `stack-mobile` (together) | Loads a sticky, depth-scaled mobile card-stack scroll animation for a bento section's child cards (e.g. [Explore Card](./explore-card.md)) with a [Rich Content](./rich-content.md) title pinned above it. Only active below the 768px breakpoint; respects reduced-motion. | Only some deployments |

**Scroll-animation family** — part of Milo's shared scroll-driven section-transition system; this block mostly just passes these through rather than implementing the animation itself (see "Cross-block interactions" below for what actually reacts to them):

| Class | Effect | Availability |
| --- | --- | --- |
| `parallax move up fast` | Triggers a scroll-linked "move up" transition on the section; see Cross-block interactions for the one block that also reacts to it directly. | All deployments |
| `parallax garage door reveal` / `parallax double garage door` | Scroll-driven "garage door" reveal transitions between sections. | All deployments |
| `parallax video garage door` | A variant of the above, paired with [Rich Content](./rich-content.md)'s `media` variant on the same section — no effect without that variant also present. | Only where Rich Content's `media` variant is available (see [rich-content.md](./rich-content.md)) |
| `parallax stagger ltr` / `parallax stagger rtl` | Staggers the scroll-in of a section's child items left-to-right or right-to-left; pairs with the multi-block grid classes above (see "Multi-block grids"). | All deployments |

**Narrow, single-block-only values** — not general-purpose, only meaningful with one specific block:

| Class | Effect | Availability |
| --- | --- | --- |
| `base card section` | Forces a single-column mobile layout with extra gap for a section holding multiple [Base Card](./base-card.md) blocks. | Wherever Base Card is used |
| `region selector text` | Used only inside the region/locale-selector [Modal](./modal.md) fragment to tighten its intro-copy padding/typography. Don't reuse it elsewhere. | Wherever that Modal fragment is used |

### Multi-block grids: `product-grid` + `two-up` / `three-up` / `four-up` / `six-up`

To arrange **more than one block side-by-side in the same section** as an even-column grid instead of the default stacked layout, add both a grid-mode class and a column-count class to the same `style`/`layout` row:

| Class | Effect |
| --- | --- |
| `product-grid` | Turns the section into a CSS grid with stretched, equal-height rows. Does nothing on its own — must be paired with one of the column-count classes below. |
| `two-up` | 2 columns (tablet width and up; collapses to 1 column on mobile). |
| `three-up` | 3 columns. |
| `four-up` | 4 columns. |
| `six-up` | 6 columns. |
| `fill-last-row` | Pairs only with `two-up`: a leftover single block in the last row spans the full row width instead of sitting alone in one column. |

There's no `five-up` — only two/three/four/six column counts are defined, and this behaves identically everywhere the block is used.

Optionally add `parallax-stagger-ltr`/`parallax-stagger-rtl` to the same row for a staggered scroll-in animation whose per-column timing automatically matches the `-up` count you picked. In most deployments, this block's own code also computes the per-item stagger index locally to drive that timing; in the simplest deployment there's no such code — stagger there relies entirely on the shared animation system reading DOM position, with nothing computed here.

**Which blocks this is commonly used with:** `product-grid` + a `-up` class works with *any* block — it's positional, not tied to a specific block. In practice it's most often used to arrange several small, self-contained promo/card-style blocks side by side (e.g. [Base Card](./base-card.md), [Explore Card](./explore-card.md), [Product Marquee Grid](./product-marquee-grid.md)), since those are sized to sit comfortably in an even column.

**Gotcha — two blocks reuse these exact class names internally, unrelated to this system:** [News](./news.md) and [Quick Actions](./quick-actions.md) both apply `two-up`/`three-up`/`four-up`/`six-up` (or a subset) to their *own internal* item/tile grid automatically, based on item count or viewport width — this has nothing to do with Section Metadata's `product-grid` system and isn't affected by adding these classes here. If you're troubleshooting a News or Quick Actions layout and see these class names, check that block's own doc ([news.md](./news.md) / [quick-actions.md](./quick-actions.md)) rather than this one.

## Example

```
| Section Metadata |
| --- | --- | --- |
| style | rounded corners | container |
| background | #000000 | ![Desktop background](/media/hero-bg.jpg) |
| anchor | Featured products |
```

Masonry example, with different spans per breakpoint:

```
| Section Metadata |
| --- | --- |
| masonry | full width, half width, half width | span 4, span 4, span 4 |
```

Multi-block grid example — 3 blocks arranged as an even 3-column grid, with scroll-in stagger:

```
| Section Metadata |
| --- |
| style | product grid, three up, parallax stagger ltr |
```

(Place this Section Metadata at the bottom of a section that also contains three visual blocks — they'll tile into 3 equal columns instead of stacking.)

## Notes

- The `style`/`layout` classes only take effect together with matching CSS — a typo silently does nothing.
- For `background`, plain text with no image/video in that cell is treated as a CSS color value — an empty cell is simply skipped, it does not clear a previously inherited background.
- `masonry`'s span list is matched to the section's other blocks **in DOM order**, excluding this Section Metadata block and any auto-generated background container — miscounting blocks (e.g. forgetting a hidden metadata block further up) will misalign spans to the wrong block.
- Multi-column `style`/`background`/`masonry` rows switch live as the browser is resized (wired to media-query listeners), so you can preview the breakpoint switch by resizing the window rather than needing separate device tests.
- `product-grid` by itself does nothing — it must be combined with a `two-up`/`three-up`/`four-up`/`six-up` class in the same row, or the section falls back to its default stacked layout.
- The column count on mobile is always effectively 1 (the grid collapses to a single column below the tablet breakpoint) regardless of which `-up` class you chose — the `-up` class only controls tablet/desktop column count. This is identical everywhere the block is used.
- Key matching is case-insensitive and whitespace-trimmed (e.g. `Background` and `background` both work), but must otherwise match exactly — `back ground` will not.
- `style` and `layout` are functionally identical (both call the same class-toggling code); they exist as two keys purely so authors can separate concerns.
- Video gotcha (`background` key): pair the video link with its poster image as two adjacent cells/lines — Milo grabs the poster from whichever image sits next to the video link, and won't show one otherwise. For the background video to autoplay only while scrolled into view (instead of finishing during page load), the video link's hash needs both `autoplay` and `viewportplay`, e.g. `#autoplay|viewportplay`. Using `#autoplay` alone plays the video immediately on page load — by the time the section is visible it has already finished, so visitors just see its frozen last frame.

### Cross-block interactions

Some other blocks have their own CSS/JS tied to a specific `style`/`layout` class on the section:

| Class | Block | Effect |
| --- | --- | --- |
| `parallax move up fast` | [Router Marquee](./router-marquee.md) | If the section *immediately after* a Router Marquee carries this class, the marquee repositions its bottom nav-card controls to make room as that section animates up over it. |
| `parallax move up fast`, `parallax garage door reveal` | [Offer Hero](./offer-hero.md) | Suppresses Offer Hero's own `rounded-corners-bottom` treatment when either is also present, to avoid clipping during the scroll transition. |
| `parallax video garage door` | [Rich Content](./rich-content.md) | Enables a scroll-driven "garage door" reveal of the media, only when combined with Rich Content's own `media` variant. |
| `bento` | [Explore Card](./explore-card.md), [Rich Content](./rich-content.md) (via `grid-full-width`) | Extra spacing/sizing rules specific to those blocks when placed in a bento-style section. |
| `bento` + `stack-mobile` | Section Metadata itself (this doc) | Loads the mobile card-stack scroll animation described above. |
| `base card section` | [Base Card](./base-card.md) | Forces single-column mobile layout for a multi-card grid. |
| `region selector text` | [Modal](./modal.md) | Tightens padding/typography for the region-selector modal fragment's intro copy. |

`parallax move up fast`, `parallax garage door reveal`, `parallax double garage door`, and `parallax stagger ltr`/`rtl` are otherwise part of Milo's shared scroll-driven section-transition system — this block mostly just passes the class name through to the section rather than implementing the animation itself. Treat that system as the source of truth for exact scroll-animation behavior beyond what's listed above.

### Custom keys read by other blocks

These rows aren't processed by Section Metadata's own code — the other block reads its own key(s) directly out of the same table.

| Key | Read by | Format |
| --- | --- | --- |
| `carousel` | [Carousel C2](./carousel-c2.md) | Value must match the parent Carousel C2 block's name exactly — tags that section as one of its slides. |
| `starting-marquee` | [Router Marquee](./router-marquee.md) | 1-based slide number — reorders which slide plays first. |
| `tab`, `tab-background`, `link`, `deeplink` | [Tabs](./tabs.md) | Attaches the whole section as a tab panel; see [tabs.md](./tabs.md). |
| `custom-hide` | [Floating CTA](./floating-cta.md) | A CSS selector — hides the floating CTA while the matching element is in view. |
| `expand` | [Comparison Table C2](./comparison-table-c2.md) | `all`, or a comma-separated list of 1-based sub-table numbers — controls which `+++`-separated sub-tables render expanded by default. |
