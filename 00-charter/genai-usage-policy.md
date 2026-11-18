# GenAI usage policy

Shared with the intern on Day 1. GenAI tools (chat assistants, coding assistants, code
completion) are **allowed and encouraged** throughout the program, under three rules:
**verify, disclose, protect data.** How well you follow them is scored under "GenAI judgment"
in the [evaluation rubric](evaluation-rubric.md).

## 1. Verify

You are responsible for every line you submit, whoever or whatever wrote it.

- **Run it.** Never submit code you have not executed. Check the output, not just that it ran.
- **Test it.** Add at least one test or sanity check for any non-trivial AI-generated function.
- **Check claims against a primary source.** API signatures, library behavior and numbers
  quoted by an assistant must be checked against official docs or by experiment. LLMs invent
  plausible-looking function names, parameters, citations and URLs.
- **Be suspicious of fluent answers.** Week 3 is built on code that looks right and runs cleanly
  but is wrong. AI output has the same failure mode.
- **Understand it.** If you cannot explain a piece of code in the demo, it counts against you,
  whether or not an AI wrote it.

## 2. Disclose

Add a short **GenAI disclosure** to every submission (Week 3 reviews, Week 4 tasks):

```markdown
## GenAI disclosure
- Tool(s): <e.g. chat assistant, IDE completion>
- Used for: <e.g. drafting the chunking function; explaining MRR; writing test scaffolding>
- What I changed or rejected: <e.g. the suggested overlap logic was off by one; fixed and tested>
- How I verified: <tests run, docs checked, outputs compared>
```

"None" is a valid answer. Undisclosed use discovered later is treated as a serious issue.

## 3. Protect data: never paste into an external tool

- Credentials of any kind: API keys, passwords, tokens, connection strings, private keys.
- Personal data about real people (customers, colleagues, yourself beyond what is needed).
- Company-confidential material: internal code, documents, designs, strategies, client
  names, non-public financial data, anything marked internal or confidential.

The synthetic data and code in this repository contain no confidential
material and may be pasted into GenAI tools. When in doubt, ask your mentor first.

A breach of these data rules scores 1 on GenAI judgment and is a no-go criterion (see
[go-no-go-criteria.md](go-no-go-criteria.md)).

## Good uses

- Explaining a concept a second way after reading the core resource.
- Generating test cases you then check by hand.
- Drafting boilerplate (argument parsing, plotting code) you then read line by line.
- Rubber-ducking a bug: describe symptoms, then verify any suggested cause by experiment.

## Poor uses

- Pasting a Week 3 exercise and submitting the answer without reproducing the symptom yourself.
- Asking for a "full solution" to a Week 4 task and editing it lightly.
- Citing a URL, paper or number from an assistant without opening the source.
