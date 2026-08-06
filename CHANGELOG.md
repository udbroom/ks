# Kitchen Sink Docs — Changelog

Tracks snapshots of `/blocks/` taken on request. Live docs in `/blocks/` are always the current working copy; a version here is a frozen copy made at `snapshots/<version>/` only when asked for.

## v1.0 — 2026-08-04 (baseline)

First snapshot. Captures all 34 block docs as they stand today, including the same-day updates below (folded into this baseline since no earlier snapshot existed to diff against):

- **tabs.md** — added `radio` and `quiet` tab-style variations, plus `dark` (combinable with either), sourced from PR #6340 (Rares Munteanu, 2026-08-03). Documented the new optional leading-paragraph visible label for the `radio` variation.
- **tour.md** — removed the claim that steps show a visible `( 1/3 )` counter; that UI was removed in PR #6356 (2026-07-28).

**Not yet included:** no doc exists yet for the new `roller-carousel` block (PR #6399, 2026-08-04) — flagged as a gap, to be written as its own doc in a future version.
