from __future__ import annotations

from .base_agent import BaseAgent


class PlannerAgent(BaseAgent):
    def run(self, user_request: str) -> list[str]:
        prompt = f"Create a plan for this academic research task: {user_request}"
        plan = self.ask_model(prompt)
        return [line.strip() for line in plan.splitlines() if line.strip()]
