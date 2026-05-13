from __future__ import annotations

from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """Provider interface used by all agents.

    This makes the project provider-agnostic. Agents do not need to know whether
    the response comes from OpenAI, Anthropic, Gemini, or a local mock provider.
    """

    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        raise NotImplementedError
