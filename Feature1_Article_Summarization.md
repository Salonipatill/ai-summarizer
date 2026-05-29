# First Starting Step of AI Service Codebase


# First AI Feature

Start with:

```text
Article Summarization
```
it is the simplest REAL AI feature and teaches the complete backend flow.

---

# Goal

Build this API:

```http
POST /summarize
```

Input:

```json
{
  "text": "Long article text..."
}
```

Output:

```json
{
  "summary": "Short AI generated summary..."
}
```

---

# Step 1 — Create AI Service Structure first

```text
ai-service/
│
├── app/
│   ├── main.py
│   │
│   ├── routers/
│   │   └── summarize.py
│   │
│   ├── schemas/
│   │   └── summarize.py
│   │
│   └── services/
│       └── summarize_service.py
│
├── requirements.txt
├── .env
└── README.md
```

---

# Step 2 — Install Required Packages

Activate virtual environment.

Then install:

if using openai api

```bash
pip install fastapi uvicorn openai python-dotenv
```
if using groq api key

```bash
pip install fastapi uvicorn groq python-dotenv
```


Explanation:
- `fastapi` → backend framework
- `uvicorn` → FastAPI server
- `openai` → OpenAI SDK
- `python-dotenv` → loads environment variables

---

# Step 3 — Create Main FastAPI App

File:

```text
app/main.py
```

Code:

```python
from fastapi import FastAPI
from app.routers.summarize import router as summarize_router

app = FastAPI()

app.include_router(summarize_router)
```

Purpose:
- creates FastAPI app
- connects summarize API router

---

# Step 4 — Create Request Schema

File:

```text
app/schemas/summarize.py
```

Code:

```python
from pydantic import BaseModel

class SummaryRequest(BaseModel):
    text: str
```

Purpose:
- validates incoming request body

---

# Step 5 — Create Summarize Service

File:

```text
app/services/summarize_service.py
```

Code:

```python
def summarize_text(text: str):
    return "This is AI summary"
```

Purpose:
- contains AI business logic
- currently returns fake summary

Do NOT integrate OpenAI yet.

First understand the backend flow.

---

# Step 6 — Create Summarize Router

File:

```text
app/routers/summarize.py
```

Code:

```python
from fastapi import APIRouter
from app.schemas.summarize import SummaryRequest
from app.services.summarize_service import summarize_text

router = APIRouter()

@router.post("/summarize")
def summarize(data: SummaryRequest):

    summary = summarize_text(data.text)

    return {
        "summary": summary
    }
```

Purpose:
- receives request
- validates data
- calls service
- returns JSON response

---

# Step 7 — Run FastAPI Server

Run server:

```bash
uvicorn app.main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

---

# Step 8 — Open Swagger Docs

Open:

```text
http://127.0.0.1:8000/docs
```

This lets you test your AI API directly.

---

# Step 9 — Test API

Test endpoint:

```http
POST /summarize
```

Request:

```json
{
  "text": "Artificial intelligence is transforming education."
}
```

Response:

```json
{
  "summary": "This is AI summary"
}
```

---

# What We Learn From This

This ONE feature teaches:

```text
API Request
      ↓
Router
      ↓
Schema Validation
      ↓
Service Logic
      ↓
Response
```

This is the foundation of your entire AI backend architecture.

---
 
# Next Step — Integrate Groq API for Real AI Summarization

Previously, the summarization service returned a fake response:

```python
return "This is AI summary"
```

Now we will integrate the real Groq AI model.

This makes the summarization feature an actual AI-powered API.

---

# Updated AI Flow

```text
Request
   ↓
Router
   ↓
Schema Validation
   ↓
Summarize Service
   ↓
Groq API
   ↓
AI Generated Summary
   ↓
