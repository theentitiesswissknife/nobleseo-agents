---
name: gsc-performance-review
description: Diagnose Google Search Console performance changes and prioritize evidence-backed SEO actions from exported or connected data. Use for traffic drops, query/page opportunities, device or country comparisons, and possible query-to-page overlap; use gsc-visualization for chart-only requests.
---

# GSC performance review

## Requirements

GSC CSV/JSON exports or an already connected tool that exposes the required GSC data. Discover the available MCP tools before choosing a path: installing this skill does not deploy server tools, connect Google, or extend an OAuth grant. For larger tables use an available local analysis runtime; the optional `gsc-visualization` skill supplies chart scripts and lists their dependencies.

## NobleSEO Analytics path (when available)

The Analytics server increment requires an explicitly granted `analytics.read` scope. Earlier Research MCP deployments expose clustering, research and briefs only. If the tools below are absent, use supplied exports or another authorized connector; do not call invented tools or claim that reinstalling the skill enables analytics.

1. Select an authorized project and call `analytics_get_project_site`. The server resolves the property and any project section; do not substitute a broader property.
2. Choose explicit past dates, at most 90 days, and call `analytics_get_data_status`. `observed_days` describes rows seen, not verified ingestion completeness. `no_observed_data` is not evidence of zero traffic.
3. Call `analytics_report_query_performance` with `dimension` set to `page`, `query`, `page_query` or `date`. Retain the exact page/query filters and follow every `next_cursor`. These are persisted web-search query/page rows, not whole-property totals or live Google data. This increment does not expose device, country, GA4 or conversion reports.
4. For changes, call `analytics_compare_query_performance` with equal-length, non-overlapping earlier comparison dates and a page/query dimension. A missing group stays unknown; zero-baseline percent change stays null. CTR is a ratio, and its delta multiplied by 100 is percentage points. Positive position delta means worse ranking.
5. Optionally use `analytics_find_ctr_opportunities`. Preserve its method, population and thresholds. Its existing detector uses position-bucket medians with a fixed fallback for sparse buckets; the score is a prioritization heuristic, not a forecast or measured causal effect. Rows missing required metrics are excluded and counted.

If the server returns `ANALYTICS_WINDOW_TOO_LARGE_NARROW_FILTERS`, narrow the dates or exact page/query; do not retry the same request with a smaller output page and assume that fixes source size. If a cursor snapshot changes, restart the same report and discard the earlier partial result. If data is unavailable, report that limitation without silently fetching live Google data or starting a backfill.

## Stored performance, trends and decay (when discovered)

Discover `analytics_report_performance` and `analytics_compare_performance` before using them. Select the declared `property_day` or `page_day` grain. Property-day totals use the stored daily-total markers; page-day results use the separate page breakdown. Do not add markers to page details or reconstruct a property total from query rows. A section grant cannot read property totals; retain the section and use page-day evidence. Comparison dates have equal duration and do not overlap, with daily rows aligned by offset; missing days stay unknown and zero-baseline relative changes stay null.

For a trend or decay question, discover `analytics_get_content_trends` and `analytics_analyze_content_decay`. Their current schemas require 30–180 explicit past days, attainable minimum observation counts and declared metric thresholds. Preserve the returned algorithm/version, observed dates, regression significance and severity thresholds. The active product regression is shared, while this scoped mode uses stored web observations and declared weighted daily aggregation because the legacy aggregate cannot isolate search type. Do not mix these results with another algorithm or population as if they were equivalent. Missing days are not zero-filled. A fitted decline is a signal to investigate; it does not identify the cause, prove a content defect or forecast recovery.

`analytics_analyze_zero_click` returns a proxy with monthly distinct query/page denominators. In the current method an identity qualifies when any observed row records zero clicks; another row for it may have clicks. Distinct identities cannot be summed across months. Preserve unavailable history/correlations, missing observations and privacy limits. Do not label this as measured zero-click SERP behavior or attribute it to AI Overviews.

`analytics_get_opportunity_quadrant` classifies stored page sums with explicit impression and CTR thresholds. CTR is a ratio, and the default 1% threshold is a classification choice. Retain the thresholds, grouping/population and raw metrics. A quadrant label is not expected uplift or measured business impact. The current scoped mode does not load property-wide saved groups.

These tools perform no sync, materialization, acquisition or provider action. Device/country/search-appearance dimensions are unavailable unless a separately discovered contract declares a supported disjoint grain. Do not infer them from the performance or trend results. If a required tool is missing, use the earlier query-data or authorized-export path and state which analysis remains unavailable.

## Stored segments and rank history (when discovered)

Discover `analytics_report_segments` and its closed mode schema before use. It requires `analytics.read`, explicit past dates within 90 days and one granted project. GSC modes use bounded joint web-search observations after project section filtering, with no synchronization or materialization. Follow every cursor without mixing snapshots. The source limit is 25,000 rows before section filtering; a heatmap also bounds the complete report to 100,000 cells and returns at most 100 cells per page. Narrow dates, exact page/query or the supported minimum total after a work-bound refusal; a smaller output page does not reduce source work.

