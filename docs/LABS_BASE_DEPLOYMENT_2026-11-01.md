# Labs base backend deployment

Status: deployed and verified on [Labs](https://labs.nobleseo.io). Verification completed at `2026-11-01T01:32:29Z`.

## Release binding

- Deployed backend: `c1f96b383b75b8964e56794b5b04ac6ec1f85ab0`, merged to main in [backend PR 37](https://github.com/MaxGSEO/NobleSEO_Refactoring/pull/37).
- Exact-revision image CI: [Monorepo Split CI](https://github.com/MaxGSEO/NobleSEO_Refactoring/actions/runs/41253705821).
- Skill package: [v0.3.0](https://github.com/theentitiesswissknife/nobleseo-agents/releases/tag/v0.3.0).
- [Base ZIP](https://github.com/theentitiesswissknife/nobleseo-agents/releases/download/v0.3.0/nobleseo-agents-0.3.0-base.zip), SHA256 `6fa636cd518f23bb1b791130831dbce8a0aaf3aceba2e0573468d974d25985f2`.

The existing ZIP and tag remain unchanged. The ZIP contains skills; this deployment supplies their backend. Factory, WordPress and Google Analytics are excluded. The release catalogue exposes 143 tools; deferred Factory and WordPress names are rejected before adapter dispatch. GSC uses `analytics.read`; this does not enable Google Analytics.

## Approval repair

An execution attempted before approval is saved still correctly returns `APPROVAL_REQUIRED`. Its response now retains the original owned approval ID, pending state and recovery action. Poll the original preview until it reports the same ID as approved with a saved timestamp. Reused previews refresh their database row; the browser page distinguishes an unsaved decision from committed approval. Expiry returns `APPROVAL_EXPIRED`. Execute the original inputs once; retries replay the original accepted result without another dispatch.

The reported incident does not establish a post-commit rejection: the recorded attempts preceded the saved browser approval. The original expired records are preserved. The separate managed-run allowance and research action quota are not interchangeable, and unknown cost is not zero. Native authorization, revision/input binding, CSRF, expiry and credit admission remain enforced.

OAuth metadata uses the same release catalogue as tool discovery. The SDK selects 18 base scopes rather than requesting archived Factory scopes that the registered base client cannot grant. The regression was reproduced with the official SDK's scope-selection function; after repair, the native consent and token exchange complete with exactly the base permissions.

## Verification

Exact-revision [image CI](https://github.com/MaxGSEO/NobleSEO_Refactoring/actions/runs/41253705821) passed: 2,271 API-image cases, 369 native Google/PostgreSQL cases and 26 MCP/PostgreSQL approval/native-worker cases. The separate [Python lint](https://github.com/MaxGSEO/NobleSEO_Refactoring/actions/runs/41253582093), [Ruff](https://github.com/MaxGSEO/NobleSEO_Refactoring/actions/runs/41253582096) and [editor/clusterizer E2E](https://github.com/MaxGSEO/NobleSEO_Refactoring/actions/runs/41253582145) checks passed for the same commit. Duplicate main-push workflows were canceled after these exact-commit checks; canceled runs are not successful checks.

The native deployment script completed PostgreSQL/Redis backups, image builds, migrations and service smoke checks. All five API/worker/web/GSC services carry the verified commit label and are healthy. Earlier local regression groups overlap the final CI coverage and are not added to its counts.

The integration also retains the existing worker authorization seam and flushes the native voice result marker before a financial-owner refresh in the same transaction. Both requirements files pin the qualified `fal-client==0.11.0` and `langgraph==1.0.6`; the previous unconstrained versions changed client lifecycle and cancellation behavior in Linux CI. The existing image suite retains its previous selections, runs the affected modules first, and fails promptly on the first regression.

Post-deployment verification used the actual API container:

| Check | Result |
| --- | --- |
| Critical source manifest | 16 files match the verified Git commit using Python AST/text hashes |
| Qualified SDKs | `fal-client 0.11.0`, `langgraph 1.0.6` |
| Database head | `mcp20261031b1` |
| Existing base feature flags | Nine required flags remain enabled; no additional feature activation |
| Release catalogue and scope offers | 143 tools, 18 base scopes, Factory/WP/GA excluded |
| Existing-grant native reads | `get_context`, `list_projects`, `research_get_run`, `brief_get` passed in read-only transactions |
| GSC connection | Successful query in an explicitly read-only transaction |
| Controlled SDK/browser tests | 13 passed in the deployed container, including approval/dispatch replay and discovery/consent/token exchange |
| Public HTTP and OAuth | Main and GSC health/pages return 200; PKCE/public-client metadata and MCP resource binding pass; unauthenticated MCP returns 401 |

The 13 protocol cases use private SQLite data, controlled dispatch and a physical network fence. Persisted reads use the existing grant and actual databases without customer-data writes. Client scope offers were extended with a private configuration backup; existing grants were not expanded. The original expired approvals were preserved. The skill ZIP and tag are immutable and unchanged.

## Client test procedure

1. Install the v0.3.0 base ZIP if using the original limited package.
2. Reconnect with the scopes needed for the selected base workflows. Existing grants are not silently expanded; updated client scope offers require explicit consent.
3. Create a fresh research preview. Old expired approvals cannot be reused. Complete browser approval, then observe the original preview until the saved approval is visible.
4. Start using that original approval ID and exact execution inputs. Use the returned run/job identity for status and recovery.
5. If blocked, report the tool name, approval/request/correlation IDs, timestamps, status/code and run stage. Do not include tokens or private provider payloads.

Controlled protocol tests and persisted reads do not establish Paul’s installed-client acceptance or a paid live research/generation result. No paid acceptance run is claimed.
