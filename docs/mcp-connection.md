# Connect the NobleSEO Research MCP

The plugin supplies skills; it does not automatically install an MCP server entry. Reuse an existing working NobleSEO connection. Otherwise obtain your endpoint, registered client ID and exact callback settings from your team. Sign in with your own NobleSEO account and select your authorized organization and projects.

The endpoint uses Streamable HTTP and OAuth. No local backend or API key is needed. The registered callback must match the supplied host, port and path; do not substitute loopback hostnames.

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

`APPROVAL_REQUIRED` means browser approval has not been accepted. Unknown cost is not a free run. Missing tools can reflect missing scope, disabled capability or an unavailable deployment; report the actual response instead of bypassing it.

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

## Optional WordPress publication candidate

After deployment and registered-client admission are confirmed, request fresh `publish` consent for the selected project with editor access. Discover `publication_list_targets`, `publication_preview`, `publication_execute`, `publication_get_status` and `publication_refresh_status`; article inspection uses its own read scope. Use the project's explicit paired site and discover its contract/features. Legacy supports plain draft/live publication with guarded excerpt preservation; the options-aware contract supports additional choices. Exact browser approval authorizes one dispatch. Stored status never contacts WordPress; explicit same-ID verification performs a read and canonical reconciliation without resend. Discovered retry/revert modes need separate exact approval, preserve the original publication ID/payload and record canonical per-operation uncertainty. Section-bound creation and historical compensation without an in-scope baseline remain required work. Plugin installation does not change OAuth registrations, pair a target or authorize external publication.
