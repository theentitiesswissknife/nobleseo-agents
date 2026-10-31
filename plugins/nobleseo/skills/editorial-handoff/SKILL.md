---
name: editorial-handoff
description: Deliver one saved NobleSEO article revision as an approved document or task, or publish one explicitly reviewed stored social derivative through its separate native approval. Retain the original receipt and any uncertainty. Use for editorial handoff, document export and requested social publication or scheduling.
---

# Deliver an article to an approved destination

## Requirements

Use a connected NobleSEO MCP server that discovers the four `delivery_*` tools. Each requires `delivery.write` and the current project editor role. Preview and execute additionally require `content.read`. Installing this skill does not deploy the tools, extend an existing grant or configure an integration. Fresh consent may be needed.

Native organization administrators configure project destinations and permitted users separately. Do not enumerate account-wide Google Drive, ClickUp workspaces or Jira projects, inspect integration settings, accept an arbitrary remote URL, or create an alternate connection through MCP. An empty destination list is a setup result, not permission to search other accounts.

## Workflow

1. Confirm the requested article, saved revision, connector and one destination. Read the article through its permitted content tools. Discover the server's supported kinds and limits. Do not infer that a Google connection qualifies ClickUp or Jira.
2. Call `delivery_list_destinations` with the explicit project and kind (`google_docs`, `clickup` or `jira`). Select a returned ID/name and retain it. Pagination is bound to the project, kind, grant and current visible destination snapshot.
3. Call `delivery_preview` with `content_id`, `revision`, `kind`, `destination_id`, a new UUID `request_id` and only supported `fields`. Defaults include the saved article body. Optional title, SEO fields and a note must reflect the user's requested handoff. The initial contract exports plain text: no formatting transfer, image upload or remote asset fetching. Private article knowledge notes are excluded by the canonical publishable renderer. Oversized exports refuse rather than silently truncate.
4. Review the exact title, exported text, destination, revision and effects. One external artifact is created; no explicit comment or assignee is added. Destination sharing, notifications and automations can notify other users. Approval does not promise silent delivery. Send the native `approval_url` to the user for browser confirmation; do not approve it on their behalf or treat a chat reply as native approval.
5. Call `delivery_execute` with only the original approved `approval_id`. Do not reconstruct or substitute the preview inputs. The server rechecks the current grant, role, destination, connection, revision and lease immediately before the physical request.
6. Keep the immutable command acceptance and native delivery receipt. Use `delivery_get_receipt(receipt_id)` to read the stored outcome; it performs no remote poll or resend. Report the original revision, destination, external ID/link and whether native content linking succeeded.

## Uncertainty and changes

A consumed approval never sends again. An `outcome_unknown` receipt means a request was admitted without confirmed success; a timeout, redirect, malformed response or connection refusal does not authorize an automatic replacement create. Replaying execute or reading the receipt preserves this uncertainty. Ask for human reconciliation through the owning external integration before a separately authorized new delivery; do not change request IDs to hide uncertainty.

A `refused_before_send` result requires reviewing changed authority or inputs and preparing a fresh preview when appropriate. Expired or replaced connections require native reconnection; this workflow does not refresh credentials, edit OAuth settings or switch accounts. A known successful external artifact with `linked: false` remains a successful external create: a concurrent native link or article move was preserved. Do not create another artifact to repair that link.

Deliver only the requested artifact. Do not fan out to multiple connectors, post comments, add assignees, publish social content or infer WordPress authorization from a delivery approval. Local simulated acceptance and live/native-client acceptance remain separate evidence.

## Separate mode: publish a reviewed stored social derivative

This mode requires the discovered `social_preview_publish`, `social_publish` and `social_get_publication` tools. All require `publish` and the current project editor role; preview and execution also require `content.read` and `media.read`. Document/task delivery approval does not authorize this mode. Native administrators connect the social account and bind its channel through existing connection/project settings; MCP cannot create or replace that connection. Discover supported formats separately for each provider.

1. Read the selected stored social batch/item with `media.read`, and the current saved article revision with `content.read`. Publishing does not generate or rewrite a derivative, fetch an asset locally or imply permission for another channel. Choose one exact item.
2. Call `social_preview_publish` with its `content_id`, `item_id`, current `revision` and a new UUID `request_id`. For scheduling, provide an explicit timezone-aware `scheduled_for` instant and an IANA `timezone` for human display. Inspect the compiled payload, account/channel, post/source/asset versions, supported format and effects. A selected image may be retrieved by the destination provider; public posting, sharing rules and notifications are external effects. The preview also identifies a replaced legacy schedule. Unknown external-service fees are not a free-provider claim; no LLM generation is included.
3. Require the user's native browser approval, then call `social_publish` with only that original `approval_id`. The accepted native attempt commits before its one deterministic queue submission. A future schedule remains at its exact approved instant and has a bounded execution window; accepting it before preview expiry does not permit changing the date, post, account, asset or grant later.
4. Read `social_get_publication` with the same article/item and `publication_id`. Stored reads never poll the provider, refresh credentials, repair a queue or resend. Keep immutable command acceptance distinct from current queue, preparation and publication state.
5. Report `published` only from the native receipt. `outcome_unknown` may include an admitted create or a known Instagram container without a confirmed visible post. A container ID or `FINISHED` preparation is not itself publication. `refused_before_send` records a refused original attempt; inspect the changed authority/input and prepare a fresh preview only if the user still requests it. Do not manufacture another request ID to bypass an uncertain attempt or silently replace an active schedule.

A consumed approval never creates a second queue submission or post. After timeout, lost queue acknowledgement, malformed response or partial preparation, preserve the original receipt and require native human reconciliation before a replacement. Original grant revocation stops subsequent sends while retaining acknowledgements from already admitted work. Account credentials, app permissions, provider-format acceptance and native desktop/live testing remain separate release evidence; plugin installation does not establish them. This mode does not authorize WordPress work or social generation.
