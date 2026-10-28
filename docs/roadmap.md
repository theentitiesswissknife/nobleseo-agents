# Roadmap and capability boundary

## Implemented workflows

The plugin includes `keyword-clustering`, `seo-content-briefing`, `gsc-performance-review` and `gsc-visualization`. The first two use a separately configured NobleSEO Research MCP connection. The GSC skills work with exports or an available authorized connector.

Research MCP provides clustering previews/execution, stored clusters/hubs and domain comparisons, SERP/AI research/checkpoints, evidence/recommendations and stored content briefs. Capabilities depend on granted permissions. Reading existing results does not create a run.

## Connection packaging

Automatic MCP connection packaging remains separate from skill installation. Setup reuses each client's registered OAuth configuration, as described in [MCP setup](mcp-connection.md), without changing an existing connection or assuming all installations share endpoint/callback registrations.

## Future capabilities

- Direct GSC/GA4 retrieval needs actual public tools and access controls before a skill can use it. Current GSC skills do not claim this capability.
- Internal-link review needs a public read tool before it can be offered as an MCP workflow.
- Publication needs explicit supported tools and separate authorization; it is outside these research skills.

See [CHANGELOG.md](../CHANGELOG.md) for version history and [CONTRIBUTING.md](../CONTRIBUTING.md) for release checks.
