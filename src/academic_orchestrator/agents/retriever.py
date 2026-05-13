from __future__ import annotations

from academic_orchestrator.tools.document_tools import search_documents

from .base_agent import BaseAgent


class RetrieverAgent(BaseAgent):
    def run(self, query: str, papers: list[dict]) -> list[dict]:
        self.hooks.log("tool_call", self.name, {"tool": "search_documents", "query": query})
        results = search_documents(query, papers, top_k=3)
        self.hooks.log("tool_result", self.name, {"documents_found": len(results)})
        return results
