from __future__ import annotations

from dataclasses import dataclass

from academic_orchestrator.hooks import RunHooks
from academic_orchestrator.providers.base import BaseProvider


@dataclass
class BaseAgent:
    name: str
    role: str
    provider: BaseProvider
    hooks: RunHooks

    def ask_model(self, prompt: str) -> str:
        self.hooks.log("agent_start", self.name, {"role": self.role})
        response = self.provider.generate(self.role, prompt)
        self.hooks.track_usage(self.name, prompt, response)
        self.hooks.log("agent_finish", self.name, {"response_preview": response[:120]})
        return response
