# NobleSEO MCP R2 work plan

Date: 2026-11-01. Status: proposed delivery backlog, not implemented capability or authorization to spend/deploy.

## Baseline and scope

Start from backend main containing `c1f96b383b75b8964e56794b5b04ac6ec1f85ab0`, the published v0.3.0 skills and the [Labs receipt](LABS_BASE_DEPLOYMENT_2026-11-01.md). Verify current HEAD/status and runtime before editing; preserve unrelated work and the historical expansion branch. The base exposes 143 tools and 18 offered MCP scopes. Existing grants are not automatically expanded.

R2 covers advanced single-article generation/Refresh, advanced editor operations, remaining non-WordPress Link Workbench operations and Social Intelligence. Factory, WordPress and Google Analytics remain excluded. Research batches retain their separate owner. A standalone images/infographics product and a new social publishing integration are not added to this scope.

This document is the execution checklist. The [advanced technical specification](specs/ADVANCED_MCP_NEXT_SESSION_SPEC_2026-10-31.md) remains the detailed source for native owners, contracts and acceptance cases. Reuse those owners rather than creating parallel services or stores.

## Recommended delivery order

| Priority | Slice | Deliverable | Exit evidence |
| --- | --- | --- | --- |
| P0 | Base acceptance and scope freeze | Paul's reproducible findings; finite R2 capability matrix | Accepted base scenarios or specific tracked defects; every R2 operation has a declared owner/effect/limit |
| P1 | Advanced generation/Refresh | A selected set of additional native effects and profiles | Real native worker execution with controlled providers, exact approval binding and per-effect outcomes |
| P1 | Advanced editor | Selected grounding, factcheck and quality/schema operations | Review/apply separation, stale/lease/access refusal and native history preservation |
| P2 | Link Workbench | Selected plan editing, export, discovery and exact reversal operations | Both endpoint scopes, invalidated review on edits, bounded exports and original insertion reconciliation |
| P3 | Social Intelligence | Scoped workspaces, ingest/status, collected items and profile selection/activation | Bounded acquisition, original accounting/receipts, cross-project refusal and no implicit generation |

This order prioritizes validating the shipped base and finishing one slice at a time. It is not a commitment to an unlimited combination matrix or a duration estimate.

## P0 — close base feedback and freeze the operation matrix

- [ ] Give Paul the [user guide](MCP_USER_GUIDE.md) and [feedback template](feedback-template.md).
- [ ] Record client/version, plugin/checksum, server revision and actual granted scopes for each test session.
- [ ] Verify existing reads and one explicitly authorized bounded research flow from fresh preview through saved approval, start and original-run observation. Paid testing requires its own approved limits.
- [ ] Triage failures as reproducible engineering defects or concrete access/source/native-readiness prerequisites. Do not treat every refusal as a bug or disguise missing implementation as configuration.
- [ ] Freeze a finite operation matrix before coding. For each row record: existing tool/native action, requested delta, owner, R/W/P effects, roles/scopes, exact source/revision pins, bounds, prerequisites and acceptance cases.
- [ ] Mark each row selected, deferred or blocked with a concrete reason. Do not reopen the historical full-portfolio goal.

R = persisted read; W = native persisted mutation; P = provider/paid execution. Composite operations declare all applicable effects. Reads must not dispatch, provision, reconcile accounting or mutate implicitly.

## P1 — advanced generation and Refresh

- [ ] Inspect the current generation compiler, editorial action service, Refresh owner and native graph; reuse existing outline/media/knowledge seams.
- [ ] Select the additional effects to qualify: bibliography, optional native analyses and specific model/template/voice/source variants. Admit only finite profiles supported by native execution.
- [ ] Bind preview/start to exact effects, sources, versions, work ceilings and credit/provider treatment. Unknown cost stays unknown.
- [ ] Report each effect's actual completion, refusal, failure or uncertainty. Do not infer execution from an options list or admitted counter.
- [ ] Preserve canonical Refresh checkpoints, cancellation, original receipts and uncertain-dispatch recovery.
- [ ] Verify duplicate delivery, changed inputs, source/voice/template drift, optional-effect failure, late acknowledgement and one representative supported composed profile.
- [ ] Update the existing generation skill and evaluations to describe only newly admitted profiles.

## P1 — advanced editor

