---
name: editorial-handoff
description: Deliver one saved NobleSEO article revision as an explicitly approved Google Doc, ClickUp task or Jira issue, retaining the native external receipt and any uncertainty. Use for requested document export or editorial task handoff.
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
