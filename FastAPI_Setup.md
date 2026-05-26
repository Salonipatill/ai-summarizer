#  FastAPI

FastAPI is a modern, high-performance Python framework used for building APIs and backend services.

It provides:
- fast development
- async support
- automatic API documentation
- data validation
- scalable backend architecture

In this project, FastAPI is used as the core backend framework for:
- LLM integrations
- AI APIs
- semantic search
- embeddings workflows
- vector database operations
- RAG pipelines
- AI microservices

---


# FastAPI Project Setup (Windows)

## 1. Install Python

Install Python 3.11 on your system.

Check Python version:

```bash
python --version
```

Expected output:

```text
Python 3.11.x
```

This confirms Python is installed correctly.

---

## 2. Open Project in VS Code

Open the project folder in VS Code.

Open terminal:

```text
Terminal → New Terminal
```

The terminal is used to run Python and FastAPI commands.

---

## 3. Navigate to AI Service Folder

Move into the AI service directory:

```bash
cd backend/ai-service
```

This folder contains the FastAPI backend code.

---

## 4. Create Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

A virtual environment keeps project packages isolated from the system Python.

---

## 5. Activate Virtual Environment

Activate the environment:

```bash
venv\Scripts\activate
```

After activation you will see:

```text
(venv)
```

This means the virtual environment is active.

---

## 6. Install FastAPI and Uvicorn

Install FastAPI framework and Uvicorn server:

```bash
pip install fastapi uvicorn
```

Explanation:
- `fastapi` → API framework
- `uvicorn` → server used to run FastAPI applications

---

## 7. Install Project Dependencies

Install all required project packages:

```bash
pip install -r requirements.txt
```

This installs:
- AI libraries
- database packages
- utility packages
- additional backend dependencies

---

## 8. Create Environment File

Create a `.env` file in the project root folder.

Example:

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

The `.env` file stores:
- API keys
- configuration
- database URLs
- secret values

---

## 9. Run FastAPI Server

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

Explanation:
- `app.main` → main FastAPI file
- `app` → FastAPI application instance
- `--reload` → reloads server automatically after code changes

Server URL:

```text
http://127.0.0.1:8000
```

---

## 10. Open API Documentation

FastAPI automatically generates API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

Used for:
- testing APIs
- viewing endpoints
- sending requests

---

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Used for:
- reading API documentation
- viewing endpoint details