# ex07: expected behavior

**Goal of the script:** publish valid documents with personal data removed; hold invalid
documents back.

## What correct output looks like

| Doc | Status | Steps |
|---|---|---|
| D1 Quarterly volunteer report | published | validate → detect_pii → enrich → **redact** → summarize |
| D2 Library opening hours | published | validate → detect_pii → enrich → summarize |
| D3 (untitled) | **quarantined** | validate → quarantine |
| D4 Park cleanup sign-up | published | validate → detect_pii → enrich → **redact** → summarize |
| D5 Pool maintenance notice | **quarantined** | validate → quarantine |
| D6 Community garden rules | published | validate → detect_pii → enrich → **redact** → summarize |

- **No published summary contains an email address** (D1 and D4 show `[REDACTED]`).
- `meta` for published documents contains both the PII findings and the enrichment fields
  (`pii`, `word_count`, `reading_minutes`).

## Sanity checks you can run

- Stream the graph (`app.stream(..., stream_mode="updates")`) and compare each node's update with
  the final state.
- For each conditional edge, list inputs that should take each branch, and test them.
