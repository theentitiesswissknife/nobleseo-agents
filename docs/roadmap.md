# Roadmap and capability boundary

## Implemented workflows

The plugin includes `keyword-clustering`, `seo-content-briefing`, `gsc-performance-review` and `gsc-visualization`. The first two use a separately configured NobleSEO Research MCP connection. The GSC skills work with exports or an available authorized connector.

Research MCP provides clustering previews/execution, stored clusters/hubs and domain comparisons, SERP/AI research/checkpoints, evidence/recommendations and stored content briefs. Capabilities depend on granted permissions. Reading existing results does not create a run.

## Connection packaging

Automatic MCP connection packaging remains separate from skill installation. Setup reuses each client's registered OAuth configuration, as described in [MCP setup](mcp-connection.md), without changing an existing connection or assuming all installations share endpoint/callback registrations.

## Future capabilities

- The local Analytics server increment adds five bounded GSC query/page read tools under `analytics.read`. The GSC review skill has a capability-detected path for them; deployment and fresh consent are separate acceptance gates. Complete property totals, content-decay adapters and GA4 remain future work.
- The local portfolio candidate includes scoped persisted link reads, explicit simulation and versioned inclusion/withdrawal/business approval under fresh `links.read`/`links.write` consent. `internal-link-review` discovers these capabilities; exact application and remaining plan/discovery/export workflows remain required server work. Deployment and native-client acceptance remain pending.
- Publication needs explicit supported tools and separate authorization; it is outside these research skills.

See [CHANGELOG.md](../CHANGELOG.md) for version history and [CONTRIBUTING.md](../CONTRIBUTING.md) for release checks.
