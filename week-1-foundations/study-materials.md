# Week 1 study materials

**Rule:** each topic has **1 core** resource (do it) and **up to 2 optional** deep dives (only if
time allows). Level for this week: **intermediate**. Read the topic's `notes.md` first; it tells
you what to focus on.

All links were found and checked by web search on **2026-11-18**. See
[resources/link-verification-log.md](../resources/link-verification-log.md). If a link is dead,
tell your mentor; do not substitute a random one.

## 01 Python advanced

| Role | Resource | Level | Time | Watch/read this part | Why |
|---|---|---|---|---|---|
| Core | [Corey Schafer: Python OOP Tutorials – Working with Classes (YouTube playlist)](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) | Intermediate | ≈1.5 h | All 6 videos (classes, class variables, class/static methods, inheritance, dunder methods, property decorators) | Clear, compact OOP refresher; afterwards you can design small class hierarchies with properties and dunder methods. |
| Optional | [Real Python: Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/) | Intermediate | ≈1 h | Sections up to and including "Decorators with arguments" | Afterwards you can write decorators with `functools.wraps` and arguments. |
| Optional | [pytest: Get Started](https://docs.pytest.org/en/stable/getting-started.html) | Intermediate | ≈30 min | Whole page | Afterwards you can write and run tests, use fixtures and `pytest.raises`. |

## 02 Data analysis and visualization

| Role | Resource | Level | Time | Watch/read this part | Why |
|---|---|---|---|---|---|
| Core | [pandas: 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) | Intermediate | ≈1.5 h (typing along) | Whole page; type every example | Afterwards you can select, filter, group, merge and reshape DataFrames fluently. |
| Optional | [seaborn: User guide and tutorial](https://seaborn.pydata.org/tutorial.html) | Intermediate | ≈1.5 h | "Overview of seaborn plotting functions", "Visualizing distributions", "Visualizing statistical relationships" | Afterwards you can pick the right plot for a distribution or relationship. |
| Optional | [pandas: User Guide](https://pandas.pydata.org/docs/user_guide/) | Intermediate | ≈1 h | "Merge, join, concatenate and compare", "Group by", "Working with missing data" | The three areas where silent data bugs most often come from. |

## 03 Statistics

| Role | Resource | Level | Time | Watch/read this part | Why |
|---|---|---|---|---|---|
| Core | [StatQuest: Statistics Fundamentals (YouTube playlist)](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9) | Intermediate | ≈2.5 h | Videos on histograms, distributions, normal distribution, mean/variance/SD, sampling, hypothesis testing and null hypothesis, p-values (and how not to misuse them), confidence intervals, covariance and correlation | Intuition first; afterwards you can explain a p-value and a confidence interval correctly. |
| Optional | [OpenIntro Statistics (free PDF from the official site)](https://www.openintro.org/book/os/) | Intermediate | ≈2 h | Ch. 1 (data and sampling, bias), Ch. 5 (foundations for inference) | Rigorous reference with exercises; link only, do not copy the PDF into the repo. |

## 04 ML algorithms and evaluation

| Role | Resource | Level | Time | Watch/read this part | Why |
|---|---|---|---|---|---|
| Core | [StatQuest: Machine Learning (YouTube playlist)](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) | Intermediate | ≈3 h | Gentle intro, cross validation, confusion matrix, sensitivity/specificity, bias and variance, ROC and AUC, linear regression, decision trees, random forests, AdaBoost, gradient boost (part 1), k-means | Covers this week's algorithms and metrics with strong intuition. |
| Optional | [scikit-learn: Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html) | Intermediate | ≈45 min | Whole page | Data leakage and inconsistent preprocessing, with pipeline fixes. Directly relevant to Weeks 3 and 4. |
| Optional | [Andrew Ng: Machine Learning Specialization (Coursera)](https://www.coursera.org/specializations/machine-learning-introduction) | Intermediate | Pick ≈2 h | Course 2, week on decision trees and tree ensembles; Course 3, week on clustering | Structured lectures if you prefer a course format. Check Coursera for current access options; do not pay for it without asking your mentor. |
