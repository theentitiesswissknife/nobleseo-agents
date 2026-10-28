---
name: gsc-performance-review
description: Diagnose Google Search Console performance changes and prioritize evidence-backed SEO actions from exported or connected data. Use for traffic drops, query/page opportunities, device or country comparisons, and possible query-to-page overlap; use gsc-visualization for chart-only requests.
---

# GSC performance review

## Requirements

GSC CSV/JSON exports or an already connected tool that exposes the required GSC data. This skill does not connect a Google account or add a GSC API. NobleSEO's Research MCP tools for clustering, research and briefs are not a GSC data connector. For larger tables use an available local analysis runtime; the optional `gsc-visualization` skill supplies chart scripts and lists their dependencies.

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
