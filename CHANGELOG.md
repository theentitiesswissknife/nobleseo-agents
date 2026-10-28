# Changelog

All notable changes to this repository. Versions follow semantic versioning; the plugin version in both manifests equals the release tag.

## [Unreleased]

- Add `editorial-coverage-planning` for selected article/topic projections and authorized covering-content lookup, with read-only and missing-capability fallbacks.
- Add conditional article inspection, fixed-reference scoring, requested draft edits and selected-field history restoration guidance in `article-optimization-review`.
- Extend briefing with optional effective-context/document/grounding discovery. Article and knowledge capabilities require separately deployed tools and fresh scope consent; native-client acceptance remains pending.

## [0.2.0] - 2026-10-28

### Added
- `keyword-clustering`: review and export clusters, hubs and domain coverage, or execute an exact approved preview with bounded inputs and replay handling.
- `seo-content-briefing`: reuse evidence, retain all eight recommendation sections and revision bindings, optionally prepare stored briefs or run approved research.
- `gsc-performance-review`: comparable-period diagnostics, correct aggregation, segment contributions and evidence-backed action priorities.
- Synthetic behavioral evaluations and MCP setup instructions for Codex and Claude Code.

### Clarified
- Skill installation and the authenticated MCP connection are separate. The GSC review skill discovers the optional Analytics increment and uses its five read tools only when deployed and granted through `analytics.read`; exports remain supported. GA4 retrieval is not included.
- The former roadmap's larger keyword limit was not a supported contract. Skills inspect the live schema and never silently truncate or batch inputs.
- Privacy documentation covers MCP requests, stored changes and provider-backed work.

## [0.1.0] - 2026-10-15

### Added
- `nobleseo` plugin for Claude Code and Codex, installable from this repository's marketplaces.
- `gsc-visualization` skill: six chart scripts for Google Search Console and GA4 data, reading CSV or JSON. Percent values such as `5.2%` are converted to numbers.

### License
- No license granted yet; all rights reserved by the NobleSEO rights holder.
