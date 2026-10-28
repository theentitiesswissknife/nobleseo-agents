---
name: editorial-coverage-planning
description: Review persisted NobleSEO topic placement for selected project articles, identify visible coverage evidence and propose a focused editorial backlog. Use for topic coverage planning, existing covering-article lookup and evidence-backed brief selection without automatic classification or generation.
---

# Plan from persisted topic coverage

## Requirements

A connected NobleSEO MCP server exposing `coverage_get_map`, `coverage_get_content_placement` and `coverage_find_covering_content`, with explicit `coverage.read` consent for the selected project. Article discovery may additionally require `content.read`; existing research discovery uses `read`. Stored briefs and paid workflows require their own scopes and approvals. Discover the current schemas and capability flags rather than assuming installation enabled coverage.

## Select a bounded portfolio

Resolve the authorized project and article IDs. Use the current schema's explicit selection limit. Do not silently split an oversized selection or substitute all organization articles. If coverage tools are absent or disabled, use an authorized export for a local analysis and explain the missing coverage evidence.

Read `coverage_get_map` for the selected articles and `coverage_get_content_placement` for details. Follow every cursor and preserve the snapshot bindings. A changed snapshot requires a restart; do not combine pages from different snapshots. The map contains topics bound to selected/visible articles, not the entire organizational topic space. Report that scope so a missing row is not mistaken for proof that a topic is absent everywhere.

## Interpret placement and evidence

Keep topic identity, article identity, classification origin and hidden state together. A manual choice remains a user choice; an automated placement remains a classification. Preserve hidden/manual placement rather than presenting it as a new gap. Search demand, search performance and editorial coverage are different measurements. Do not invent search volumes or infer rankings from placement alone.

Use `coverage_find_covering_content` only for visible selected node IDs. Retain the canonical observed coverage evidence, target article IDs and URLs. An existing draft can cover a topic without having a published URL. No covering result means no supported covering result within the authorized projection; it does not prove that no article anywhere covers the topic.

## Propose the next action

Produce a short backlog with the visible evidence, the affected article/topic and a proposed action such as revising a draft, reviewing an adjacent covering article or preparing a new brief. Label inferred gaps as hypotheses when evidence is incomplete. A persisted `new_article` placement is a candidate for review, not authorization to generate content.

For a user-selected topic, continue through the existing briefing workflow, retaining project, content, node and snapshot identities. Preparing a stored brief needs a requested write. Research or generation needs a separately discoverable bounded preview and exact approval; never classify, refresh or run a provider call just to fill an empty map.

Placement changes remain unavailable unless a separately qualified write tool with concurrency protection is discovered. Do not imitate the product's organization-wide routes or replace a manual placement from a local recommendation. Link application and external publication require their own separately authorized workflows.

Report the selected scope, observations, editorial hypotheses, pending decisions and missing evidence. Do not claim complete project coverage after a partial page or a size/timeout refusal.
