# Connect the NobleSEO Research MCP

The plugin supplies skills; it does not automatically install an MCP server entry. Reuse an existing working NobleSEO connection. Otherwise obtain your endpoint, registered client ID and exact callback settings from your team. Sign in with your own NobleSEO account and select your authorized organization and projects.

The endpoint uses Streamable HTTP and OAuth. No local backend or API key is needed. The registered callback must match the supplied host, port and path; do not substitute loopback hostnames.

For Labs, see the separate [base backend deployment receipt](LABS_BASE_DEPLOYMENT_2026-11-01.md). The Codex and Claude clients offer 18 base scopes; existing grants retain their original permissions. Reconnect and consent to the scopes needed for additional workflows before creating a new execution preview. The offered set is `analytics.read`, `brief.write`, `clusterizer.run`, `content.generate`, `content.read`, `content.score`, `content.write`, `coverage.read`, `delivery.write`, `knowledge.read`, `knowledge.write`, `links.read`, `links.write`, `media.read`, `publish`, `read`, `research.curate` and `research.run`. Factory permissions are excluded; `analytics.read` covers GSC.

## Codex

Merge this into `~/.codex/config.toml`, replacing every placeholder. Update existing `nobleseo` tables instead of adding duplicates. The callback port must be numeric and match the explicit port in a direct local callback URL.

```toml
[mcp_servers.nobleseo]
url = "<NOBLESEO_MCP_URL>"
oauth_resource = "<NOBLESEO_MCP_URL>"

[mcp_servers.nobleseo.oauth]
client_id = "<REGISTERED_CODEX_CLIENT_ID>"
callback_url = "<REGISTERED_CALLBACK_URL>"
callback_port = <REGISTERED_CALLBACK_PORT>
```

Choose the login command for your intended workflow:

```bash
# Read existing clusters, research and briefs
codex mcp login nobleseo --scopes read

# Read and run clustering
codex mcp login nobleseo --scopes read,clusterizer.run

# Clustering, research, stored briefs and curation
codex mcp login nobleseo --scopes read,clusterizer.run,research.run,research.curate,brief.write
```

Complete browser consent and restart the client/start a new chat if needed. If an old grant stays read-only, use the client's logout/reconnect flow and authorize the needed scopes. The live tool catalogue is authoritative.

## Claude Code

Use the supplied Claude client ID and callback port:

```bash
claude mcp add --transport http --scope user --client-id <REGISTERED_CLAUDE_CLIENT_ID> --callback-port <REGISTERED_CALLBACK_PORT> nobleseo <NOBLESEO_MCP_URL>
```

Run `/mcp` inside Claude Code and complete browser authentication, choosing the needed projects and permissions. Inspect/update an existing entry rather than adding a duplicate.

## First checks

1. Read the connection context and list authorized projects.
2. List existing clustering runs and inspect one, including every page and unclustered keywords.
3. To run new clustering, supply a small keyword list, project, market and language. Review the preview before approving it in NobleSEO.
4. Select a cluster and request a brief from existing research. Request new research separately if needed.

`APPROVAL_REQUIRED` means the server did not observe an approved action for that call. OAuth consent, opening an approval link and approving the action are separate steps. Wait until the action page says `Preview status: approved`. Before the first execution, replay the matching preview with the exact original inputs and unchanged request ID; verify the same approval ID/digest, approved status and a future expiry. A pending replay is a reason to wait, not to start repeatedly or create another approval. After execution or an ambiguous dispatch, inspect the existing run/receipt instead of replaying a preview for an earlier checkpoint. Unknown cost is not a free run. Missing tools can reflect missing scope, disabled capability or an unavailable deployment; report the actual response instead of bypassing it. Use the [feedback template](feedback-template.md) for reproducible findings without credentials.

## Optional Analytics increment

The original Research MCP catalogue does not retrieve GSC reports. A separate server increment adds five project-scoped Analytics tools for persisted web-search query/page data. This plugin candidate supports that increment but does not deploy it.

Only after your team confirms deployment and adds `analytics.read` to the registered client's allowed scopes, authorize it through a fresh consent flow:

```bash
codex mcp login nobleseo --scopes read,analytics.read
```

Verify that `analytics_get_project_site`, `analytics_get_data_status`, `analytics_report_query_performance`, `analytics_compare_query_performance` and `analytics_find_ctr_opportunities` appear. Old `read` grants do not include them. Select only authorized projects. These reports are privacy-filtered query/page observations, not complete property totals, GA4 reports or a live Google connection. If absent, use supplied exports or another authorized connector.

References: [Codex MCP](https://learn.chatgpt.com/docs/extend/mcp) and [Claude Code MCP](https://code.claude.com/docs/en/mcp).

## Optional internal-link candidate

After deployment and registered-client scope admission are confirmed, request fresh `links.read` consent for stored internal-link review. Explicit simulation and supported versioned plan/business-review changes separately require `links.write`. Exact draft-only link preview/application additionally requires `content.write`; inspecting drafts uses the article tools' separate read permission. Discover the live catalogue, supported targets and capability limits. Existing grants and plugin installation do not add these permissions. The project needs its explicit site/path binding and stored analysis; section access does not grant the entire property. WordPress application and the remaining plan/discovery/export workflows remain unfinished in this candidate. External CMS writes require their separately supported authority.

## Research batch capabilities

Research batch inspection is a separate owner and capability family. Discover `research_batch_list` and `research_batch_get` under `read`; candidate ranking additionally requires explicit `analytics.read` and uses stored GSC data without synchronization. The initial adapter admits only retained native selections of at most 20 current project articles. Preserve `membership_basis`: legacy item rows cascade away after article deletion, so historical original-roster completeness is not proven. Preserve native batch/item/research IDs, missing cost and pagination. Missing capabilities cannot be replaced by a Factory run or direct HTTP. Deployment and native client acceptance remain separate qualifications.

When `research_batch_get_map` is discovered under `read`, inspect its stored preliminary needs/cells and exact query verdicts separately, preserving native completeness, snapshot and stale-basis information. It does not rebuild a map, record feedback or authorize batch execution. Project reach/demand and the current viewer's vote remain scoped; private provider responses and feedback notes are withheld.

If `research_batch_cancel` is discovered, explicit user-requested stopping requires both `read` and `research.run`. Review `research_batch_get selection=cancellation`, keep its exact snapshot and one request ID, and distinguish pending exclusion from preserved started work/unknown usage. Lost replies use identical arguments to recover the original atomic receipt; do not create a new command or reset accounting. Paid preview/start and native desktop acceptance remain separate qualifications.

## Optional Outline generation candidate

After the backend increment and registered-client admission are confirmed, request `content.generate`, `content.read` and `knowledge.read` together. Discover `outline_preview_generate`, `outline_start_generate`, `outline_regenerate_section` and `outline_get` with `selection=request`. The original Labs catalogue and the dedicated four-skill 0.2.1 approval-retest package do not supply this increment. Plugin installation alone does not add the tools or scopes.

Native approval binds one planning request, its current sources and a finite shared USD cap for text calls and cloud KB query embeddings. Current article/plan/background revisions, an existing KB runtime and locally available model assets still apply. An uncertain queue reply is reconciled through the original receipt without a new job or allowance. Plan generation preserves the article body; insertion, acceptance, prose generation and external publication remain separate actions.

## Deferred features

Factory and WordPress are excluded from the 0.3.0 release. Their preserved development adapters and archived skills are not an invitation to request scopes, call hidden tools or enable native flags. Google Analytics retrieval is also excluded. Advanced generation/editor combinations, the remaining full Link Workbench flows and Social Intelligence belong to a separate implementation session.
