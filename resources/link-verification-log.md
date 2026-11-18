# Link verification log

Every external link in this repository, with the date it was last checked and how.
**Re-check quarterly** (see [CONTRIBUTING.md](../CONTRIBUTING.md#adding-or-replacing-a-study-link))
and update the "Links last verified" date in the [README](../README.md).

**Method codes**

- **S+F**: found by web search, then the page was fetched and its title confirmed.
- **S**: found and confirmed current by web search (title, publisher and date in results), but
  the site blocks automated fetching (HTTP 403 to non-browser clients). Open it in a browser
  at the next quarterly check.

No URL was written from memory. PDFs are linked at their official source, never copied.

## Week 1 ([study-materials](../week-1-foundations/study-materials.md))

| Topic | Role | Resource | URL | Checked | Method | Note |
|---|---|---|---|---|---|---|
| 01 Python | Core | Corey Schafer: Python OOP Tutorials – Working with Classes | https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc | 2026-11-18 | S+F | Playlist title confirmed; 6 videos (2016), content still current |
| 01 Python | Optional | Real Python: Primer on Python Decorators | https://realpython.com/primer-on-python-decorators/ | 2026-11-18 | S | Search shows the article updated Dec 2024, tagged intermediate; fetch returned 403 |
| 01 Python | Optional | pytest: Get Started | https://docs.pytest.org/en/stable/getting-started.html | 2026-11-18 | S+F | pytest 9.2.0 docs |
| 02 Data | Core | pandas: 10 minutes to pandas | https://pandas.pydata.org/docs/user_guide/10min.html | 2026-11-18 | S+F | pandas 3.1.1 docs (repo built with 2.2.3; examples compatible) |
| 02 Data | Optional | seaborn: User guide and tutorial | https://seaborn.pydata.org/tutorial.html | 2026-11-18 | S+F | seaborn 0.13.2 docs |
| 02 Data | Optional | pandas: User Guide | https://pandas.pydata.org/docs/user_guide/ | 2026-11-18 | S | Parent of the verified 10-minutes page |
| 03 Statistics | Core | StatQuest: Statistics Fundamentals | https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9 | 2026-11-18 | S+F | Playlist title confirmed |
| 03 Statistics | Optional | OpenIntro Statistics (free PDF) | https://www.openintro.org/book/os/ | 2026-11-18 | S+F | Official page; free PDF offered |
| 04 ML | Core | StatQuest: Machine Learning | https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF | 2026-11-18 | S+F | Playlist title confirmed |
| 04 ML | Optional | scikit-learn: Common pitfalls and recommended practices | https://scikit-learn.org/stable/common_pitfalls.html | 2026-11-18 | S+F | scikit-learn 1.9.1 docs |
| 04 ML | Optional | Andrew Ng: Machine Learning Specialization | https://www.coursera.org/specializations/machine-learning-introduction | 2026-11-18 | S+F | Coursera page loads |

## Week 2 ([study-materials](../week-2-advanced-llm-systems/study-materials.md))

| Topic | Role | Resource | URL | Checked | Method | Note |
|---|---|---|---|---|---|---|
| 01 LLMs | Core | Hugging Face: LLM Course | https://huggingface.co/learn/llm-course/chapter1/1 | 2026-11-18 | S+F | 12 chapters |
| 01 LLMs | Optional | Jay Alammar: The Illustrated Transformer | https://jalammar.github.io/illustrated-transformer/ | 2026-11-18 | S+F | |
| 01 LLMs | Optional | Attention Is All You Need (arXiv) | https://arxiv.org/abs/1706.03762 | 2026-11-18 | S+F | Paper, linked not copied |
| 02 RAG | Core | LangChain docs: Retrieval | https://docs.langchain.com/oss/python/langchain/retrieval | 2026-11-18 | S+F | Covers loaders, splitters, embeddings, vector stores, retrievers |
| 02 RAG | Optional | DeepLearning.AI: Building and Evaluating Advanced RAG | https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/ | 2026-11-18 | S+F | 2h05m; access terms may change |
| 02 RAG | Optional | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (arXiv) | https://arxiv.org/abs/2005.11401 | 2026-11-18 | S+F | Paper, linked not copied |
| 03 Agents | Core | Anthropic: Building effective agents | https://www.anthropic.com/engineering/building-effective-agents | 2026-11-18 | S+F | |
| 03 Agents | Optional | Lilian Weng: LLM Powered Autonomous Agents | https://lilianweng.github.io/posts/2023-06-23-agent/ | 2026-11-18 | S+F | |
| 04 LangChain/LangGraph | Core | LangGraph docs: Quickstart | https://docs.langchain.com/oss/python/langgraph/quickstart | 2026-11-18 | S+F | Docs labelled v1 |
| 04 LangChain/LangGraph | Optional | LangGraph docs: Graph API how-to | https://docs.langchain.com/oss/python/langgraph/use-graph-api | 2026-11-18 | S+F | Covers reducers; conditional edges briefly |
| 04 LangChain/LangGraph | Optional | DeepLearning.AI: AI Agents in LangGraph | https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/ | 2026-11-18 | S+F | 1h47m; reviewers note some code needs updating |
| 05 Eval & responsible | Core | Hugging Face (OpenEvals): The LLM Evaluation Guidebook | https://huggingface.co/spaces/OpenEvals/evaluation-guidebook | 2026-11-18 | S+F | Current edition per the old GitHub repo's README (Dec 2025); Space page loads (content renders client-side) |
| 05 Eval & responsible | Optional | OWASP Top 10 for LLM Applications 2025 | https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/ | 2026-11-18 | S+F | Entry names checked at https://genai.owasp.org/llm-top-10/ |

## Week 3 domain primer ([reading guide](../week-3-code-review/domain-primer/00-reading-guide.md))

| Topic | Resource | URL | Checked | Method | Note |
|---|---|---|---|---|---|
| CAGR | Corporate Finance Institute: CAGR | https://corporatefinanceinstitute.com/resources/valuation/what-is-cagr/ | 2026-11-18 | S+F | |
| Sharpe ratio | Corporate Finance Institute: Sharpe Ratio | https://corporatefinanceinstitute.com/resources/wealth-management/sharpe-ratio-definition-formula/ | 2026-11-18 | S+F | |
| Max drawdown | Corporate Finance Institute: Maximum Drawdown | https://corporatefinanceinstitute.com/resources/uncategorized/maximum-drawdown/ | 2026-11-18 | S+F | |
| Survivorship bias | Corporate Finance Institute: Survivorship Bias | https://corporatefinanceinstitute.com/resources/capital_markets/survivorship-bias/ | 2026-11-18 | S+F | |

Investopedia was considered (named in the spec) but **not used**: its pages could not be
fetched or confirmed by search on 2026-11-18. Re-evaluate at the next quarterly check.

## Reading list ([reading-list.md](reading-list.md))

| Resource | URL | Checked | Method |
|---|---|---|---|
| Karpathy: Neural Networks: Zero to Hero | https://karpathy.ai/zero-to-hero.html | 2026-11-18 | S+F |
| 3Blue1Brown: Attention in transformers, step-by-step (Deep Learning Ch. 6) | https://www.3blue1brown.com/lessons/attention | 2026-11-18 | S+F |
| mypy: Type hints cheat sheet | https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html | 2026-11-18 | S+F |
| LangChain docs: RAG with Deep Agents tutorial | https://docs.langchain.com/oss/python/langchain/rag | 2026-11-18 | S+F |
| OWASP: LLM Top 10 list page | https://genai.owasp.org/llm-top-10/ | 2026-11-18 | S+F |

## Quarterly checklist

- [ ] Fetch every URL above in a browser; confirm it loads and still matches the description.
- [ ] Re-check the level and the "watch/read this part" notes (playlists get reordered).
- [ ] Replace dead or outdated links (verify by search first; never from memory).
- [ ] Update the "Checked" dates here and the "Links last verified" date in the README.
