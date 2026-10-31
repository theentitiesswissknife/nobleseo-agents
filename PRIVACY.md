# Privacy

The skills in this repository run on your computer, inside your AI assistant.

- `gsc-visualization` reads the data file you point it at and writes chart images to your working directory. The scripts make no network requests and send no data anywhere.
- What your AI assistant itself sends to its provider is governed by that assistant's own terms.
- `gsc-performance-review` analyzes supplied exports or an already authorized connector. It does not add a Google connection. When optional NobleSEO Analytics tools are deployed and granted, requests include a selected project ID, date windows and optional exact page/query filters; responses contain project-scoped persisted query/page data.
- `keyword-clustering` and `seo-content-briefing` use a separately configured NobleSEO MCP connection. Requests may include selected project/run/content IDs, keywords, market/language, research selections and brief edits. Responses contain data permitted by your organization/project grants.
- New clustering or research requires a preview approved in NobleSEO and can use credits and external providers. Preparing a stored brief changes NobleSEO state even without a research provider call. Reading data does not implicitly authorize these operations.
- The plugin contains no credentials. Your MCP client handles sign-in and token storage. Revoke the connection from NobleSEO account settings, Connected clients.
