from __future__ import annotations

import json
from pathlib import Path

from academic_orchestrator.agents.citation_agent import CitationAgent
from academic_orchestrator.agents.planner import PlannerAgent
from academic_orchestrator.agents.retriever import RetrieverAgent
from academic_orchestrator.agents.reviewer import ReviewerAgent
from academic_orchestrator.agents.summarizer import SummarizerAgent
from academic_orchestrator.agents.writer import WriterAgent
from academic_orchestrator.hooks import RunHooks
from academic_orchestrator.providers.base import BaseProvider
from academic_orchestrator.tools.document_tools import load_papers


class ResearchOrchestrator:
    """Coordinates all subagents for the academic research assistant use case."""

    def __init__(self, provider: BaseProvider, data_path: str | Path, output_dir: str | Path = "outputs"):
        self.provider = provider
        self.data_path = Path(data_path)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.hooks = RunHooks()

        self.planner = PlannerAgent("PlannerAgent", "Breaks academic tasks into subtasks.", provider, self.hooks)
        self.retriever = RetrieverAgent("RetrieverAgent", "Finds relevant documents.", provider, self.hooks)
        self.summarizer = SummarizerAgent("SummarizerAgent", "Summarizes retrieved documents.", provider, self.hooks)
        self.citation = CitationAgent("CitationAgent", "Formats citations.", provider, self.hooks)
        self.writer = WriterAgent("WriterAgent", "Writes the final academic response.", provider, self.hooks)
        self.reviewer = ReviewerAgent("ReviewerAgent", "Checks final output quality.", provider, self.hooks)

    def run(self, user_request: str) -> dict:
        papers = load_papers(self.data_path)

        plan = self.planner.run(user_request)
        documents = self.retriever.run(user_request, papers)
        summaries = self.summarizer.run(documents)
        citations = self.citation.run(documents)
        report = self.writer.run(user_request, summaries, citations)
        review = self.reviewer.run(report)

        final_report_path = self.output_dir / "final_report.md"
        trace_path = self.output_dir / "run_trace.json"

        final_report_path.write_text(report, encoding="utf-8")
        trace_path.write_text(json.dumps(self.hooks.to_dict(), indent=2), encoding="utf-8")

        return {
            "plan": plan,
            "documents_found": len(documents),
            "review": review,
            "final_report_path": str(final_report_path),
            "trace_path": str(trace_path),
        }
