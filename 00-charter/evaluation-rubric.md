# Evaluation rubric

Shared with the intern on Day 1. Every dimension is scored on a 1–4 scale with the written
descriptors below. Scores are based on evidence collected across all four weeks (check-ins,
progress log, Week 3 reviews, Week 4 tasks and demo).

## Dimensions and weights

| # | Dimension | What it covers | Weight (default, adjustable) |
|---|---|---|---|
| 1 | **Learning** | How fast you absorb context and tools | 25% |
| 2 | **Technical quality** | Correctness, tests, clarity | 25% |
| 3 | **Initiative** | Asks good questions, proposes ideas, unblocks yourself | 20% |
| 4 | **GenAI judgment** | Uses GenAI effectively and verifies outputs | 15% |
| 5 | **Communication and readiness to contribute** | Updates, docs, demo | 15% |

Weights may be adjusted by the mentor **before Day 1 only**, and any change is shared with
the intern on Day 1.

## Scale

| Score | Label | Meaning |
|---|---|---|
| 4 | Exceeds | Consistently above what is expected of an intern at this stage |
| 3 | Meets | Solid and reliable at the expected level |
| 2 | Developing | Partly there; needs regular support |
| 1 | Not yet | Significant gaps; not at the expected level |

## Descriptors

### 1. Learning (25%)

| Score | Descriptor |
|---|---|
| 4 | Picks up new concepts quickly, connects them across topics (e.g. links leakage in Week 1 to look-ahead bias in the primer), and applies them unprompted in later weeks. |
| 3 | Understands each week's material, answers check-in questions correctly, applies concepts in tasks with little prompting. |
| 2 | Understands the basics but struggles to apply them; needs concepts re-explained or examples to proceed. |
| 1 | Key concepts remain unclear by the end of the week; repeats the same misunderstandings. |

### 2. Technical quality (25%)

| Score | Descriptor |
|---|---|
| 4 | Code is correct, tested, readable and well structured; edge cases handled; results verified against independent checks. |
| 3 | Code is correct and readable with reasonable tests; minor issues only. |
| 2 | Code mostly works but has correctness gaps, little testing, or is hard to follow. |
| 1 | Code is frequently incorrect or untested; results not checked. |

### 3. Initiative (20%)

| Score | Descriptor |
|---|---|
| 4 | Asks sharp, well-researched questions; proposes improvements; unblocks self through docs, experiments and debugging before escalating; goes beyond the brief where it adds value. |
| 3 | Asks questions when stuck after trying first; occasionally proposes ideas; manages own time. |
| 2 | Waits to be told; asks questions without trying first, or stays stuck too long without asking. |
| 1 | Rarely asks or proposes anything; frequently blocked. |

### 4. GenAI judgment (15%)

| Score | Descriptor |
|---|---|
| 4 | Uses GenAI to go faster on the right tasks; always verifies (tests, docs, re-running); catches and corrects wrong AI output; discloses use fully; never pastes restricted data. |
| 3 | Uses GenAI sensibly, verifies most output, discloses use. |
| 2 | Accepts AI output with little verification, or discloses inconsistently. |
| 1 | Submits unverified AI output as own work, does not disclose, or breaks data rules. A data-rule breach is scored 1 regardless of other evidence. |

### 5. Communication and readiness to contribute (15%)

| Score | Descriptor |
|---|---|
| 4 | Clear, concise updates; excellent docs and READMEs; demo is well structured and handles questions confidently and honestly ("I don't know, here is how I'd find out"). |
| 3 | Regular, clear updates; adequate docs; demo covers the work and answers most questions. |
| 2 | Updates irregular or unclear; docs thin; demo hard to follow. |
| 1 | Little communication; no docs; cannot explain own work. |

## Computing the overall score

```
overall = Σ (score_i × weight_i)        # range 1.00–4.00
```

Example: Learning 3, Technical 3, Initiative 4, GenAI 3, Communication 2 →
`3×0.25 + 3×0.25 + 4×0.20 + 3×0.15 + 2×0.15 = 3.05`.

The overall score informs, but does not by itself decide, the go/no-go outcome. See
[go-no-go-criteria.md](go-no-go-criteria.md).

## What is not scored

How much routine work you completed. A smaller amount of work that is correct, verified and
well explained scores higher than a large amount of unverified work.
