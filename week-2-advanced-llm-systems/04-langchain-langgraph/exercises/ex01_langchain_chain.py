"""Week 2 / 04 LangChain / Exercise 1: an LCEL chain with a custom retriever and a stub model.

Needs: langchain-core (runs offline; no model provider package or API key).
Run:  python ex01_langchain_chain.py
"""
from __future__ import annotations

import sys
from pathlib import Path

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from llm_stubs import HashEmbedder, StubLLM  # noqa: E402

DOCS = [
    Document(page_content="Orders can be cancelled free of charge until a courier is assigned.", metadata={"source": "cancellations"}),
    Document(page_content="If your delivery is more than 30 minutes late you receive an automatic credit of 10% of the basket value.", metadata={"source": "late"}),
    Document(page_content="Refunds for missing items are issued to the original payment method within 3 business days.", metadata={"source": "refunds"}),
    Document(page_content="The delivery fee is 2.50 for baskets under 40.00 and free for baskets of 40.00 or more.", metadata={"source": "fees"}),
]

embedder = HashEmbedder()
doc_vectors = embedder.embed_many([d.page_content for d in DOCS])


def retrieve(question: str, k: int = 2) -> list[Document]:
    scores = doc_vectors @ embedder.embed(question)
    return [DOCS[i] for i in scores.argsort()[::-1][:k]]


def format_docs(docs: list[Document]) -> str:
    return "\n".join(f"[{d.metadata['source']}] {d.page_content}" for d in docs)


stub = StubLLM()
llm = RunnableLambda(lambda prompt_value: stub.complete(prompt_value.to_string(), temperature=0.0))

prompt = PromptTemplate.from_template(
    "Answer only from the context; say you don't know otherwise.\nContext: {context}\nQuestion: {question}\n"
)

# LCEL: compose runnables with |. Inputs flow left to right.
rag_chain = (
    RunnableParallel(context=RunnableLambda(retrieve) | RunnableLambda(format_docs), question=RunnablePassthrough())
    | prompt
    | llm
    | StrOutputParser()
)


def main() -> None:
    print("prompt input variables:", prompt.input_variables)
    for q in [
        "How long until refunds for missing items arrive?",
        "When is the delivery fee free for baskets?",
        "Do you sell gift cards?",
    ]:
        print(f"Q: {q}\n  sources: {[d.metadata['source'] for d in retrieve(q)]}\n  A: {rag_chain.invoke(q)}")
    print("\nbatch:", rag_chain.batch(["Can I cancel before a courier is assigned?"]))
    print(
        "\nYour turn:\n"
        "  1. Wrap `retrieve` as a proper LangChain retriever (subclass BaseRetriever) and use it.\n"
        "  2. Add a step that returns {'answer': ..., 'sources': [...]} instead of a string.\n"
        "  3. What happens if the template uses {query} but the chain passes 'question'? Try it."
    )


if __name__ == "__main__":
    main()
