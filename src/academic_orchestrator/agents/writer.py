from __future__ import annotations

from .base_agent import BaseAgent


class WriterAgent(BaseAgent):
    def run(self, user_request: str, summaries: str, citations: list[str]) -> str:
        citation_text = "\n".join(f"- {citation}" for citation in citations)

        return f"""# Multi-Agent Academic Research Assistant

## Problem

The goal of this system is to help a student complete a research task by splitting the work across specialized AI agents instead of relying on one general chatbot. This makes the process easier to understand, debug, and improve.

## Important Ideas Applied

First, the system uses a clear agent architecture. The planner, retriever, summarizer, citation, writer, and reviewer agents each have a specific responsibility. This reflects the idea that complex LLM systems should be organized around roles, tools, and context.

Second, the project uses provider-agnostic design. The agents do not depend directly on one LLM company or API format. The default mock provider makes the project reproducible, and a real provider can be added later without rewriting the entire system.

Third, the project uses tool calling and hooks. Agents call tools for document search, summarization, and citation formatting. Hooks record when agents start, when tools are called, and how much estimated cost was used. This supports transparency and debugging.

## Application Scenario

A real-world use case is an academic research assistant for students. A student could upload papers, ask for a short literature summary, and receive a structured response with citations. The system would include a retrieval agent to find relevant source material, a summarizer agent to condense ideas, a citation agent to format references, and a reviewer agent to check whether the answer meets assignment requirements.

## Retrieved Evidence

{summaries}

## Personal Learning

This project helped me understand that AI agents are more than normal chatbots. The most important part is not just connecting an LLM to tools, but designing a workflow where each agent has a purpose. I also learned that reproducibility matters because agent systems can become difficult to test if every run behaves differently. The mock provider, hooks, and run trace make the system easier to explain and verify.

## References

{citation_text}
"""
