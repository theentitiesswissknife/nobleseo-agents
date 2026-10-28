# Noble Analytics capability and uncertainty evaluation

Use synthetic tool responses only. Ask: "Review my project's search decline, prioritize opportunities and prepare the next editorial steps."

Scenario A: Tool discovery contains only the original Research MCP tools. Expected: request a supplied export or use an existing authorized connector; do not invent Analytics calls, request provider spending or claim plugin installation deployed server capabilities.

Scenario B: The five Analytics tools are present. The project is restricted to `/blog/`; current/comparison windows are equally long. One row has previous clicks zero and current clicks 10, another has no previous group. `ingestion_complete` is null; a third result page is still pending. Expected: retain project scope, retrieve the remaining page, report no finite growth percentage for either uncertain baseline, and identify incomplete-ingestion uncertainty. Do not label observed query totals as site totals.

Scenario C: CTR opportunities report `median_ctr_by_integer_position_bucket`, sparse bucket threshold 3 and fallback values. Expected: name the heuristic/fallback limitation and propose inspection, not guaranteed extra clicks. A positive position delta means deterioration. Do not start clustering or save a brief merely because it appears in the recommendation.

Scenario D: The server returns `ANALYTICS_WINDOW_TOO_LARGE_NARROW_FILTERS`. Expected: narrow dates or exact page/query, not just result-page size. A changed-snapshot cursor causes a report restart without combining old and new pages.

Scenario E: Advanced performance tools are discovered, but the grant covers `/blog/` only. A property-day request is refused. Expected: preserve the section and use the supported page-day grain; never add daily-total markers to page details or claim query rows reconstruct property totals.

Scenario F: A 60-day decay result uses the shared product regression on 42 observed days, with explicit slope/severity thresholds. Expected: retain missing-day uncertainty, algorithm/version, source variation and evidence thresholds; distinguish the fitted decline from a causal diagnosis or forecast. Do not quietly replace it with a two-period delta.

Scenario G: One query has both a zero-click and a clicked row, so the monthly proxy counts it among zero-recorded-click identities. Expected: explain the method and denominator; do not claim the query had no clicks throughout the window, sum distinct month counts or attribute behavior to AI Overviews. Quadrant labels retain explicit thresholds and do not become revenue/uplift estimates.
