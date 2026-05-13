# Academic Research Orchestrator

A small multi-agent AI system inspired by **Orchestral AI: A Framework for Agent Orchestration**.  
The project demonstrates an academic research assistant that breaks a student research task into smaller agents:

- **Planner Agent** — breaks the user request into subtasks
- **Retriever Agent** — searches local paper notes / text files
- **Summarizer Agent** — extracts useful points from retrieved context
- **Citation Agent** — formats simple citations from source metadata
- **Writer Agent** — creates a structured draft response
- **Reviewer Agent** — checks whether the final answer meets requirements

This is designed as a class-friendly codebase: it runs without an API key using a mock provider, but the structure is provider-agnostic so an OpenAI or other LLM provider can be added later.

---

## Why this relates to the Orchestral AI paper

The paper emphasizes several ideas that this project applies:

1. **Agent architecture**  
   Each agent has a role, receives context, and calls tools through the orchestrator.

2. **Provider-agnostic design**  
   The code separates the LLM provider from the agent logic. The default `MockProvider` makes the project reproducible without paid API access.

3. **Tool calling and hooks**  
   Agents use tools such as `search_documents`, `summarize_text`, and `format_citation`. Hooks log agent starts, finishes, tool calls, and estimated costs.

4. **Cost tracking and reproducibility**  
   Each run creates a JSON trace in `outputs/run_trace.json`, showing which agents ran, what tools were used, and estimated token/cost information.

5. **Subagents**  
   The orchestrator delegates work to specialized agents instead of using one large agent for the whole task.

---

## Project structure

```text
academic_research_orchestrator/
├── data/
│   └── sample_papers.json
├── outputs/
│   └── final_report.md
├── screenshots/
│   ├── terminal_run.txt
│   └── sample_output_preview.txt
├── src/
│   └── academic_orchestrator/
│       ├── agents/
│       ├── providers/
│       ├── tools/
│       ├── hooks.py
│       ├── orchestrator.py
│       └── run_demo.py
├── tests/
│   └── test_tools.py
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone https://github.com/YOUR-USERNAME/academic-research-orchestrator.git
cd academic-research-orchestrator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Run the demo

```bash
python -m src.academic_orchestrator.run_demo
```

The demo asks the multi-agent system to create a short research summary about agent orchestration.

---

## Example output

```text
[PlannerAgent] Created 4 subtasks
[RetrieverAgent] Found 3 relevant notes
[SummarizerAgent] Built summary from retrieved context
[CitationAgent] Created citations
[WriterAgent] Drafted final response
[ReviewerAgent] Checked final response against requirements

Final report written to outputs/final_report.md
Run trace written to outputs/run_trace.json
```

---

## Screenshots / run evidence

Because this project is command-line based, the `screenshots/` folder includes text-based run evidence:

- `screenshots/terminal_run.txt`
- `screenshots/sample_output_preview.txt`

You can replace these with actual screenshots from your terminal before submitting.

---

## Notes for submission

Before submitting, update this README with:

1. Your GitHub repository link
2. Your own terminal screenshot
3. Any extra feature you added
4. Your reflection report

---

## Possible extensions

- Add a real OpenAI, Anthropic, or Gemini provider
- Let users upload PDFs
- Add vector search instead of keyword search
- Add a web UI with Streamlit or FastAPI
- Save run history in SQLite
