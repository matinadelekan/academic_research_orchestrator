from __future__ import annotations

from academic_orchestrator.tools.document_tools import format_citation

from .base_agent import BaseAgent


class CitationAgent(BaseAgent):
    def run(self, documents: list[dict]) -> list[str]:
        citations = []
        for doc in documents:
            self.hooks.log("tool_call", self.name, {"tool": "format_citation", "document": doc["id"]})
            citations.append(format_citation(doc))
        return citations