- [ ] Select TOC grounding notes/preview/application and fact verification/review/selective application from existing native routes.
- [ ] Locate the actual native quality owner before defining its MCP operation. Select supported entity-schema execution/status/application separately.
- [ ] Resolve any required provider credential through an existing secure server-side connection; exclude secret fields from public tool arguments.
- [ ] Separate paid analysis, stored review and body/schema mutation. Pin the exact analysis, selected findings and article/body revision.
- [ ] Preserve edit leases and native history; reject stale analysis, revoked access and duplicate application.
- [ ] Test malformed output, missing secure connection, no-op review and selective apply. Update existing optimization/editor guidance.

## P2 — remaining Link Workbench

- [ ] Select plan-item addition/bulk addition, direction flip, candidate editing and bounded export from native owners.
- [ ] Keep explicit discovery/anchor work separate from plan mutations. Audit convenience wrappers that auto-discover or reconcile before exposing reads.
- [ ] Check source and target authority, content-group/path bounds, plan/item revisions and current analysis.
- [ ] Invalidate old review and insertion data when a candidate or direction changes. A flip must not trigger paid discovery implicitly.
- [ ] Implement only supported exact draft removal/reversal using the original insertion reference. Preserve unrelated edits and refuse ambiguous matches.
- [ ] Test stale/self/duplicate pairs, both endpoint grants, bulk/export limits, partial/unknown discovery and reversal after unrelated edits.
- [ ] Retain useful inline and CTA/service-block paths; similarity alone is not editorial justification. Update the existing internal-link skill.

## P3 — Social Intelligence

- [ ] Reuse native workspace/content-group ownership, ingest workers, normalization and existing voice analysis; add no MCP mapping store.
- [ ] Select scoped workspace reads/provisioning, original ingest job/status, normalized item browsing and stored voice-profile browsing/activation.
- [ ] Classify reads as R, provisioning/activation as W, and ingestion/analysis as P; freeze finite item/source/page/time/provider limits before dispatch.
- [ ] Audit native admission/accounting before exposing ingest starts. Preserve original jobs, allowances and unknown-start recovery without replacement runs.
- [ ] Keep platform actors and credentials server-owned; bound corpus selection before hydration. Preserve the existing 200-item voice ceiling.
- [ ] Test cross-project access, duplicate items, partial ingestion, revoked access, unknown outcomes and stale/failed-profile activation.
- [ ] Keep activation distinct from article voice application, derivative generation and publishing. Extend existing guidance where appropriate.

## Gates for each selected slice

- [ ] Record redundancy/seam checks: inspected adapters and adjacent flows, reused owner, and justification for any new interface.
- [ ] Use closed schemas and server-resolved ownership. Recheck authority before execution and result publication; keep lock sessions short.
- [ ] Cover the actual SDK/browser preview-to-start flow, input canonicalization, original-ID replay, expiry and quota refusal with controlled dispatch.
- [ ] Use owned PostgreSQL fixtures for changed concurrency, locking and financial ownership; preserve shared databases/queues and clean up owned fixtures.
- [ ] Test read non-mutation, bounds before hydration, safe projections and partial/degraded/unknown outcomes.
- [ ] Keep a per-operation ledger distinguishing implementation, local tests, native qualification, deployment, installed-client and paid acceptance.
- [ ] Update user documentation, skills and evaluations alongside admitted capabilities. Record unsupported cases explicitly.
- [ ] Run relevant repository/CI checks; repeat or broaden only for new changes, failures or unresolved concerns.

## R2 release checklist

- [ ] Review the selected matrix and actual catalogue for excluded Factory/WP/GA exposure, including OAuth metadata.
- [ ] Build a new versioned package only when its guidance/capabilities change; preserve the v0.3.0 artifact and checksum.
- [ ] Publish an English changelog, manifest/checksums, CI links, operation ledger and actual acceptance limits.
- [ ] Obtain separate authorization before paid/live calls, Labs deployment or production OAuth/flag/provider changes. Preparing implementation and controlled evidence does not authorize activation.
- [ ] After an authorized deployment, verify actual source/image/schema, scope offers, public protocol boundaries and controlled in-container behavior. Do not infer deployment from a published ZIP or merge.
- [ ] Run installed-client/paid acceptance only at its explicitly authorized scope and budget; capture actual outcomes rather than promoting local tests to live success.

## Fresh-session instruction

> Implement only selected R2 rows from this plan and the advanced technical specification. First verify backend main containing c1f96b383b75b8964e56794b5b04ac6ec1f85ab0, current runtime and worktree ownership. Freeze the finite operation matrix, reuse native owners, complete one reviewable slice at a time, and preserve Factory/WP/GA exclusions. No paid calls, deployment, production configuration changes or external messages without separate authorization. Update evidence and guidance for what actually passes; report concrete blockers while completing independent selected work.
