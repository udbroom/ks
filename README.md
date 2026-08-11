# Kitchen Sink Docs

Documentation for Milo/Kitchen Sink blocks — one Markdown file per block, describing authoring instructions, variations, and gotchas for content authors.

## Structure

- `blocks/` — the current, working copy of each block's doc (34 blocks).
- `snapshots/` — frozen copies of `blocks/` taken on request, versioned (e.g. `snapshots/v1.0/`). See [CHANGELOG.md](./CHANGELOG.md) for what changed in each snapshot.
- `kitchen-sink-index.html` — a generated index page linking all block docs.
- `.kitchen-sink-index-tools/` — scripts that generate the index:
  - `convert.py` — converts the block docs into `blocks_data.json`.
  - `build_html.py` — builds `kitchen-sink-index.html` from `blocks_data.json`.

## Regenerating the index

```bash
python3 .kitchen-sink-index-tools/convert.py
python3 .kitchen-sink-index-tools/build_html.py
```
