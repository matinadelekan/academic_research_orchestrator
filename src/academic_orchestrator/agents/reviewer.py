from __future__ import annotations

from .base_agent import BaseAgent


class ReviewerAgent(BaseAgent):
    def run(self, report: str) -> str:
        checks = {
            "has_problem": "## Problem" in report,
            "has_application": "## Application Scenario" in report,
            "has_learning": "## Personal Learning" in report,
            "has_references": "## References" in report,
        }

        missing = [name for name, passed in checks.items() if not passed]
        if missing:
            return f"Needs revision. Missing: {', '.join(missing)}"

        return self.ask_model("Review the report for completeness and assignment alignment.")
