# NobleSEO MCP user guide

Updated: 2026-11-01. Audience: users and testers of the published base, including Paul.

## What you need

- A NobleSEO account with access to the intended organization and projects.
- A supported MCP client and the [v0.3.0 base package](https://github.com/theentitiesswissknife/nobleseo-agents/releases/tag/v0.3.0).
- A connection to the team's NobleSEO endpoint. For this delivery, the backend is [Labs](https://labs.nobleseo.io); no local backend or provider API key is needed in the client.

Follow the [connection guide](mcp-connection.md) for exact client IDs, callback requirements and login commands. Reuse an existing connection rather than adding a duplicate. Never paste tokens, cookies or provider credentials into chat.

The skills guide the assistant through workflows. The MCP server supplies tools, checks access and runs supported native operations. Installing the ZIP does not change server permissions. The [deployment receipt](LABS_BASE_DEPLOYMENT_2026-11-01.md) records the separately deployed backend and its checks.

## First session

1. Install the package using the [Codex](codex.md) or [Claude Code](claude-code.md) instructions.
2. Connect and complete browser consent using your own account. Select the intended organization, projects and permissions.
3. Refresh the client's tool catalogue or start a new chat after an update.
4. Ask the assistant to read connection context and list authorized projects. Confirm the project before requesting work.
5. Inspect existing results first. Request a new run explicitly when needed.

Example:

> Read my NobleSEO connection context and list the projects I can access. Show which base workflows are available with my current permissions. Do not start any runs or change data.

Labs offers 18 base scopes to the registered Codex and Claude clients. An existing grant retains its original permissions. Additional tools may require reconnecting and consenting to additional scopes. `analytics.read` is for GSC; it does not enable Google Analytics. The connection guide lists the complete offered set. Tool discovery can declare additional required permissions for a particular action.

## Choose a workflow

Replace bracketed values with your selected project, content or run. The assistant should discover actual tool names, supported options and limits before execution.

| Task | Example request | Expected result and boundary |
| --- | --- | --- |
| Inspect clusters | “Review clustering run [run] in [project], including unclustered keywords and pagination. Do not launch another run.” | Stored clusters and missing-data notes; no replacement execution |
| Run clustering | “Preview clustering for this keyword list in [project], using [language/market]. Show limits and cost before approval.” | An exact preview followed by browser approval for a new run |
| Research and brief | “Inspect research for content [content]. If new research is needed, preview full mode with at most five pages and the requested outputs. Wait for approval before starting.” | Existing research or a bounded approved run, then a brief from available evidence |
| GSC review | “Compare these two complete weeks for [project]. Explain page/query drivers and missing coverage; do not synchronize Google data.” | Persisted GSC observations, with coverage/privacy limits |
| Charts | “Use gsc-visualization to chart this authorized report/export and label its dates and limitations.” | Local chart artifacts; chart generation does not fetch Google data |
| Generate one article | “Show supported generation options for [content/source]. Preview one qualified profile with explicit work and spending limits; wait for approval.” | Supported native generation or canonical Refresh, with original receipt and actual outcome |
| Review a draft | “Inspect and score saved draft [content] at its current revision. Propose edits without saving them.” | Review/proposal; saving requires an explicit request and current revision/lease checks |
| Outline and assets | “Inspect the outline and stored assets for [content]. Show supported changes before applying anything.” | Scoped outline/asset operations; standalone advanced image generation is not implied |
| Internal links | “Review stored link candidates for [project]. Explain destination usefulness and show a simulation before proposing exact draft insertion.” | Qualified review/simulation/draft operations; full Link Workbench and WordPress application are deferred |
| Social derivative | “Discover supported social derivative options for [content]. Preview one bounded derivative; do not publish it.” | Supported derivative generation with explicit approval; Social Intelligence ingestion is deferred |
| Handoff | “List approved [Google Docs/ClickUp/Jira] destinations for [project] and preview delivery of revision [revision]. Do not send yet.” | A preview for one configured destination; execution may notify other users |

Use only discovered, supported capabilities. Missing native connections, source bindings, eligible evidence or feature flags can block a particular action. Ask for the exact missing prerequisite; do not substitute another project, provider or workflow. The [base scope](release-scope.md) defines the release boundary.

## Approve and start work

OAuth connection consent and approval of an individual action are separate steps. Browser approval also does not replace native business review, credit admission or revision checks.

1. Ask for a preview of one explicit action. Review its project, source, selected outputs, destination, revision, limits, expiry and known or unknown cost.
2. Keep the original request ID, approval ID and execution inputs. Open the returned approval page and approve there yourself.
3. Wait for the page to confirm that approval is saved. Before first execution, have the assistant observe the matching preview with unchanged inputs and request ID. It must show the same approval ID, approved status, saved `approved_at` timestamp and a future expiry.
4. Start with that original approval ID and exact execution inputs. Do not silently change the model, source, page limit, destination or revision.
5. Keep the returned run/job/receipt identity. Inspect that existing execution for progress and recovery.

`APPROVAL_REQUIRED` while the original preview is pending means the server has not observed saved approval. Wait and observe that preview; repeated starts or replacement approvals do not repair it. `APPROVAL_EXPIRED` requires a fresh preview with a new request identity and fresh browser approval. The approvals from the original October test have expired.

If execution was accepted or its reply was lost, inspect the original run/receipt before doing anything else. An ambiguous response is not permission to create a new run. A replay must retain the original identity and inputs through the supported recovery path.

Unknown cost is not zero. An allowance for one action cannot be assumed to cover another action. Approval does not bypass the native quota or spending checks.

## Read progress and results

- **Accepted/queued:** work was admitted; this does not prove completion.
- **Running:** inspect stage progress and the original run identity.
- **Completed:** inspect the action's own artifact/revision and completed effects, rather than assuming every optional effect ran.
- **Partial/degraded:** preserve successful results and report missing or failed stages.
- **Unknown/uncertain:** preserve receipts and cost holds; use advertised reconciliation or request human review.
- **Cancelled:** future work is stopped according to the native contract; previously admitted work may still have costs.

These are reading guidelines, not a promise that every tool uses identical status strings. Preserve the actual returned status. Do not treat a diagnostic draft as an approved saved article, a simulation as application, or an exported document as an externally published page.

## Recover from common problems

| Observation | Next action |
| --- | --- |
| A tool is missing or permission is refused | Refresh discovery, inspect granted scopes and current project access; reconnect with needed permissions when appropriate |
| Approval is still pending | Observe the original preview and confirm the browser save completed |
| Approval expired | Create a fresh preview and request identity; review and approve again |
| Inputs, source or article revision changed | Inspect current state and review a fresh preview; do not apply a stale approval |
| Another editor holds a lease | Stop the mutation and coordinate through the native editor; do not take over the lease |
| GSC coverage is missing | Inspect the project's site binding and stored data status; absent rows are not confirmed zero traffic |
| A connection, destination or knowledge runtime is unavailable | Report the exact native prerequisite; do not provision it or search private accounts implicitly |
| Execution timed out or status is unknown | Inspect the existing run/receipt and preserve the last observed state; do not automatically resend |

## Test and report an issue

Start with read-only checks, then one explicitly approved bounded action. A real provider run may incur costs. Do not repeat paid work merely to produce a better report. For an already accepted action, inspect its existing receipt.

Use the [feedback template](feedback-template.md), one report per reproducible issue. Include client/plugin version, timestamp with timezone, exact prompt, expected/observed behavior, error code, IDs, preview expiry, saved approval observation and run stage. Record unknown values as unknown. Redact credentials, private article text and provider payloads.

The deployed backend passed controlled SDK/browser tests and persisted-read checks. Paul's installed-client acceptance and paid live acceptance remain separate. The [R2 plan](R2_TODO.md) tracks the next work; Factory, WordPress and Google Analytics remain excluded.
