from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_papers(path: str | Path) -> list[dict[str, Any]]:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Could not find paper data at {file_path}")

    return json.loads(file_path.read_text(encoding="utf-8"))


def search_documents(query: str, papers: list[dict[str, Any]], top_k: int = 3) -> list[dict[str, Any]]:
    """Simple keyword search over local paper notes.

    A real version could replace this with vector search.
    """
    query_terms = {term.lower() for term in query.split() if len(term) > 2}
    scored: list[tuple[int, dict[str, Any]]] = []

    for paper in papers:
        haystack = f"{paper['title']} {paper['text']}".lower()
        score = sum(1 for term in query_terms if term in haystack)
        if score > 0:
            scored.append((score, paper))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [paper for _, paper in scored[:top_k]]


def summarize_text(text: str, max_sentences: int = 3) -> str:
    sentences = [sentence.strip() for sentence in text.replace("\n", " ").split(".") if sentence.strip()]
    return ". ".join(sentences[:max_sentences]) + "." if sentences else ""


def format_citation(paper: dict[str, Any]) -> str:
    return f"{paper['authors']} ({paper['year']}). {paper['title']}."
