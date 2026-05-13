from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class RunHooks:
    """Simple hook system for logging agent activity and estimated cost."""

    events: list[dict[str, Any]] = field(default_factory=list)
    total_estimated_tokens: int = 0
    total_estimated_cost: float = 0.0

    def log(self, event_type: str, agent: str, details: dict[str, Any] | None = None) -> None:
        details = details or {}
        self.events.append(
            {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "event_type": event_type,
                "agent": agent,
                "details": details,
            }
        )

    def track_usage(self, agent: str, prompt: str, response: str) -> None:
        # Simple estimate: about 4 characters per token.
        estimated_tokens = max(1, (len(prompt) + len(response)) // 4)
        estimated_cost = estimated_tokens * 0.000001  # placeholder cost estimate

        self.total_estimated_tokens += estimated_tokens
        self.total_estimated_cost += estimated_cost

        self.log(
            "usage",
            agent,
            {
                "estimated_tokens": estimated_tokens,
                "estimated_cost_usd": round(estimated_cost, 6),
            },
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "total_estimated_tokens": self.total_estimated_tokens,
            "total_estimated_cost_usd": round(self.total_estimated_cost, 6),
            "events": self.events,
        }
