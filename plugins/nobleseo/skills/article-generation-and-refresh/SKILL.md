---
name: article-generation-and-refresh
description: Prepare a bounded NobleSEO article action from a selected keyword, cluster or qualified editorial gap, or guide an existing article through canonical Refresh checkpoints. Use for article generation and refresh requests; discover execution capabilities before promising an automated draft.
---

# Generate or refresh a selected article

## Requirements

A connected NobleSEO MCP server and explicit access to the selected project. Discover current tools, their schemas and capability flags. `generation_get_options` requires `content.read`; generation preview, start and cancellation require `content.generate` and any additional scopes reported by the server. Reading the options catalog does not establish execution authority or prove that generation is deployed.

Some server versions expose only generation options alongside the separate Refresh tools. If `generation_preview`, `generation_start`, `generation_get_run` or `generation_cancel` is missing, explain the specific missing capability and preserve the requested article inputs for later continuation. Do not invent a tool, call an organization-wide API or substitute repeated research launches for the missing generation action. A local assistant-authored article is a separate deliverable and must not be represented as a completed NobleSEO run.

## Prepare one exact action

Resolve the granted project and selected source. Read `generation_get_options(project_id)` for native content types, length bounds, voice choices and feature availability. Request only the selected project's options. The catalog cannot establish a source's eligibility, current template binding, credit allowance or executable provider cap.

Preserve the server's source identity and reference versions. A selected cluster/keyword must belong to an authorized active run when required by the current schema. A coverage gap needs canonical observed node/placement evidence; an assistant's hypothesis or a gap outside the authorized projection is insufficient. An existing article refresh follows the separate Refresh workflow below. Never replace a source object with an arbitrary prompt or use organization-wide discovery to circumvent a missing project binding.

When the full generation tool set is available, prepare one article per action through `generation_preview`, using the current schema and a stable request UUID. Bind the selected source, template/version, current article or brief revision where applicable, native length/voice choices, provider channels and work limits. Media work must be an explicit metered option already supported by that action. Do not add image generation, acquisition, social derivatives or publication because the user requested an article.

Show the exact preview's effects, approval URL, expiry and cost/credit uncertainty. An approximate estimate is not an enforceable provider cap. Unknown cost is not zero. Obtain an exact bounded preview that the service can enforce before dispatch; if that cannot be established, retain the prepared selection without starting work.

## Execute and inspect the canonical result

After the existing NobleSEO browser approval, use the returned execution inputs and matching approval/digest with `generation_start`. Do not reconstruct a stale source or silently change the template, voice or work profile. Record request, approval and canonical run/receipt identities. A timeout or ambiguous dispatch response calls for status reconciliation with `generation_get_run`, not another request UUID or automatic retry.

Track the canonical run at a modest interval. Retain stage/checkpoint details, partial or degraded results, completed artifacts and known versus held charges. A created editing shell, queued research, ready brief and completed article body are different outcomes. Do not claim an article is generated merely because a content ID or editor link exists. Honor a reported human checkpoint through its owning review flow; do not approve it on the user's behalf without authorization.

For an authorized cancellation, use `generation_cancel` on the selected canonical receipt. Report the observed terminal or pending state. Cancellation prevents future work where the service can stop it; already admitted provider work, final charges, unknown outcomes and completed artifacts remain visible. It is not evidence of a refund or permission to restart the action.

Inspect the saved article through the discovered scoped content tools, preserving revision and run provenance. Report what completed, what needs editorial review and any unresolved accounting or failed stage. Publication is a separate explicitly authorized action.

## Refresh an existing article

Use the canonical `refresh_prepare`, `refresh_get`, `refresh_preview_level`, `refresh_start_level`, `refresh_review_level`, `refresh_dismiss_candidate` and `refresh_stop` tools when deployed. Retain run/estimate IDs, binding version/hash, saved body revision/hash, the selected `correct`, `enrich` or `expand` level and its authorized worst-case cost. Generic article generation intake does not replace this state machine.

Read the current checkpoint before advancing. A reported brief or level review remains a human decision. Preparing a pool, acquiring GSC queries or selecting knowledge/research outputs has its own effects and scopes; do not purchase or collect missing evidence during inspection. Shared research continuation/recovery uses the original registered root and reported allowance. Unknown or held charges cannot be reset with a new action identity.

Use the exact current preview/approval for each requested provider-backed continuation. Inspect partial candidates and dismiss or accept them only when requested through the owning tool. Acceptance into notes does not itself apply text to the article body. Any body application uses the returned exact diff/revision/lease protection and an explicitly requested save. Follow the detailed Refresh approval and recovery guidance in [article-optimization-review](../article-optimization-review/SKILL.md) when that workflow is available.

Report the saved result and remaining review checkpoints. Keep article completion, publication, deployment and live-client qualification separate.
