# GSC performance evaluation

Run each synthetic scenario in Codex and Claude Code. Do not fetch live account data. Evaluate calculations and proposed decisions, not matching prose.

## Weighted comparison

Request: "Diagnose the change and tell me what to inspect first. These are complete, disjoint device rows for the same property, web search, no filters, two complete comparable weeks."

| Period | Device | Clicks | Impressions | Position |
| --- | --- | ---: | ---: | ---: |
| Previous | Mobile | 90 | 900 | 8 |
| Previous | Desktop | 10 | 100 | 2 |
| Current | Mobile | 45 | 900 | 8 |
| Current | Desktop | 15 | 100 | 2 |

Expected: clicks 100 to 60 (-40, -40%); impressions unchanged at 1,000; CTR 10% to 6% (-4 percentage points); weighted position 7.4 in both periods. Mobile contributes -45 clicks and desktop +5. Prioritize mobile CTR investigation; do not assert a title change, algorithm update or ranking loss caused the drop. Do not forecast conversions or guaranteed recoverable clicks.

## Insufficient grain and coverage

Request: "Prove cannibalization and total traffic loss from these top-10 query and top-10 page exports. They are separate tables; there are no joint query-page or date rows."

Expected: explain that the requested proof and property total cannot be derived. Offer supported observations and request joint query-page/date data for a switching analysis. Do not join by row position, treat missing rows as zero or label all overlap harmful.

## Zero denominator and no connector

Request: "Compare an example query with 0 clicks/0 impressions last period and 2 clicks/10 impressions now, then fetch fresh GSC data through NobleSEO."

Synthetic tool catalogue contains only NobleSEO clustering/research/brief tools.

Expected: current CTR 20%, previous CTR unavailable, click delta +2, relative growth undefined. Explain that no GSC connector is exposed and ask for an export or actual connected GSC source. Do not pass the request to research_start or interpret impressions as search volume.
