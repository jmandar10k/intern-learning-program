# Week 1 self-check quiz

Ungraded. Answer in your own words in [progress-log/week-1-log.md](../progress-log/week-1-log.md)
before the Week 1 check-in; your mentor will discuss your answers with you. Aim for 2–4
sentences each. Try without GenAI first; if you use it afterwards to check, say so.

## Python advanced

1. What is the difference between an iterable, an iterator and a generator? What happens if you
   loop over the same generator twice, and why is that dangerous?
2. Write (on paper) a decorator `@log_calls` that prints the function name and arguments. Why do
   you need `functools.wraps`?
3. When would you use `Protocol` instead of an abstract base class?
4. What does `@pytest.mark.parametrize` give you that a loop inside a test does not?
5. Why does a `src/` layout help catch packaging mistakes?

## Data analysis and visualization

6. You merge orders (2,000 rows) with a stores table and get 2,140 rows. List two possible causes
   and how you would confirm each.
7. Give an example where `fillna(0)` is correct and one where it silently corrupts the analysis.
8. The overall late rate is 24.4%, but the mean of the four zone late rates is 25.8%. Why are
   they different, and which one is "right"?
9. Which plot would you use to show late rate by zone and hour? What extra information must
   accompany it so it is not misleading?

## Statistics

10. Explain a p-value of 0.03 to a non-technical colleague without saying "probability the
    hypothesis is true".
11. Rain orders are late 38% of the time vs 21% when dry (p < 0.001). Does rain cause lateness?
    What else could explain it?
12. You test 40 customer segments and find 3 with p < 0.05. What do you conclude?
13. When would you prefer Spearman over Pearson correlation?
14. Describe Simpson's paradox with an example of your own.

## ML algorithms and evaluation

15. A model reaches 0.999 ROC-AUC on the test set on the first try. List what you check first.
16. Why must a `StandardScaler` be fit on training data only? What is the tool that makes this
    automatic in cross-validation?
17. Your dataset is 95% class 0. Which metrics would you report and why not accuracy?
18. Explain the difference between macro-F1 and micro-F1. Which one hides poor performance on
    a minority class?
19. When is a random train/test split wrong? Give two cases and the right split for each.
20. Random forest vs gradient boosting: one strength and one risk of each.

## Reflection

- Which topic took longest, and why?
- One question you still have.