`ranking_distribution` retains the native raw-row counts in its exclusive buckets; they are not distinct query counts. Its native residual 21+ bucket also contains fractional interval gaps and missing/zero positions, so do not describe every residual observation as a rank greater than twenty. `branded` requires up to twenty explicit literal aliases, matched case-insensitively; never infer brand names from the domain. Clicks/impressions partition disjoint rows, while distinct query counts cannot be summed across dates. Preserve missing metrics and null CTR denominators.

`group_heatmap` accepts up to twenty explicit caller-defined groups with bounded native contains/equals/regex conditions, inclusions and exclusions. Retain their exact definitions, dimension and metric. Native contains uses SQL wildcard semantics, equals is case-sensitive, regex is case-insensitive, exclusions veto a group, and the first match wins under descending native specificity; caller order resolves ties. Other contains unmatched rows. These are requested definitions, not a discovered property-wide saved group library. `performance_heatmap` supports daily query/page cells for clicks or impressions with an explicit minimum total. Do not invent device/country or weekly/monthly dimension sources. Preserve each cell's observation label: native group calendars fill missing cells with imputed zeros; performance calendars use imputed zeros inside observed dates and nulls for unobserved dates. Neither fill establishes confirmed zero traffic.

`rank_history` additionally requires `content.read`, current article visibility and one exact article in the selected project. It reads stored tracking observations in the selected inclusive UTC dates without requiring or opening a GSC connection. Retain engine, device, location and time separately; positions across different observations are not additive. Do not join them to GSC query metrics, infer a fresh SERP check, start tracking or acquire domain ratings. Missing history remains unknown. A moved article or revoked grant refuses the read. This mode does not expose the article body or private provider payloads.

## Establish what can be compared

Identify the property, requested question, current and comparison dates, search type, filters and row grain. Record extraction time and data completeness when supplied. Prefer comparable complete periods, including weekday alignment; use a year-over-year comparison when available and relevant to seasonality. If the supplied dates are partial or mismatched, state the limitation rather than quietly treating them as equivalent.

Inspect columns and coverage before calculating. Distinguish property/day totals, query aggregates, page aggregates and joint query-page rows. Separate query and page exports cannot be joined to prove which page ranked for a query. A top-N export, filtered query table or omitted anonymized queries is not the whole property. Do not turn an absent row into zero unless the data contract establishes a complete observation.

## Calculate reproducibly

- Sum additive clicks and impressions only over disjoint observations at the selected grain. Do not combine alternative dimension reports, totals with detail rows, or overlapping exports.
- Recompute CTR as total clicks / total impressions, using one consistent percentage convention. Report CTR changes in percentage points and label relative changes separately. A zero denominator is unavailable, not 0%.
- When aggregation is appropriate within the same report/grain, use impressions to weight position. Lower position is better. Do not average row CTRs or positions equally, and do not claim a reconstructed position equals Google's property-level aggregate across different aggregation types.
- Show absolute changes as well as relative changes. A zero comparison value has no finite percent growth. Preserve missing values and state the portion of data covered.
- Save calculations or a small reproducible analysis alongside the result when table size or arithmetic warrants it. Reuse available local analysis tools; do not start a new data service.

## Diagnose and prioritize

First quantify the change at the best supported scope. Break it down by page/query, device, country or search appearance only where supplied, retaining consistent dates and filters. Show contributions to the observed click change; do not present the largest percentage change on a tiny base as the main driver.

Separate evidence from explanations:

- Falling impressions may reflect demand, coverage or visibility changes; GSC alone does not distinguish all of them.
- Lower CTR with similar position can justify inspecting snippets and SERP changes, but does not prove that a title caused the decline. Account for changes in query, country and device mix.
- Worse average position can be a distribution change, not a uniform ranking loss. Inspect sufficiently supported segments before proposing action.
- For high-impression queries/pages, compare CTR against the site's own comparable position/device/query-type cohorts when possible. If that evidence is missing, suggest investigation instead of applying a universal CTR curve or promising extra clicks.
- Brand/non-brand classification needs an explicit brand/alias definition or a clearly stated proposal. Keep ambiguous terms separate.
- Multiple pages associated with a query are overlap candidates, not proof of harmful cannibalization. Require joint query-page evidence and, for a switching claim, a time dimension. Recommend inspecting intent and page roles before any consolidation.

Do not infer conversions, revenue or return on investment from GSC alone. GA4 or commercial data needs its own compatible scope and attribution caveats. Correlation with an update or site edit is not proof of cause.

Deliver a concise diagnosis and a prioritized action table: affected page/query or segment, observed evidence and period, proposed action, confidence/limitation, and the next validation step. Use qualitative priority tied to scale and confidence; avoid a fabricated precision score. If asked for a forecast, label assumptions and uncertainty rather than presenting a causal or guaranteed gain.

Use `gsc-visualization` for a chart when it clarifies the conclusion; pass an already correctly aggregated table. Hand a user-selected keyword set to `keyword-clustering`, or an agreed page/topic to `seo-content-briefing`, only if those skills and tools are available. GSC impressions are not keyword search volume. Research spending, website edits and publishing do not follow automatically from a diagnostic recommendation.
