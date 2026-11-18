"""Document publishing workflow for a community-services newsletter (LangGraph).

Each submitted document goes through:
  validate -> (quarantine if invalid)
           -> detect_pii -> enrich -> (redact if PII found) -> summarize -> publish
Published summaries are shown on a public page, so personal data (e.g. email addresses)
must never appear in them.

Needs: langgraph (runs fully offline).
Run:  python main.py
"""
from __future__ import annotations

import json
import operator
import re
from pathlib import Path
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph

DATA = Path(__file__).parent / "data" / "documents.json"
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")


class DocState(TypedDict):
    doc: dict
    errors: list[str]
    meta: dict
    text: str
    summary: str
    status: str
    steps: Annotated[list[str], operator.add]


def validate(state: DocState) -> dict:
    doc, errors = state["doc"], []
    if not doc.get("title", "").strip():
        errors.append("missing title")
    if len(doc.get("body", "").split()) < 5:
        errors.append("body too short")
    return {"errors": errors, "text": doc.get("body", ""), "steps": ["validate"]}


def quarantine(state: DocState) -> dict:
    return {"status": "quarantined", "steps": ["quarantine"]}


def detect_pii(state: DocState) -> dict:
    found = EMAIL.findall(state["text"])
    return {"meta": {"pii": found}, "steps": ["detect_pii"]}


def enrich(state: DocState) -> dict:
    words = state["text"].split()
    return {"meta": {"word_count": len(words), "reading_minutes": max(1, round(len(words) / 200))}, "steps": ["enrich"]}


def redact(state: DocState) -> dict:
    return {"text": EMAIL.sub("[REDACTED]", state["text"]), "steps": ["redact"]}


def summarize(state: DocState) -> dict:
    sentences = re.split(r"(?<=[.!?])\s+", state["text"].strip())
    return {"summary": " ".join(sentences[:2]), "status": "published", "steps": ["summarize"]}


def route_after_validate(state: DocState) -> str:
    return "detect_pii" if state["errors"] is not None else "quarantine"


def route_after_enrich(state: DocState) -> str:
    return "redact" if state["meta"].get("pii") else "summarize"


def build_graph():
    g = StateGraph(DocState)
    for name, fn in [("validate", validate), ("quarantine", quarantine), ("detect_pii", detect_pii),
                     ("enrich", enrich), ("redact", redact), ("summarize", summarize)]:
        g.add_node(name, fn)
    g.add_edge(START, "validate")
    g.add_conditional_edges("validate", route_after_validate, ["detect_pii", "quarantine"])
    g.add_edge("quarantine", END)
    g.add_edge("detect_pii", "enrich")
    g.add_conditional_edges("enrich", route_after_enrich, ["redact", "summarize"])
    g.add_edge("redact", "summarize")
    g.add_edge("summarize", END)
    return g.compile()


def main() -> None:
    app = build_graph()
    docs = json.loads(DATA.read_text(encoding="utf-8"))
    for doc in docs:
        final = app.invoke({"doc": doc, "errors": [], "meta": {}, "text": "", "summary": "", "status": "", "steps": []})
        print(f"[{doc['id']}] {doc['title'] or '(untitled)'}")
        print(f"     status : {final['status']}")
        print(f"     steps  : {' -> '.join(final['steps'])}")
        print(f"     meta   : {final['meta']}")
        if final["summary"]:
            print(f"     summary: {final['summary']}")
        print()


if __name__ == "__main__":
    main()
