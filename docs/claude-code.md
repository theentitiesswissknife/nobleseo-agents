# Claude Code

## Install

```
/plugin marketplace add theentitiesswissknife/nobleseo-agents
/plugin install nobleseo@nobleseo-agents
```

Restart Claude Code if the skill does not appear. Check with `/plugin` that `nobleseo` is enabled.

## Update

```
/plugin marketplace update nobleseo-agents
/plugin update nobleseo@nobleseo-agents
```

## Use

Ask for a chart and name your data file. The `gsc-visualization` skill needs Python 3.10+ with pandas, matplotlib, numpy, seaborn and scipy; the assistant checks this and asks before installing anything.

## Troubleshooting

- **"No module named …"** — install the missing package in the Python that Claude Code runs (`python -m pip install pandas matplotlib numpy seaborn scipy`).
- **"Column … not found"** — the column names in your file differ from the ones requested; ask the assistant to read the file header first.
- **Remove** — `/plugin uninstall nobleseo@nobleseo-agents`.

## Research and performance workflows

Configure the [NobleSEO MCP connection](mcp-connection.md) for keyword clustering and content briefs, or reuse your existing connection. Installing skills does not grant project access or additional permissions.

Ask to use `keyword-clustering` to review an existing run, `seo-content-briefing` to prepare a brief from existing evidence, or `gsc-performance-review` to diagnose GSC exports. New clustering/research needs a browser-approved preview; GSC retrieval needs a separate available connector.
