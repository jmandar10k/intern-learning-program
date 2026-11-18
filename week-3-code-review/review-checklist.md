# Review checklist

Use this on every exercise. A tick means you actually checked, not that you assumed.

## 1. Before reading the code

- [ ] I read `expected-behavior.md` and wrote down what "correct" looks like in numbers.
- [ ] I ran the program and saved the output.
- [ ] I listed every difference between the output and the expected behavior.
- [ ] I asked: is any number **too good to be true** or **too round**?

## 2. Data

- [ ] Row counts before and after every load, filter, join and groupby.
- [ ] Join keys are unique where they should be (`validate=`); no unexpected duplicates.
- [ ] Missing values: how are they handled, and is that handling correct for the meaning of the column?
- [ ] Aggregations group by the right column and reconcile with the raw totals.
- [ ] I read the data dictionary, if there is one, for every column used.

## 3. ML evaluation

- [ ] The split happens **before** any fitted preprocessing (scalers, imputers, encoders, selectors).
- [ ] Every feature would be available at prediction time (no target or post-outcome leakage).
- [ ] The metric matches the class balance and the business goal; there is a baseline.
- [ ] Metric arguments (e.g. `average=`, `pos_label=`) do what the label says.

## 4. Retrieval and LLM pipelines

- [ ] Chunking covers all of the text; chunk size and overlap are sensible.
- [ ] Similarity vs distance: sorting direction is right; vectors normalized if cosine is assumed.
- [ ] Every prompt is fully rendered: no unfilled `{placeholders}`, right variable in the right slot.
- [ ] Values used in a loop come from the **current** iteration, not an earlier one.
- [ ] Temperature and sampling settings fit each step (deterministic where correctness matters).

## 5. Agents and workflows

- [ ] Tool results are passed back to the model, unchanged.
- [ ] The loop continues until the task is done (or a limit is hit), not after the first call.
- [ ] Every claim in the final answer is backed by a tool result in the trace.
- [ ] State updates merge where they should (reducers) and overwrite only where intended.
- [ ] Every conditional edge sends each kind of input to the intended branch.

## 6. Fix and verify

- [ ] Smallest correct fix; I can explain each changed line.
- [ ] Output now matches `expected-behavior.md` **for the right reason**.
- [ ] I added a test, assert or sanity check that fails on the buggy version and passes on the fix.
- [ ] I kept looking for a second, subtler bug after the first fix.
