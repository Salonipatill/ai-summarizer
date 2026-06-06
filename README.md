# AI Summarizer

## Overview

`AI Summarizer` is a FastAPI-based AI backend service focused on building modular AI workflows for article summarization, semantic search, and related AI features. This repository contains architecture guidance, setup instructions, and development steps for a scalable AI microservice.

The project is designed to support:
- FastAPI backend services
- LLM / AI model integrations
- semantic search and embeddings
- RAG workflows
- health, readiness, auth, logging, and metrics middleware
- Docker deployment

## Project Goals

The main goal of this phase is to build a working FastAPI AI service that includes:
- a basic article summarization endpoint (`POST /summarize`)
- health and readiness endpoints
- auth middleware
- request logging middleware
- a metrics skeleton
- config and environment handling
- Docker containerization
- tests and CI readiness

## Core Concepts

This codebase follows a modular architecture:
- `app/main.py` — application entrypoint
- `app/routers/` — API routes and endpoint modules
- `app/schemas/` — request and response validation models
- `app/services/` — business logic, AI integrations, and helper services
- `app/middleware/` — middleware for auth, logging, metrics, and request handling
- `app/config.py` — centralized environment configuration
- `tests/` — automated test coverage for routers and services

## Recommended Structure

```text
ai-service/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── middleware/
│   ├── observability/
│   └── utils/
│
├── requirements.txt
├── requirements-dev.txt
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── README.md
└── tests/
```

## Getting Started

### 1. Install Python

Install Python 3.11 and verify:

```bash
python --version
```

Expected output:

```text
Python 3.11.x
```

### 2. Open the Project in VS Code

Open the repository root in VS Code and use the integrated terminal.

### 3. Navigate to the AI Service Folder

If the API service is contained in `ai-service/`, change directories:

```bash
cd ai-service
```

### 4. Create a Virtual Environment

```bash
python -m venv venv
```

### 5. Activate the Virtual Environment

```bash
venv\Scripts\activate
```

### 6. Install Dependencies

Install required packages and project dependencies:

```bash
pip install fastapi uvicorn python-dotenv
pip install -r requirements.txt
```

If using OpenAI or Groq, install the corresponding SDK:

```bash
pip install openai
pip install groq
```

### 7. Create Environment File

Create a `.env` file in the project root with values such as:

```env
APP_NAME=ai-service
APP_ENV=development
HOST=0.0.0.0
PORT=8000
OPENAI_API_KEY=
GROQ_API_KEY=
QDRANT_URL=
REDIS_URL=
INTERNAL_API_KEY=
```

### 8. Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

Access the service at:

```text
http://127.0.0.1:8000
```

### 9. Open API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Feature: Article Summarization

The initial AI feature is a simple article summarization endpoint.

### Endpoint

```http
POST /summarize
```

### Request

```json
{
  "text": "Long article text..."
}
```

### Response

```json
{
  "summary": "Short AI generated summary..."
}
```

### Implementation Flow

1. Request reaches `app/routers/summarize.py`
2. Request body is validated by `app/schemas/summarize.py`
3. Summarization logic runs in `app/services/summarize_service.py`
4. AI model or placeholder response is returned
5. Response is delivered as JSON

## AI Model Integration

The repository supports integrating external AI providers such as Groq or OpenAI.

### Example Groq Integration

- Add `GROQ_API_KEY` to `.env`
- Install `groq`
- Load environment variables with `python-dotenv`
- Use `Groq(api_key=os.getenv("GROQ_API_KEY"))` in the summarization service

### Prompt Engineering

A strong prompt helps control summary quality:
- specify professional tone
- limit length
- ask for simple English
- focus on key points

## Production Readiness

The project should include:
- input validation in schemas
- error handling in routers and services
- consistent API response format
- logging and request tracking
- auth middleware for protected routes
- health and readiness endpoints

## Health and Readiness Endpoints

Create reliable endpoints for service monitoring.

### Example endpoints

```http
GET /v1/healthz
GET /v1/readyz
```

These endpoints should return service status, uptime, and readiness information.

## Docker

A Dockerfile should be created for containerized deployment.

### Example Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Build and run

```bash
docker build -t ai-service .
docker run -p 8000:8000 ai-service
```

## Notes

- Keep secrets out of source control by adding `.env` paths to `.gitignore`
- Use `git check-ignore -v <path>` to verify ignored files
- Keep API response shape consistent across future endpoints (`/summarize`, `/chat`, `/translate`, etc.)

## Next Steps

After the first summarization feature is working:
- add better prompt engineering
- add structured metadata to API responses
- add logging and metrics
- add auth middleware
- write tests for routes and service flows
- add GitHub Actions for CI
- expand service to support more AI workflows
