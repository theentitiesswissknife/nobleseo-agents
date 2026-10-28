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

GSC analysis needs exports or a separate available GSC connector. The Research MCP does not retrieve GSC/GA4 reports.

References: [Codex MCP](https://learn.chatgpt.com/docs/extend/mcp) and [Claude Code MCP](https://code.claude.com/docs/en/mcp).
