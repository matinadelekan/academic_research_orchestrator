from __future__ import annotations

from academic_orchestrator.tools.document_tools import summarize_text

from .base_agent import BaseAgent


class SummarizerAgent(BaseAgent):
    def run(self, documents: list[dict]) -> str:
        summaries = []
        for doc in documents:
            self.hooks.log("tool_call", self.name, {"tool": "summarize_text", "document": doc["id"]})
            summaries.append(f"- {doc['title']}: {summarize_text(doc['text'], max_sentences=2)}")
        return "\n".join(summaries)
