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

When the discovered schema exposes the project-owned Clusterizer run profile, send one `source` with `type: clusterizer`, its `run_id` and either one `keyword_id` or one `cluster_ids` entry. Keep `configuration.project_id` equal to the selected project. Use revision zero only for a genuinely new article; an associated empty article requires its current revision. Freeze native content type, length and voice through `configuration`, a stable `request_id`, and the exact reported `max_cost_usd`, `max_provider_calls`, request-byte and output-token bounds. The call bound covers paid header, SERP and writer requests together. The manifest's worst-work estimate can exceed the authorized cap: exhaustion stops unfinished work instead of widening the cap. Native credit prices and units are a separate uncertainty. This initial profile excludes volume refresh, entity analysis, RAG, images and bibliography. Other source/effect variants remain required server work, even when the four tool names exist.

When the schema includes `type: editorial_node`, select the exact observed `node_id`, `topic_space_id` and granted `origin_content_id`. The node must be visibly classified as adjacent or new-article for that origin; sharing an organizational topic space is insufficient. Preserve a specifically reviewed `main_keyword` when requested. `expected_revision` belongs to the target article (zero for a new editor), while the service separately freezes the origin's revision/body and source versions. Do not send `start_research: true`: native independent research-v2 is a separate action; the quoted parent analysis and writer already share this action's cap. Inspect the actual preview before starting: some native versions only create an editor, while qualified versions compose the existing full writer. Native intake-only zero estimates do not price that writer. Missing locale values use the service's exact quoted configuration, not a guessed country.

## Execute and inspect the canonical result

After the existing NobleSEO browser approval, use the returned execution inputs and matching approval/digest with `generation_start`. Do not reconstruct a stale source or silently change the template, voice or work profile. Record request, approval and canonical run/receipt identities. A timeout or ambiguous dispatch response calls for status reconciliation with `generation_get_run`, not another request UUID or automatic retry.

Track the canonical run at a modest interval. Retain stage/checkpoint details, partial or degraded results, completed artifacts and known versus held charges. A created editing shell, queued research, ready brief and completed article body are different outcomes. Do not claim an article is generated merely because a content ID or editor link exists. Honor a reported human checkpoint through its owning review flow; do not approve it on the user's behalf without authorization.

For the run profile, use the returned approval ID as `receipt_id` for status and cancellation. `acceptance` is immutable and may still say accepted after the current status becomes cancelled. A missing financial root means accounting is not initialized or not yet observed; it does not establish zero spend after an ambiguous dispatch. Preserve `dispatch_outcome: unknown`. `generated_revision` identifies this action's own saved generation; `artifact` describes the current article and can include later human changes. A superseded workflow is not permission to adopt or cancel the newer work. Read native `credits` separately from known provider bills and held unknown provider costs.

A failed native intake can retain an editor before a generation workflow is bound. If status returns `artifact.kind: native_editorial_intake`, report that retained editor and `intake_status` without claiming a generated body, generation revision or zero bill. An origin edit, hidden/merged node or live source-editor lease can stop further gap generation while preserving finished analysis and admitted costs. Reusing a cancelled empty node editor requires an explicitly requested new action, current bindings and a fresh exact browser approval; never reset request identities to escape uncertain dispatch or old cost holds.

For an authorized cancellation, use `generation_cancel` on the selected canonical receipt. Report the observed terminal or pending state. Cancellation prevents future work where the service can stop it; already admitted provider work, final charges, unknown outcomes and completed artifacts remain visible. It is not evidence of a refund or permission to restart the action.

Inspect the saved article through the discovered scoped content tools, preserving revision and run provenance. Report what completed, what needs editorial review and any unresolved accounting or failed stage. Publication is a separate explicitly authorized action.

## Refresh an existing article

Use the canonical `refresh_prepare`, `refresh_get`, `refresh_preview_level`, `refresh_start_level`, `refresh_review_level`, `refresh_dismiss_candidate` and `refresh_stop` tools when deployed. Retain run/estimate IDs, binding version/hash, saved body revision/hash, the selected `correct`, `enrich` or `expand` level and its authorized worst-case cost. Generic article generation intake does not replace this state machine.

Read the current checkpoint before advancing. A reported brief or level review remains a human decision. Preparing a pool, acquiring GSC queries or selecting knowledge/research outputs has its own effects and scopes; do not purchase or collect missing evidence during inspection. Shared research continuation/recovery uses the original registered root and reported allowance. Unknown or held charges cannot be reset with a new action identity.

Use the exact current preview/approval for each requested provider-backed continuation. Inspect partial candidates and dismiss or accept them only when requested through the owning tool. Acceptance into notes does not itself apply text to the article body. Any body application uses the returned exact diff/revision/lease protection and an explicitly requested save. Follow the detailed Refresh approval and recovery guidance in [article-optimization-review](../article-optimization-review/SKILL.md) when that workflow is available.

Report the saved result and remaining review checkpoints. Keep article completion, publication, deployment and live-client qualification separate.

## Select an existing asset or edit its stored alt text

Use discovered stored media tools with `media.read`; inspecting article image blocks additionally needs `content.read`. `media_list_assets` returns exact asset versions and, when separately authorized, the current article revision/body hash and supported native image-block indexes. Reads do not generate, fetch, upload or publish. Native storage keys and generation prompts are not public asset fields.

For an explicitly requested stored alt-text change, use `media_update_alt_text` with `content.write`, `media.read`, the current article revision, exact `expected_asset_version`, a stable request UUID and the requested alt text. This edits the asset record, preserving the saved article HTML and its revision. To update an already attached article image, separately preview and apply the selected asset to its native block; do not claim the metadata edit changed published or saved HTML.

For an explicitly requested article asset selection, choose one owned saved asset and one supported native block from the current inventory. Call `media_select_asset` in preview mode with the exact article revision/body hash, asset version, block index and request UUID. Review the exact replacement. Apply only that reviewed command with `stage: apply` and its `application_hash`. The action requires `content.write`, `content.read`, `media.read`, current Writer authority and no live editor lease. It creates canonical article history and preserves private notes and all other article bytes. An unsupported imported figure needs native editor normalization; do not overwrite captions or private content to force selection.

An identical retry uses the same request UUID and returns the original receipt. Changed input under that UUID is a conflict; a stale asset, article, preview or lease requires reviewing current state. No media write accepts arbitrary URLs, local file paths, provider credentials, image generation or publication. Upload, generation, acquisition and social-draft creation use their separately discovered and approved workflows when available; these stored-asset tools do not establish those capabilities.
