# Roadmap

What is planned for this repository. Nothing on this page is available yet; released items move to [CHANGELOG.md](../CHANGELOG.md).

## NobleSEO MCP connection

The `nobleseo` plugin will connect your assistant to the NobleSEO MCP server, so it can use your NobleSEO projects: keyword clustering, competitor research and content briefs.

- You sign in with your NobleSEO account in the browser; no API key.
- You choose the organization, projects and permissions the assistant may use, and you can revoke the connection at any time in NobleSEO.
- Runs that use credits (clustering, research) start only after you approve their preview in NobleSEO.

The connection is added to the plugin when the server is generally available.

## Planned skills

Both skills need the MCP connection.

### `keyword-clustering`

Give your assistant a list of keywords — pasted, or a CSV/text file — and get clusters and topic hubs back.

1. The assistant cleans the list (trims spaces, removes duplicates) and asks which NobleSEO project, market and language to use.
2. It requests a preview. You approve it in NobleSEO; the preview shows how many keywords will be clustered.
3. When the run finishes, the assistant summarises each cluster (name, size, main keywords, hub) and saves the full result as CSV or JSON in your working directory.

Limits per run: up to 5,000 keywords and 200,000 characters. Larger lists are split by topic with your agreement, never cut silently.

### `seo-content-briefing`

Start from one main keyword and get the complete set of recommendations NobleSEO shows in its editor, as a brief file:

- **Main text** terms by priority tier, with entities marked;
- **Title**, **Headings** and **Description** terms;
- **Bolded terms** and **Related searches** from the search results;
- **FanOut**: the follow-up needs searchers have;
- **AI Topics**: the topics and facts that AI answers cover.

Steps:
1. The assistant reuses an existing NobleSEO analysis for the keyword if you have one, or prepares a new one.
2. It requests a research preview; you approve it in NobleSEO.
3. If the research pauses to let you pick competitor pages or answer three questions, the assistant shows you the choices.
4. It saves the brief as Markdown and JSON in your working directory. Warnings about stale or partial data are kept.

## Under consideration

- **Internal link review** — only once NobleSEO offers a read-only link tool through MCP.
