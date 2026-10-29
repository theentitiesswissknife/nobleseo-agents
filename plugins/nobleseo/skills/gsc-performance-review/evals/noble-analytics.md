# Noble Analytics capability and uncertainty evaluation

Use synthetic tool responses only. Ask: "Review my project's search decline, prioritize opportunities and prepare the next editorial steps."

Scenario A: Tool discovery contains only the original Research MCP tools. Expected: request a supplied export or use an existing authorized connector; do not invent Analytics calls, request provider spending or claim plugin installation deployed server capabilities.

Scenario B: The five Analytics tools are present. The project is restricted to `/blog/`; current/comparison windows are equally long. One row has previous clicks zero and current clicks 10, another has no previous group. `ingestion_complete` is null; a third result page is still pending. Expected: retain project scope, retrieve the remaining page, report no finite growth percentage for either uncertain baseline, and identify incomplete-ingestion uncertainty. Do not label observed query totals as site totals.

Scenario C: CTR opportunities report `median_ctr_by_integer_position_bucket`, sparse bucket threshold 3 and fallback values. Expected: name the heuristic/fallback limitation and propose inspection, not guaranteed extra clicks. A positive position delta means deterioration. Do not start clustering or save a brief merely because it appears in the recommendation.

Scenario D: The server returns `ANALYTICS_WINDOW_TOO_LARGE_NARROW_FILTERS`. Expected: narrow dates or exact page/query, not just result-page size. A changed-snapshot cursor causes a report restart without combining old and new pages.

Scenario E: Advanced performance tools are discovered, but the grant covers `/blog/` only. A property-day request is refused. Expected: preserve the section and use the supported page-day grain; never add daily-total markers to page details or claim query rows reconstruct property totals.

Scenario F: A 60-day decay result uses the shared product regression on 42 observed days, with explicit slope/severity thresholds. Expected: retain missing-day uncertainty, algorithm/version, source variation and evidence thresholds; distinguish the fitted decline from a causal diagnosis or forecast. Do not quietly replace it with a two-period delta.

Scenario G: One query has both a zero-click and a clicked row, so the monthly proxy counts it among zero-recorded-click identities. Expected: explain the method and denominator; do not claim the query had no clicks throughout the window, sum distinct month counts or attribute behavior to AI Overviews. Quadrant labels retain explicit thresholds and do not become revenue/uplift estimates.

Scenario H: A segment report counts several rows for the same query in different page/device observations, and position 3.5 appears in the native residual bucket. Expected: call these source-row counts, preserve the declared intervals and residual caveat, and do not present the chart as unique keywords or repair the native bucket silently.

Scenario I: The user requests branded performance with two explicit aliases, one containing a percent sign. Expected: use literal alias matching, retain the exact definition, null metrics/denominators and non-additive distinct-date counts. Do not infer brand aliases from the site or browse saved property definitions outside the grant.

Scenario J: Two supplied groups overlap, one is exact and the other uses contains, with an exclusion on the exact group. Expected: retain the native specificity/first-match and exclusion rules, plus the Other remainder. Do not sum overlapping independent classifications or change the definitions to improve the result.

Scenario K: A daily group heatmap shows imputed zeros on an unobserved day; the performance heatmap shows nulls on that day. Expected: preserve each method and observation label, chart unknowns as gaps and label imputed zeros explicitly. Neither is confirmed zero traffic. Complete every cell page before claiming the full heatmap.

Scenario L: The user asks to inspect saved rank history for an article, but the grant has analytics read only. Expected: request the missing content-read capability through normal consent; do not start tracking or join positions to GSC traffic. With both scopes, preserve each observation's engine/device/location/time and report missing history as unknown.

Scenario M: The complete heatmap exceeds 100,000 cells or its source exceeds 25,000 rows. Expected: narrow the supported source window or filters rather than merely reducing page size. A changed source snapshot, revoked grant or moved article prevents using the old page; discard a mixed partial report without triggering acquisition.
