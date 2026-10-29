# NobleSEO Agents

Skills for AI coding assistants (Claude Code and Codex) from [NobleSEO](https://github.com/theentitiesswissknife). One plugin installs the same skills in both assistants. Research skills use your separately configured NobleSEO MCP connection; analysis skills work with exports or an available data connector.

> **License notice.** No license has been granted yet. All rights are reserved by the NobleSEO rights holder until a license file is added to this repository. You may read the contents here; you may not copy, modify or redistribute them until a license is published.

## What's inside

| Skill | What it does | Needs |
|---|---|---|
| [`gsc-visualization`](plugins/nobleseo/skills/gsc-visualization/SKILL.md) | Turns Google Search Console and GA4 exports (CSV or JSON) into charts: trends, top queries and pages, device shares, position vs CTR, day-by-hour patterns, multi-metric comparisons. | Python 3.10+ with pandas, matplotlib, numpy, seaborn, scipy |
| [`gsc-performance-review`](plugins/nobleseo/skills/gsc-performance-review/SKILL.md) | Diagnoses performance changes and prioritizes actions with evidence and limitations. | GSC exports or an available GSC connector |
| [`keyword-clustering`](plugins/nobleseo/skills/keyword-clustering/SKILL.md) | Reviews clusters, hubs and domain coverage; exports results or runs approved clustering. | NobleSEO Research MCP, `read`, plus `clusterizer.run` for new runs |
| [`seo-content-briefing`](plugins/nobleseo/skills/seo-content-briefing/SKILL.md) | Turns existing SERP/AI evidence and recommendations into a writer brief; optionally prepares a stored brief or runs approved research. | NobleSEO Research MCP; permissions depend on reading, writing or research |
| [`article-generation-and-refresh`](plugins/nobleseo/skills/article-generation-and-refresh/SKILL.md) | Reads scoped native generation options and guides discovered bounded generation or canonical Refresh checkpoints; reports missing execution capabilities. | NobleSEO MCP; `content.read` for options, separately deployed execution tools and consent for paid work |
| [`article-optimization-review`](plugins/nobleseo/skills/article-optimization-review/SKILL.md) | Inspects drafts, compares scores, saves requested revisions and guides discovered Refresh levels through exact cost and human review approval. | Discovered article tools and separate content scopes; optional generation/knowledge/media/analytics scopes |
| [`editorial-coverage-planning`](plugins/nobleseo/skills/editorial-coverage-planning/SKILL.md) | Reviews selected persisted topic placement and covering articles, then proposes a bounded editorial backlog. | Discovered coverage tools and `coverage.read` consent |
| [`internal-link-review`](plugins/nobleseo/skills/internal-link-review/SKILL.md) | Reviews scoped links and evidence, changes a selected plan, simulates proposals or previews/applies exact draft edits. | Discovered link tools; `links.read`; `links.write` for actions; additional `content.write` for draft edits |
| [`review-and-publish`](plugins/nobleseo/skills/review-and-publish/SKILL.md) | Reviews an exact saved article and WordPress target, guides native approval and reads or explicitly verifies canonical publication receipts. | Discovered publication tools, `publish` consent and editor access; article reading needs its own scope |
| [`content-factory-runbook`](plugins/nobleseo/skills/content-factory-runbook/SKILL.md) | Inspects scoped native templates, exact published pipelines and stored run items/action states; keeps execution separate. | Discovered Factory read tools and fresh `factory.read`; project discovery separately needs `read` |

The original Research MCP offers clustering, research and brief tools. This candidate also supports an optional Analytics server increment for persisted GSC query/page reports and CTR opportunities. It requires deployed tools and an explicit `analytics.read` grant; GA4 retrieval is not included. Installing this plugin adds workflow guidance, not permissions or an automatic Google connection. See [MCP setup](docs/mcp-connection.md), [roadmap](docs/roadmap.md) and [changelog](CHANGELOG.md).

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

Other requests:

> Use the keyword-clustering skill to review my existing run, including unclustered terms and missing data. Do not launch a new run.

> Use the seo-content-briefing skill to prepare a local brief from the existing research for my selected cluster. Flag stale or missing sections.

> Use the gsc-performance-review skill to compare these two complete weeks and identify which pages or devices drove the click decline.

New clustering and research runs require an exact preview approved in NobleSEO. A read-only login is sufficient for inspecting existing results, but does not expose execution or brief-write tools.

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
