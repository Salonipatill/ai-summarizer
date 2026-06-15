# Codebase Architecture

## Overview

The AI service is built using a modular FastAPI architecture.

The codebase is designed for:
- scalability
- maintainability
- AI integrations
- RAG workflows
- semantic search
- microservice architecture

The project separates:
- API routes → define backend endpoints and handle requests
- business logic → contains the main application functionality
- AI workflows → manages multi-step AI processing pipelines
- vector search → performs semantic similarity search using embeddings
- middleware → processes requests before reaching API routes
- utilities → reusable helper functions used across the project

This keeps the code clean and easier to manage.


# Main Project Structure

```text
ai-service/
│
├── .env.example
├── .gitignore
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── README.md
│
├── data/
│   ├── qdrant/
│   ├── cache/
│   └── logs/
│
├── scripts/
│   ├── ingest_articles.py
│   ├── rebuild_embeddings.py
│   └── test_groq.py
│
├── tests/
│   ├── conftest.py
│   │
│   ├── test_routers/
│   │   ├── test_summarize.py
│   │   ├── test_search.py
│   │   └── test_keywords.py
│   │
│   ├── test_workflows/
│   │   ├── test_summary_flow.py
│   │   └── test_search_flow.py
│   │
│   └── test_services/
│       ├── test_groq.py
│       └── test_embeddings.py
│
└── app/
    │
    ├── main.py
    ├── config.py
    ├── dependencies.py
    │
    ├── core/
    │   ├── exceptions.py
    │   ├── constants.py
    │   ├── lifespan.py
    │   └── registry.py
    │
    ├── routers/
    │   ├── health.py
    │   │
    │   ├── summarize.py
    │   ├── semantic_search.py
    │   ├── ai_writer.py
    │   │
    │   ├── moderate.py
    │   ├── recommend.py
    │   ├── keywords.py
    │   ├── seo.py
    │   ├── related_articles.py
    │   └── tts.py
    │
    ├── schemas/
    │   ├── base.py
    │   │
    │   ├── summarize.py
    │   ├── search.py
    │   ├── writer.py
    │   ├── moderation.py
    │   ├── recommendation.py
    │   ├── keywords.py
    │   ├── seo.py
    │   └── tts.py
    │
    ├── middleware/
    │   ├── auth.py
    │   ├── logging.py
    │   ├── metrics.py
    │   └── rate_limit.py
    │
    ├── services/
    │   │
    │   ├── llm/
    │   │   ├── base.py
    │   │   ├── factory.py
    │   │   ├── groq.py
    │   │   ├── openai.py
    │   │   │
    │   │   └── prompts/
    │   │       ├── summarize.txt
    │   │       ├── ai_writer.txt
    │   │       ├── moderation.txt
    │   │       ├── seo.txt
    │   │       └── keywords.txt
    │   │
    │   ├── embeddings/
    │   │   ├── base.py
    │   │   ├── openai_embeddings.py
    │   │   ├── local_embeddings.py
    │   │   └── factory.py
    │   │
    │   ├── rag/
    │   │   ├── chunking.py
    │   │   ├── retriever.py
    │   │   ├── reranker.py
    │   │   ├── indexing.py
    │   │   │
    │   │   └── vectorstore/
    │   │       ├── base.py
    │   │       ├── qdrant.py
    │   │       └── chroma.py
    │   │
    │   ├── workflows/
    │   │   ├── base_flow.py
    │   │   │
    │   │   ├── summarize_flow.py
    │   │   ├── semantic_search_flow.py
    │   │   ├── ai_writer_flow.py
    │   │   ├── moderation_flow.py
    │   │   ├── recommendation_flow.py
    │   │   ├── seo_flow.py
    │   │   └── related_articles_flow.py
    │   │
    │   ├── apps/
    │   │   ├── summarize_service.py
    │   │   ├── search_service.py
    │   │   ├── writer_service.py
    │   │   ├── moderation_service.py
    │   │   └── recommendation_service.py
    │   │
    │   ├── cache/
    │   │   ├── base.py
    │   │   ├── redis_cache.py
    │   │   └── memory_cache.py
    │   │
    │   └── tools/
    │       ├── tokenizer.py
    │       ├── validators.py
    │       ├── text_cleaner.py
    │       ├── chunker.py
    │       ├── retry.py
    │       └── prompt_loader.py
    │
    ├── observability/
    │   ├── logging.py
    │   ├── tracing.py
    │   ├── metrics.py
    │   └── cost_tracking.py
    │
    └── utils/
        ├── text.py
        ├── time.py
        └── helpers.py

```


```text

Long-Term Architecture

Node.js Monolith
       │
       ▼
FastAPI AI Gateway
       │
       ▼
LangGraph Workflows
       │
 ┌─────┼─────────┐
 ▼     ▼         ▼
RAG   LLM      Tools
 │
 ▼
Qdrant

```

