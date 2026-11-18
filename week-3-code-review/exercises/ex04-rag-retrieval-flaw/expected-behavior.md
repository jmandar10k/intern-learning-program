# ex04: expected behavior

**Goal of the script:** answer CloudNote help questions from the help articles.

## What correct output looks like

- For **every** question in `data/eval_queries.json`, the article listed in `relevant` is among the
  retrieved sources (**recall@3 = 1.0**).
- **Every** answer contains the text in `answer_contains`, for example:
  - "How often does CloudNote sync…" → "…every five minutes."
  - "How many collaborators … on the Free plan?" → "…up to 3 on the Free plan."
  - "Which attachments are excluded from exports?" → "Attachments larger than 50 MB are excluded from exports."
  - "Is text inside scanned PDFs searchable?" → "…searchable on the Team plan through optical character recognition."
- Answers are complete sentences from the right article, not fragments.
- Every word of every article appears in at least one chunk.

## Sanity checks you can run

- Print the similarity scores of the retrieved chunks: are they the highest ones?
- Reconstruct an article from its chunks: is anything missing?
- Compute recall@3 and answer accuracy over the eval file.
