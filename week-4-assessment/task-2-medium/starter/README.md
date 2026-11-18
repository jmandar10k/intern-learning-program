# Starter: offline model stubs

`llm_stubs.py` is the same module used in Week 2. Import it from your code:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "starter"))  # adjust to your layout
from llm_stubs import HashEmbedder, StubLLM, content_words, split_sentences
```

| Component | Behavior |
|---|---|
| `HashEmbedder().embed(text)` | L2-normalized hashed bag-of-words vector. Captures word overlap, not meaning. |
| `StubLLM().complete(prompt)` | If the prompt contains `Context:` and `Question:`, returns the context sentence with the highest word overlap with the question, or "I don't know based on the provided context." when overlap is very low. |
| `content_words`, `split_sentences` | Helpers used by the stubs. |

The stubs are deterministic, so your results are reproducible. You may copy and adapt them,
but say so in your README.
