# Contributing (mentors)

How mentors keep this program current and log feedback.

## Updating content

| What | Where | Rule |
|---|---|---|
| Theory notes | `week-N-*/NN-topic/notes.md` | Keep the "After this topic you can" list in sync with [00-charter/learning-objectives.md](00-charter/learning-objectives.md) |
| Runnable exercises | `week-N-*/NN-topic/exercises/` | Must run offline in < 1 minute on a laptop. No API keys, no network |
| Study links | `week-N-*/study-materials.md` | Hard cap: 1 core + 2 optional per topic. Verify by web search before adding, then log it |
| Week 3 exercises | `week-3-code-review/exercises/` | Each must run with **no error and no warning that points at the bug**, yet give wrong output. Keep the mentors' answer key (held outside this repository) in sync |
| Week 4 tasks | `week-4-assessment/task-*/` | Keep the mentors' reference solutions (held outside this repository) in sync with `acceptance-criteria.md` |
| Rubric weights | [00-charter/evaluation-rubric.md](00-charter/evaluation-rubric.md) | Change before Day 1 only; never mid-program |

## Adding or replacing a study link

1. Search for the resource; open the page and confirm it loads, is maintained and is at the
   right level (intermediate for Week 1, advanced for Week 2).
2. Never write a URL from memory. Never copy a PDF into the repo: link to the official source.
3. Add it to the topic's table in `study-materials.md` with: role (core/optional), level, time
   estimate, "watch/read this part" note and a one-line reason.
4. Add a row to [resources/link-verification-log.md](resources/link-verification-log.md) with
   today's date and how it was checked.
5. Update the "Links last verified" date in [README.md](README.md) if you re-checked all links.

**Quarterly checklist:** re-check every link in the verification log and replace dead ones.

## Logging feedback

- At the end of Weeks 1–3, run the check-in with
  [assessment/weekly-checkin-template.md](assessment/weekly-checkin-template.md).
- Copy the filled check-in into the mentor section of `progress-log/week-N-log.md`.
- Record action items with an owner and a due date. Review open action items at the start of
  the next check-in.
- Week 4: fill [assessment/task-scoring-sheet.md](assessment/task-scoring-sheet.md), run the
  demo with [assessment/final-demo-qa-guide.md](assessment/final-demo-qa-guide.md), then
  complete [assessment/four-week-review-template.md](assessment/four-week-review-template.md).
- Write evidence, not impressions: "Explained why the scaler must be fit on train only, without
  prompting" beats "good understanding".
