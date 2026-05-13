from academic_orchestrator.tools.document_tools import format_citation, search_documents, summarize_text


def test_search_documents_finds_relevant_document():
    papers = [
        {"id": "1", "title": "Agent Tools", "authors": "A", "year": 2024, "text": "tool calling and agents"},
        {"id": "2", "title": "Other", "authors": "B", "year": 2024, "text": "unrelated topic"},
    ]

    results = search_documents("tool calling agents", papers)
    assert results[0]["id"] == "1"


def test_summarize_text_limits_sentences():
    text = "Sentence one. Sentence two. Sentence three."
    summary = summarize_text(text, max_sentences=2)
    assert summary == "Sentence one. Sentence two."


def test_format_citation():
    paper = {"title": "Test Paper", "authors": "Doe", "year": 2025}
    assert format_citation(paper) == "Doe (2025). Test Paper."
