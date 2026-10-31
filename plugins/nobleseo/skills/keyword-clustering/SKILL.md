---
name: keyword-clustering
description: Use NobleSEO's connected MCP Clusterizer to group keywords into clusters and hubs, inspect existing runs, compare domain coverage, and export a keyword map. Use for keyword clustering and for reviewing the quality of an existing NobleSEO clustering result.
---

# Keyword clustering with NobleSEO

## Requirements

A connected NobleSEO Research MCP server and an authorized project. Reading existing runs requires `read`; creating a run also requires `clusterizer.run`. Tool prefixes vary between clients: discover the tools by their names below. If they are unavailable, explain the missing connection or scope; do not substitute invented clusters or a private API call.

## Select the work

Read `get_context` and `list_projects` and resolve the user's project, country/market and language. If the server offers `nobleseo://capabilities` or `nobleseo://workflows/cluster-keywords`, use them for current capabilities and workflow details. A connected account does not necessarily authorize every project or operation.

For an existing run, use `clusterizer_list_runs`, `clusterizer_get_run` and `clusterizer_get_workspace`. Reading or exporting a result does not require starting a new run. Select by the user's run/project information; do not silently choose the first project.

For a new run:

1. Read the supplied keyword list. Trim and normalize whitespace, remove exact duplicates, and report original and retained counts. Keep meaningful variants, punctuation and spelling differences. Never silently discard rows to fit a limit.
2. Inspect `clusterizer_preview_run`'s live input schema. Its current contract accepts 2–100 unique keywords per run; a larger input needs an explicitly agreed subset or batching plan. Independent batches cannot establish clusters across batch boundaries. The live schema takes precedence over this documented limit.
3. Resolve the run name, market/language and requested options. Preserve server defaults unless the user chooses otherwise; do not automatically relax clustering thresholds because a result has many unclustered terms.
4. Call `clusterizer_preview_run` with a new stable UUID `request_id`. Retain the exact normalized input, request ID and returned approval ID. Display the approval URL, expiry, keyword count, work limits, cache observations and cost/credit estimate. A null or unknown estimate is unknown, not zero; observed cache reuse is not a guaranteed discount. If the user set a monetary cap and the preview cannot establish or enforce it, stop before execution and explain that limit.
5. Wait for the user to finish approving this exact preview in NobleSEO. Opening the link, completing OAuth consent or a chat message saying "approved" is not proof that the action approval was saved. The action page must report `Preview status: approved`.
6. Before the first create call, replay `clusterizer_preview_run` with the exact original plan inputs and the unchanged `request_id`. Require the same `approval_id` and `input_digest`, `status: approved`, and an expiry still in the future. This observes the original approval; do not generate another request ID. If pending, show the same link and wait rather than calling create or looping. If expired, consumed or changed, reconcile the reported state. Only after this check call `clusterizer_create_run` once with identical plan inputs, omitting `request_id` and adding the verified `approval_id`. Do not approve on the user's behalf or change account settings.
7. Preserve the receipt and `run_id`. Poll `clusterizer_get_run` at a modest interval, for example 30 seconds, until terminal status or a bounded wait limit. If waiting must end, return the run ID and last observed state. After a timeout or unclear creation response, reconcile the existing run/receipt before any new execution; do not replay its pre-execution preview or create a new approval. If the server reports `provider_outcome_unknown`, stop for reconciliation.

Expired approval, changed inputs and an explicitly requested new run require a new preview and approval. A failed run is not authorization to launch another.

## Read and assess the result

Follow every `next_cursor` from `clusterizer_get_workspace` until null. Its rows can mix hubs, clusters and keyword members: join them by IDs, not row order. If a cursor reports a changed snapshot, restart the traversal rather than combining versions. If output is too large, reduce the page limit without dropping rows. Retain provenance and warnings.

Report run status, market/language, input count, clustered and unclustered counts, clusters and hubs. Reconcile counts with the run summary and identify incomplete data instead of silently forcing them to match.

Produce a useful keyword map: hub, cluster ID, primary keyword, member keywords, available volume/intent and suggested next action. Keep the source clustering intact. Flag questionable groupings, fragmented near variants and major unclustered terms as review candidates. Suggested merges, splits or article ideas are editorial proposals, not persisted changes or proof of ranking potential.

Volumes can be partially covered. Preserve nulls and coverage counts; never turn missing volume, CPC, difficulty or rank into zero. Do not add hub totals to their child-cluster totals or treat summed keyword volumes as unique demand.

For requested competitor comparisons, use `clusterizer_compare_domains` with the selected domains and optional cluster/hub filters, within its live schema limits. Follow pagination. Missing rank means absent from the stored observations, not necessarily unindexed or unranked everywhere. These are stored SERP observations, not GSC clicks.

## Deliver and continue

Use `clusterizer_export_run` for JSON or CSV and follow its cursor through the full export. Assemble CSV pages with one header, preserving escaping and values; check the exported row count. Save outputs to the user's workspace and include run identity and data limitations in the accompanying summary.

If the user wants a writer brief for a selected cluster, preserve `run_id`, `cluster_id`, project and market/language and use the `seo-content-briefing` skill if available. Preparing a brief persists state even when no research provider is called; creating research needs its own preview and approval. This skill does not publish content or modify the stored clustering through unsupported operations.
