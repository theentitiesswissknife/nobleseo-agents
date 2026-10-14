# Codex

## Install

```bash
codex plugin marketplace add theentitiesswissknife/nobleseo-agents
codex plugin add nobleseo@nobleseo-agents
```

Check with `codex plugin list`.

## Update

```bash
codex plugin marketplace upgrade
```

## Use

Ask for a chart and name your data file, or call the skill directly: `Use $gsc-visualization to chart daily clicks from gsc-performance.csv`. The skill needs Python 3.10+ with pandas, matplotlib, numpy, seaborn and scipy.

## Troubleshooting

- **"No module named …"** — install the missing package (`python -m pip install pandas matplotlib numpy seaborn scipy`).
- **"Column … not found"** — ask Codex to read the file header and use the exact column names.
- **Remove** — `codex plugin remove nobleseo@nobleseo-agents`.
