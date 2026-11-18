"""Deterministic, offline stand-ins for an LLM and an embedding model.

Used by every Week 2 exercise so nothing needs an API key or network access.

- HashEmbedder: bag-of-words hashing embedder. Captures word overlap, NOT meaning
  ("refund" and "money back" are unrelated to it). Good enough to study retrieval
  mechanics; keep its limits in mind when interpreting results.
- StubLLM: a rule-based "model" with a chat interface similar to real APIs:
    * answers questions extractively from a "Context:" block in the prompt,
      or says it does not know;
    * emits tool calls (function calling) when tools are offered;
    * honours temperature deterministically via a seed.
"""
from __future__ import annotations

import json
import re
import zlib
from dataclasses import dataclass, field
from typing import Any

import numpy as np

STOPWORDS = set(
    "a an the is are was were be been to of in on for and or with by at from as it its this that "
    "what which who how when where why do does did can could should would will i you we they my your "
    "our me us please about into than then so if not no".split()
)

_WORD = re.compile(r"[a-z0-9]+(?:[-'][a-z0-9]+)*")


def tokenize(text: str) -> list[str]:
    """Lowercase word tokens (a crude stand-in for a real subword tokenizer)."""
    return _WORD.findall(text.lower())


def _stem(tok: str) -> str:
    for suffix in ("ing", "ed", "es", "s"):
        if len(tok) > 4 and tok.endswith(suffix):
            return tok[: -len(suffix)]
    return tok


def content_words(text: str) -> list[str]:
    return [_stem(t) for t in tokenize(text) if t not in STOPWORDS]


def split_sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", text) if s.strip()]


class HashEmbedder:
    """Deterministic bag-of-words embedder: words hashed into `dim` buckets, L2-normalised."""

    def __init__(self, dim: int = 512) -> None:
        self.dim = dim

    def embed(self, text: str) -> np.ndarray:
        vec = np.zeros(self.dim, dtype=np.float64)
        for w in content_words(text):
            vec[zlib.crc32(w.encode()) % self.dim] += 1.0
        norm = np.linalg.norm(vec)
        return vec / norm if norm > 0 else vec

    def embed_many(self, texts: list[str]) -> np.ndarray:
        return np.vstack([self.embed(t) for t in texts]) if texts else np.zeros((0, self.dim))


@dataclass
class ToolCall:
    name: str
    arguments: dict[str, Any]
    id: str = ""


@dataclass
class ChatResponse:
    content: str = ""
    tool_calls: list[ToolCall] = field(default_factory=list)


def _overlap(a: str, b: str) -> int:
    return len(set(content_words(a)) & set(content_words(b)))


class StubLLM:
    """Rule-based chat model. Deterministic for a given (input, temperature, seed)."""

    def __init__(self, seed: int = 0) -> None:
        self.seed = seed

    # ---- plain completion ------------------------------------------------------------
    def complete(self, prompt: str, temperature: float = 0.0) -> str:
        if "Context:" in prompt and "Question:" in prompt:
            return self._answer_from_context(prompt, temperature)
        if prompt.lower().startswith("summarize:"):
            sents = split_sentences(prompt.split(":", 1)[1])
            return " ".join(sents[:2]) if sents else ""
        if prompt.lower().startswith("classify sentiment:"):
            text = prompt.split(":", 1)[1].lower()
            pos = sum(w in text for w in ("great", "good", "fast", "love", "thanks", "excellent"))
            neg = sum(w in text for w in ("late", "bad", "cold", "missing", "never", "worst", "refund"))
            return "positive" if pos > neg else "negative" if neg > pos else "neutral"
        return "I can only answer questions about the provided context."

    def _answer_from_context(self, prompt: str, temperature: float) -> str:
        context = prompt.split("Context:", 1)[1].split("Question:", 1)[0]
        question = prompt.split("Question:", 1)[1].split("\n", 1)[0]
        scored = sorted(
            ((_overlap(s, question), i, s) for i, s in enumerate(split_sentences(context))),
            key=lambda t: (-t[0], t[1]),
        )
        if not scored or scored[0][0] < 2:
            return "I don't know based on the provided context."
        if temperature > 0:
            # Higher temperature -> sample among more candidate sentences.
            k = min(len(scored), 1 + int(temperature * 3))
            rng = np.random.default_rng(self.seed + zlib.crc32(question.encode()))
            return scored[int(rng.integers(0, k))][2]
        return scored[0][2]

    # ---- chat with function calling ---------------------------------------------------
    def chat(self, messages: list[dict], tools: list[dict] | None = None) -> ChatResponse:
        """messages: [{"role": "user"|"assistant"|"tool", "content": str, "name"?: str}]
        tools: [{"name", "description", "parameters": {param: "number"|"string"}}]
        Calls each relevant tool at most once, then answers using the tool results.
        """
        user_msgs = [m for m in messages if m["role"] == "user"]
        question = user_msgs[-1]["content"] if user_msgs else ""
        last_user_idx = max(i for i, m in enumerate(messages) if m["role"] == "user") if user_msgs else -1
        tool_msgs = [m for m in messages[last_user_idx + 1 :] if m["role"] == "tool"]
        called = {m.get("name") for m in tool_msgs}

        if tools:
            ranked = sorted(tools, key=lambda t: -_overlap(t["description"], question))
            for tool in ranked:
                if tool["name"] in called or _overlap(tool["description"], question) < 2:
                    continue
                args = self._extract_args(question, tool.get("parameters", {}))
                if args is not None:
                    return ChatResponse(tool_calls=[ToolCall(tool["name"], args, id=f"call_{len(called)}")])
        if tool_msgs:
            facts = "; ".join(f"{m.get('name')} -> {m['content']}" for m in tool_msgs)
            return ChatResponse(content=f"Based on the tool results ({facts}), here is the answer.")
        return ChatResponse(content="I could not find a tool for that, so I cannot answer reliably.")

    @staticmethod
    def _extract_args(question: str, params: dict[str, str]) -> dict[str, Any] | None:
        args: dict[str, Any] = {}
        numbers = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", question)]
        ids = re.findall(r"\b[A-Z]{1,3}-\d+\b", question)
        for name, kind in params.items():
            if kind == "number":
                if not numbers:
                    return None
                args[name] = numbers.pop(0)
            elif name.endswith("_id"):
                if not ids:
                    return None
                args[name] = ids.pop(0)
            elif name == "expression":
                m = re.search(r"[-\d.\s()+*/]{3,}", question)
                if not m:
                    return None
                args[name] = m.group(0).strip()
            else:
                args[name] = question
        return args


def tool_result_message(call: ToolCall, result: Any) -> dict:
    return {"role": "tool", "name": call.name, "tool_call_id": call.id, "content": json.dumps(result)}
