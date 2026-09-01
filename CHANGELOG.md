# Kitchen Sink Docs — Changelog

Tracks snapshots of `/blocks/` taken on request. Live docs in `/blocks/` are always the current working copy; a version here is a frozen copy made at `snapshots/<version>/` only when asked for.

## v1.1.2 — 2026-09-01

Two new block docs, a round of upstream corrections (including a "GTK" video-flags reference table added to every video-capable block), and three site/tooling improvements to the index itself.

**New blocks:**

- **globe-gallery.md** and **roller-carousel.md** — added, filling the "not yet included" gap flagged back in v1.0. Globe Gallery was later restructured from 4 to 5 rows (PR #6477) to add on-screen pause/resume and rotate controls; Roller Carousel picked up an SVG-icon authoring note (VQA changes, 2026-08-19–24).

**Upstream corrections:**

- **New "GTK: Video Flags and Attributes" reference table**, added to all 10 video-capable blocks (hub-hero, explore-card, elastic-carousel, rich-content, split-aside-grid, section-metadata, router-marquee, social-proof, side-by-side, offer-hero) — documents `autoplay`, `autoplay1`, `viewportplay`, `hoverplay`, and the new `_hide-controls` flag. Independently confirms the mechanics behind the v1.1 "Video gotcha" notes.
- **Corrected the video hash delimiter**: multiple flags are joined with additional `#` marks (e.g. `#autoplay#viewportplay`), not `|` — `|` is already reserved for separating a poster image's embedded video URL from its alt text. Updated everywhere the old `|`-joined example appeared.
- **Elastic Carousel** flags that its own mobile-autoplay/hover playback is driven by block-specific code, independent of the hash flags above — worth confirming against current code if a slide's autoplay/hover isn't behaving as documented.
- Assorted smaller upstream fixes: Hub Hero (video in `slides-3` image grid, accessibility label deployment differences), Offer Hero (dark-mode card treatment corrected, PR #6554), Router Marquee (Korean-locale free-trial CTA override), Section Metadata (`bento` + `body-color-solid`, masonry + stagger pairing), Side by Side (`card-stacked` icon badge), Split Aside Grid (reduced-motion support), Tabs (`radio` accessibility fix, Up/Down keyboard nav), Rich Content (quote-detection locale coverage, `spacing-<size>` modifier for `media`, deployment-availability wording), Product Marquee Grid (merch/pricing card), Comparison Table C2, News, Region Nav, Global Navigation, PDF Space, Tour (each a small documentation correction or clarification).

**Site improvements** (not doc content — the index tooling itself):

- Main content column now uses full width instead of a fixed 780px cap.
- Every block now has a clean, shareable URL (`/<slug>`, e.g. `/comparison-table-c2`), with browser back/forward support; `vercel.json` updated with a catch-all rewrite so the deployed site resolves these paths.
- Every heading now gets a stable, slugified `id` for deep-linking (e.g. `/comparison-table-c2#variations`).

## v1.1 — 2026-08-13

Pulled in upstream Milo changes since v1.0, plus a new authoring gotcha added across all video-capable blocks.

**Upstream content changes:**

- **hub-hero.md** — added the `slides-3` variation (an alternate 3-slide/3-column layout, vs. the default 4-slide/5-column grid) and a `dark` knockout color treatment, from PR #6406 (Denys Fedotov, 2026-08-05). Row-count table now documents both layouts side by side.
- **side-by-side.md** — documented a fix so `reverse`/`equal`/`featured` now work correctly when combined with mobile/tablet/desktop viewport-override rows; previously the combination could silently fall back to the default card layout instead of applying the variant. Commit [`c025f84`](https://github.com/adobecom/milo/commit/c025f84) — Ratko Zagorac, 2026-08-07.
- **product-marquee-grid.md** — the CTA link can now also be an unwrapped Merchandising-at-Scale (M@S) commerce link (recognized via its `data-wcs-osi` attribute), in addition to the existing bold/italic button syntax. MWPW-203872 — Narcis Radu, 2026-08-11.

**New across all video-capable blocks** (hub-hero, explore-card, elastic-carousel, rich-content, split-aside-grid, section-metadata, router-marquee, social-proof, side-by-side, offer-hero, plus cross-references on modal.md/modal-metadata.md): a "Video gotcha" Notes bullet — pair the video link with an adjacent poster image, and use the `autoplay|viewportplay` hash combo (not `#autoplay` alone) so playback is scroll-gated instead of finishing during page load. Confirmed against Milo's actual `decorate.js`/`getVideoAttrs` source, not just observed behavior.

**Housekeeping:** consolidated each block's duplicate plain-text description paragraph into its Quick Summary blockquote (the blockquote is now the single source for that summary text) — no content change, just removes redundant repetition under the `> **Quick summary:**` line.

## v1.0 — 2026-08-04 (baseline)

First snapshot. Captures all 34 block docs as they stand today, including the same-day updates below (folded into this baseline since no earlier snapshot existed to diff against):

- **tabs.md** — added `radio` and `quiet` tab-style variations, plus `dark` (combinable with either), sourced from PR #6340 (Rares Munteanu, 2026-08-03). Documented the new optional leading-paragraph visible label for the `radio` variation.
- **tour.md** — removed the claim that steps show a visible `( 1/3 )` counter; that UI was removed in PR #6356 (2026-07-28).

**Not yet included:** no doc exists yet for the new `roller-carousel` block (PR #6399, 2026-08-04) — flagged as a gap, to be written as its own doc in a future version.
