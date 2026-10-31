# Codex

## Install

```bash
codex plugin marketplace add theentitiesswissknife/nobleseo-agents
codex plugin add nobleseo@nobleseo-agents
```

Check with `codex plugin list`.

For clustering and briefs, also configure the [NobleSEO MCP connection](mcp-connection.md). Keep an existing working connection rather than adding a duplicate.

## Update

```bash
codex plugin marketplace upgrade
```

## Use

Ask for a chart and name your data file, or call the skill directly: `Use $gsc-visualization to chart daily clicks from gsc-performance.csv`. The skill needs Python 3.10+ with pandas, matplotlib, numpy, seaborn and scipy.

- `Use $keyword-clustering to review my existing run and export a complete keyword map.`
- `Use $seo-content-briefing to build a local brief from existing research, without starting another run.`
- `Use $gsc-performance-review to diagnose the click change in these GSC exports and prioritize the next checks.`

A read-only grant does not expose execution tools. New clustering needs `clusterizer.run`, stored brief creation needs `brief.write`, new research needs `research.run`, and recommendation edits need `research.curate`. Request only the permissions needed for the intended workflow.

## Troubleshooting

- **"No module named …"** — install the missing package (`python -m pip install pandas matplotlib numpy seaborn scipy`).
- **"Column … not found"** — ask Codex to read the file header and use the exact column names.
- **Remove** — `codex plugin remove nobleseo@nobleseo-agents`.