JSON Response
```

---

# Step 1 — Add Groq API Key

Open:

```text
.env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key
```

Purpose:
- securely stores Groq API key
- avoids hardcoding secrets in source code

---

# Step 2 — Install Groq SDK

Install required package:

```bash
pip install groq python-dotenv
```

Explanation:
- `groq` → Groq AI SDK
- `python-dotenv` → loads environment variables from `.env`

---

# Step 3 — Update Summarize Service

File:

```text
app/services/summarize_service.py
```

Replace old code with:

```python
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def summarize_text(text: str):

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "Summarize the article in short."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content
```

---

# Code Explanation

## `load_dotenv()`

Loads variables from:

```text
.env
```

---

## `os.getenv("GROQ_API_KEY")`

Reads the API key securely.

---

## `Groq()`

Creates Groq AI client.

---

## `model="llama3-8b-8192"`

Specifies the AI model used for summarization.

---

## `messages`

Prompt sent to the AI model.

### System Message

```text
Summarize the article in short.
```

This controls AI behavior.

### User Message

Contains the actual article text.

---

# Step 4 — Run FastAPI Server

Start the server:

```bash
uvicorn app.main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

---

# Step 5 — Open Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows testing APIs directly from the browser.

---

# Step 6 — Test Real AI Summarization

Endpoint:

```http
POST /summarize
```

Request:

```json
{
  "text": "Artificial intelligence is transforming modern education through automation and personalized learning."
}
```

Example Response:

```json
{
  "summary": "AI is improving education using automation and personalized learning systems."
}
```

Now the response is generated by a real AI model.

---

# What We Learn From This Step

This step teaches:

- LLM integration
- API key management
- environment variables
- AI prompting
- external AI API calls
- real AI response generation

---

#  Backend Flow Is Now

```text
Frontend / Backend Request
           ↓
FastAPI Router
           ↓
Schema Validation
           ↓
Summarize Service
           ↓
Groq AI Model
           ↓
Generated Summary
           ↓
JSON Response
```

This is  first real AI microservice feature.

---

# Next Step - Better Prompt Engineering


After integrating Groq AI successfully, the next step is:

```text
Better Prompt Engineering
```

This phase improves the quality of AI-generated summaries.

---

# Prompt Engineering

A prompt is the instruction sent to the AI model.

Example:

```python
"Summarize the article in short."
```

Prompt engineering means:

```text
Writing better instructions for AI
```

Better prompts produce:
- better summaries
- cleaner responses
- more accurate outputs
- professional tone
- controlled AI behavior

---

# Current Basic Prompt

Current code:

```python
messages=[
    {
        "role": "system",
        "content": "Summarize the article in short."
    },
    {
        "role": "user",
        "content": text
    }
]
```

This works, but the AI output may:
- be too long
- sound inconsistent
- miss important points
- change writing style randomly

---

# Goal of This Phase

Improve summary quality using better prompts.

---

# Better Prompt Example

Replace old prompt with:

```python
messages=[
    {
        "role": "system",
        "content": """
        You are a professional news summarizer.

        Summarize the article clearly and professionally.

        Rules:
        - Keep summary under 100 words
        - Use simple English
        - Focus on key points
        - Avoid unnecessary details
        """
    },
    {
        "role": "user",
        "content": text
    }
]
```

---

# What Improved Here

## Role Definition

```text
You are a professional news summarizer.
```

This gives AI a specific behavior.

---

## Clear Instructions

```text
Keep summary under 100 words
```

Controls output length.

---

## Writing Style Control

```text
Use simple English
```

Makes summaries easier to read.

---

## Focus Guidance

```text
Focus on key points
```

Improves relevance.

---

# Updated `summarize_service.py`

File:

```text
app/services/summarize_service.py
```

Code:

```python
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def summarize_text(text: str):

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": """
                You are a professional news summarizer.

                Summarize the article clearly and professionally.

                Rules:
                - Keep summary under 100 words
                - Use simple English
                - Focus on important points
                """
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content
```

---

# What We Learn In This Phase

This phase teaches:

- prompt engineering
- AI instruction design
- AI output control
- professional AI responses
- LLM behavior management

---

# Importance of Prompt Engineering 

AI quality depends heavily on prompts.

Bad prompt:

```text
Summarize this.
```

Good prompt:

```text
Summarize professionally in under 100 words using simple language.
```

Small prompt improvements can dramatically improve AI output.

---

# Real AI Backend Architecture

```text
Request
   ↓
Router
   ↓
Schema
   ↓
Service
   ↓
Prompt Engineering
   ↓
Groq API
   ↓
AI Response
```

Prompt engineering is a core part of  backend logic.

---

