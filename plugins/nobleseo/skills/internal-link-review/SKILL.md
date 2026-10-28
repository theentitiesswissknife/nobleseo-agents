---
name: internal-link-review
description: Review persisted NobleSEO internal links and selected proposal evidence within an authorized project section. Inspect plan history and application receipts, compare an explicitly requested scoped simulation, and guide exact edits only when supported write tools and authority are discovered.
---

# Review internal links and selected changes

## Requirements

A separately connected NobleSEO MCP server exposing the discovered `links_*` schemas and `links.read` consent for the selected project. Explicit simulation needs `links.write`; draft edits and external CMS writes require their complete discovered permissions and supported workflows. Skill installation does not grant scopes, bind a site, deploy tools or establish proposal quality. Discover capabilities first. If these tools are absent, use an authorized export for a local review and identify the missing evidence.

## Establish scope and stored evidence

Use `links_get_project_snapshot` to confirm the explicit project, connected site and path binding. Do not infer access to a whole property from a connected domain. Retain the source snapshot and opaque plan version. Both endpoints must be visible within the selected project section. Counts, relations and application statuses describe that permitted projection; omitted sibling sections are not zero-valued observations.

Read `links_list_edges` for existing links, optionally selecting a permitted page or mapped article ID and direction. Use `links_get_opportunities` for persisted candidates, `links_get_plan` for canonical plan states and `links_get_proposal` for exact selected evidence. Read `links_get_page_relations` for a selected page and `links_get_item_history` for visible item history. Follow cursors to completion; restart on changed snapshots instead of concatenating inconsistent pages. Respect size/time refusals without silently splitting an oversized operation.

These reads do not discover opportunities, rebuild graphs, repair legacy data or reconcile plan state. Missing persisted candidates do not prove that no useful links exist. Missing cached analysis or binding needs the owning product's supported setup workflow, not an improvised URL fetch, private route or organization-wide query.

## Assess a proposal

Keep source/target URLs, mapped article IDs, proposal/item ID, revision, observed status, freshness, review state, apply state and evidence together. Distinguish existing observed links, saved recommendations, user-approved plan items and agent-authored suggestions. Source passage text is a bounded projection; truncated text or stripped markup is not an exact edit payload. A stale or missing passage needs renewed evidence before application.

Native business approval does not establish experimental quality qualification or authorize execution. Preserve stated quality holds and scope; do not activate a held experiment, relax an anchor rule or expand its corpus from a read result. A deterministic simulation score is a model result, not measured traffic uplift or proof of editorial relevance. An eligible-for-native-application field reports owning-service state, not permission to write.

## Optional explicit simulation

Only when requested, call discovered `links_simulate` with the exact current plan version/source snapshot, explicit item selection, scope and a fresh request ID. It persists a bounded, expiring simulation through the existing calculation core. It does not generate proposals, approve items or write a CMS. Read its stored sections with `links_get_simulation`, following cursors. Results cover the permitted nodes/edges/items; do not compare them as full-property scores or assume site-wide priority goals were included.

Reuse the same request ID only for an identical retry. Changed arguments require a new request. An expired/missing result does not authorize automatic recomputation. Changed input bindings withhold stale results; explain the change and request a new explicit simulation when needed.

## Continue through supported writes

When explicitly requested and discovered, use `links_set_included` to change one item's future-batch selection, `links_withdraw_item` to withdraw it, `links_approve_item` for the exact saved business candidate or `links_unapprove_item` to return it to pending. Supply a stable request ID and current plan/source bindings and item revision from a fresh read. Approval also requires the selected insertion identity/revision and exact evidence hash; do not approve a missing, truncated or stale candidate from an inferred replacement. These operations preserve canonical state/history and do not run discovery or apply/remove a live link. Retry identical arguments with the same request ID; a replay returns the immutable command receipt, so read the plan for current state. Changed arguments need a distinct request ID and explicit selection. A conflict requires reading current state and reconsidering the requested change, not blindly substituting newly read versions. Do not turn an approval request into automatic execution.

For a requested edit, discover the exact preview/application schemas and their full authority before acting. Plan edits or business approvals need current item/plan versions. Do not substitute simulation, a saved recommendation or business approval for an exact application preview. If `links_preview_apply` or `links_apply` is missing, report that the application workflow remains unavailable in this candidate; provide a reviewable proposal without inventing a tool or writing through private routes.

A supported preview must bind selected proposals, current source revisions and an exact insertion/removal diff. Apply only that approved selection and retain the owning per-source receipt. A NobleSEO draft save and a WordPress write are separate effects; a link scope alone never grants external publication. Do not ask for raw CMS credentials in a tool argument. Broader publication/delivery authority must be enforced by the supported connection and owning service.

Use `links_get_application` to read a supported existing receipt. Report each visible source's outcome, partial failure and reconciliation requirement. Reading the receipt does not retry, recover or verify the live CMS. Do not declare an interrupted or uncertain write successful, and do not repeat it blindly.

Return the selected scope, observed evidence, proposed edits, unresolved quality/freshness conditions and concrete next action. Keep author suggestions separate from persisted product decisions.
