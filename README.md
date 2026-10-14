# NobleSEO Agents

Skills for AI coding assistants (Claude Code and Codex) from [NobleSEO](https://github.com/theentitiesswissknife). One plugin installs the same skills in both assistants.

> **License notice.** No license has been granted yet. All rights are reserved by the NobleSEO rights holder until a license file is added to this repository. You may read the contents here; you may not copy, modify or redistribute them until a license is published.

## What's inside

| Skill | What it does | Needs |
|---|---|---|
| [`gsc-visualization`](plugins/nobleseo/skills/gsc-visualization/SKILL.md) | Turns Google Search Console and GA4 exports (CSV or JSON) into charts: trends, top queries and pages, device shares, position vs CTR, day-by-hour patterns, multi-metric comparisons. | Python 3.10+ with pandas, matplotlib, numpy, seaborn, scipy |

**Planned:** a connection to the NobleSEO MCP server (signed in with your NobleSEO account) and two skills built on it — `keyword-clustering` and `seo-content-briefing`. See [docs/roadmap.md](docs/roadmap.md). They are not available yet; released items appear in [CHANGELOG.md](CHANGELOG.md).

## Install

### Claude Code

```
/plugin marketplace add theentitiesswissknife/nobleseo-agents
/plugin install nobleseo@nobleseo-agents
```

### Codex

```bash
codex plugin marketplace add theentitiesswissknife/nobleseo-agents
codex plugin add nobleseo@nobleseo-agents
```

More detail, updates and troubleshooting: [docs/claude-code.md](docs/claude-code.md) · [docs/codex.md](docs/codex.md).

## Use

Ask your assistant for a chart and point it at your export, for example:

> Chart daily clicks and impressions from `gsc-performance.csv`, with average position on a second axis.

The skill picks the chart script, checks the column names and saves a PNG into a `charts/` folder in your working directory. Everything runs on your computer; see [PRIVACY.md](PRIVACY.md).

## Repository layout

```
.claude-plugin/marketplace.json     Claude Code marketplace
.agents/plugins/marketplace.json    Codex marketplace
plugins/nobleseo/                   the plugin (manifests for both assistants + skills/)
docs/                               install and usage guides, skill publication checklist
scripts/                            repository checks used by CI
tests/fixtures/                     synthetic data for the chart smoke test
```

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
