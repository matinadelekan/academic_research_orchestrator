from __future__ import annotations

from pathlib import Path

from academic_orchestrator.orchestrator import ResearchOrchestrator
from academic_orchestrator.providers.mock_provider import MockProvider


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    data_path = project_root / "data" / "sample_papers.json"
    output_dir = project_root / "outputs"

    user_request = (
        "Create a short research summary about agent orchestration, including "
        "provider-agnostic design, tool calling, hooks, cost tracking, and subagents."
    )

    orchestrator = ResearchOrchestrator(
        provider=MockProvider(),
        data_path=data_path,
        output_dir=output_dir,
    )

    result = orchestrator.run(user_request)

    print("[PlannerAgent] Created subtasks")
    print(f"[RetrieverAgent] Found {result['documents_found']} relevant notes")
    print("[SummarizerAgent] Built summary from retrieved context")
    print("[CitationAgent] Created citations")
    print("[WriterAgent] Drafted final response")
    print(f"[ReviewerAgent] {result['review']}")
    print()
    print(f"Final report written to {result['final_report_path']}")
    print(f"Run trace written to {result['trace_path']}")


if __name__ == "__main__":
    main()
