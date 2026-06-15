# 11. Final Deliverables

## By end of Subphase 1:
```text
✅ FastAPI service running

✅ Docker working

✅ Health endpoint working

✅ Ready endpoint working

✅ Auth middleware working

✅ Logging middleware working

✅ Metrics skeleton working

✅ Model loader skeleton working

✅ Tests passing

✅ GitHub Actions passing

✅ README completed

✅ .env.example completed

✅ Models stored using volume mount
```


```text
We create health.py to provide health and readiness endpoints that allow Docker, backend services, and monitoring systems to verify that the AI service is running correctly and ready to accept requests.
```

# Step-by-Step: Create Health and Readiness Endpoints

# Step 1: Create the Router Folder

```text
app/
├── routers/
```

# Step 2: Create __init__.py
Inside routers create:

```text
app/routers/__init__.py
```

Keep it empty.

Purpose:
Makes routers a Python package.

# Step 3: Create health.py

Create:

```text
app/routers/health.py


Purpose:
Store all health-related APIs.
```

# Step 4: Import Required Libraries
Inside health.py:

```text
from fastapi import APIRouter
import time
import platform
```

APIRouter → creates routes.
time → calculates uptime.
platform → gets Python version.


# Step 5: Create Router Object

```text
router = APIRouter()
```
Purpose:
Holds all endpoints in this file.

# Step 6: Store Application Start Time

```text
START_TIME = time.time()
```

Purpose:

Used to calculate uptime.
Current Time - START_TIME = uptime

# Create Health Endpoint

# Step 7: Add /healthz

```text
@router.get("/healthz")
def healthz():
    return {
        "status": "ok",
        "uptime_sec": int(time.time() - START_TIME),
        "version": "0.1.0",
        "python": platform.python_version()
    }
```

# What it does

When someone calls:

```text
GET /v1/healthz
```

it returns:

```text
{
  "status": "ok",
  "uptime_sec": 120,
  "version": "0.1.0",
  "python": "3.11.9"
}
```
Purpose:
Confirms the service is alive.

# Create Readiness Endpoint

# Step 8: Add /readyz

```text
@router.get("/readyz")
def readyz():
    return {
        "ready": True,
        "models": {
            "summarize": "not_loaded"
        }
    }

```

# What it does

When someone calls:

```text
GET /v1/readyz
```

it returns:

```text
{
  "ready": true,
  "models": {
    "summarize": "not_loaded"
  }
}
```

Purpose:
Confirms the service is ready to accept requests.

# Step 9: Register the Router

Open:

app/main.py

Add:

```text
from fastapi import FastAPI
from app.routers.health import router as health_router

app = FastAPI()

app.include_router(
    health_router,
    prefix="/v1",
    tags=["Health"]
)
```

Purpose:

Connects health.py to the FastAPI app.

Without this step, the endpoints won't work.

# Step 10: Run the Server

```text
uvicorn app.main:app --reload
```
Expected:

```text
Uvicorn running on http://127.0.0.1:8000
```
# Step 11: Test Health Endpoint

Open:

```text
http://localhost:8000/v1/healthz
```

Expected:

```text
{
  "status": "ok",
  "uptime_sec": 50,
  "version": "0.1.0",
  "python": "3.11.x"
}
```

# Step 12: Test Readiness Endpoint

Open:

```text
http://localhost:8000/v1/readyz
```
Expected:

```
{
  "ready": true,
  "models": {
    "summarize": "not_loaded"
  }
}
```
# Health Endpoint (/healthz)

Checks whether the service is alive and running.


# Readiness Endpoint (/readyz)

Checks whether the service has completed initialization and is ready to handle requests.


## Configuration Management (config.py)

Objective

The config.py file is used to centralize application configuration by loading and validating environment variables. It ensures that all required settings are available before the FastAPI application starts.

Purpose
Read environment variables from the .env file.
Validate configuration values at application startup.
Provide a single source of configuration throughout the project.
Improve security by keeping sensitive values outside the source code.


# Environment Variables Used

AI_INTERNAL_KEY – Internal authentication key.
PORT – Application port number.
LOG_LEVEL – Logging level for the application.
MODELS_CACHE_DIR – Directory used for storing model cache files.
ENABLE_METRICS – Enables or disables metrics collection.


# Open app/config.py.

write :

```text
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    AI_INTERNAL_KEY: str
    PORT: int
    LOG_LEVEL: str
    MODELS_CACHE_DIR: str
    ENABLE_METRICS: bool

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
```

Open main.py and add:


```text
from app.config import settings

print(settings.PORT)
```

Run the application:

```text
uvicorn app.main:app --reload
```
inside this
```text
C:\The Infimit\infimit\ai-service
```
Create file:-
test_env.py

And Paste here:-

```text
from dotenv import dotenv_values

required = [
    "AI_INTERNAL_KEY",
    "PORT",
    "LOG_LEVEL",
    "MODELS_CACHE_DIR",
    "ENABLE_METRICS"
]

env = dotenv_values(".env")

for var in required:
    print(f"{var}: {'FOUND' if var in env else 'MISSING'}")

```


```text
python test_env.py
```

```text
from app.config import Settings

try:
    settings = Settings()
    print("SUCCESS")
    print(settings.model_dump())
except Exception as e:
    print(e)
```

```text
python test_settings.py
```
Option 2: Run directly from PowerShell (no file needed)

```text
python -c "from dotenv import dotenv_values; print(dotenv_values('.env'))"
```

is used to check whether Python can read your .env file correctly.

Use this command :-

This proves the variables exist without revealing values.
```text
python -c "from dotenv import dotenv_values; env=dotenv_values('.env'); print({k:'***' for k in env})"
```




## Dockerfile :-

Create:
```text
ai-service/Dockerfile
```

Selected the Python image.
```text
first check python version

python --version

then write this in file

FROM python:3.11.3-slim


Ensures everyone uses exactly Python 3.11.3.(if version is this )

otherwise write

FROM python:3.11-slim


```

# Set the Working Directory

Created and entered the /app directory.
write:
```text

WORKDIR /app

```

write:
This copies your project files from your computer into the /app directory inside the container.
```text
COPY . .
```

Write:

This installs all Python dependencies listed in requirements.txt.

```text
RUN pip install -r requirements.txt
```

write:
For a FastAPI application running on port 8000:
```text
EXPOSE 8000
```
write:

```text
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
# Save the Dockerfile

## Some extra commands to get some information:-


# Check whether the Dockerfile exists
```text
Get-ChildItem Dockerfile
```
# Display the contents of the Dockerfile
```text
Get-Content Dockerfile
```
# Open Terminal in the ai-service Folder

Check that the Dockerfile exists:

```text
dir
```

You should see:
```text
Dockerfile
requirements.txt
...
```

# Install Docker Desktop

https://www.docker.com/products/docker-desktop/?utm_source=chatgpt.com

# Run the installer.

# Start Docker Desktop
Open Docker Desktop from the Start Menu.
Wait until it finishes starting (Docker icon becomes stable and shows it's running).

in Configuration:-
click:- All-users installation (Requires password)


After that:

Let Docker Desktop finish installing.
If it asks for administrator permission, click Yes.
If it asks to restart, restart your PC.
Open Docker Desktop and wait until it says Docker is running.

after installation succeeded

click :-
Close and log out

# Verify Installation

inside C:\The Infimit\infimit\ai-service
```text
docker --version
```

Then run:

```text
docker build -t ai-service .

```



# Build the Docker Image

Run:

```text
docker images
```

# second time whenever you want run it again
```text
docker build -t ai-service .
```
# If you want a completely fresh build

```text
docker build --no-cache -t ai-service .
```



# Step 4: Run the Container

```text
docker run -p 8000:8000 ai-service
```

# Open the API
```text
http://localhost:8000/docs
```
If the FastAPI Swagger page opens, your Docker setup is working correctly.


# Check Docker When You Reach a Milestone

For example:

Dockerfile completed ✅
New feature completed ✅
Ready to test the application in a container ✅

Then run:

```text
docker build -t ai-service .
docker run -p 8000:8000 ai-service
```

# During Development

only need to make sure Docker Desktop is running (Windows).

Quick check:

```text
docker ps
```

If it shows a table (even an empty one), Docker is working.

Example:

```text
CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS   PORTS   NAMES
```
An empty table is fine. It means Docker is running but no containers are currently running.


## Auth middleware working

# Step 1: Create the Middleware Folder

```text
app/
├── middleware/
├── routers/
└── main.py
```

# Step 2: Create the Middleware File

```text
auth_middleware.py
```

# Step 3: Add Imports

Open auth_middleware.py and write:

```text
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
```
# Step 4: Create Middleware Class

```text
class AuthMiddleware(BaseHTTPMiddleware):
    pass
```
# Step 5: Create the Dispatch Method

```text
class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        return response
```

dispatch() runs for every request.
call_next(request) sends the request to the endpoint.
return response sends the response back.

# Step 6: Register the Middleware in main.py

Open:

```text
app/main.py
```

Import the Middleware

Add:

```text
from app.middleware.auth_middleware import AuthMiddleware
```

# Register the Middleware

```text
app.add_middleware(AuthMiddleware)
```

look like this:

```text
from fastapi import FastAPI
from app.middleware.auth_middleware import AuthMiddleware

app = FastAPI()

app.add_middleware(AuthMiddleware)
```

# Step 7: Verify the Middleware Runs
Temporarily update auth_middleware.py:

```text
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        print("Auth Middleware Executed")

        response = await call_next(request)
        return response
```
This is a simple test. Every request should print:

```text
Auth Middleware Executed
```
# Create logging middleware

```text
# app/middleware/logging.py

import time
from fastapi import Request

async def logging_middleware(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    duration = time.time() - start

    print(
        f"{request.method} {request.url.path} "
        f"Status={response.status_code} "
        f"Time={duration:.2f}s"
    )

    return response
```
# Register in main.py:

```text
app.middleware("http")(logging_middleware)
```

# Step 8: Run the Application

```text
uvicorn app.main:app --reload
```

# Step 9: Test

```text
http://localhost:8000/docs

```

see 

```text
Auth Middleware Executed
```

in the terminal, then your middleware is working correctly. ✅


# Step 10: Read the Authorization Header

```text
app/middleware/auth_middleware.py
```

Replace the code inside dispatch() with:

```text
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return JSONResponse(
                status_code=401,
                content={"detail": "Authorization token required"}
            )

        response = await call_next(request)
        return response
```

This code checks whether the request contains an:
```text
Authorization
```

# header.

If the header is missing, the request is blocked and returns:
```text
{
  "detail": "Authorization token required"
}
```

with status code:
```text
401 Unauthorized
```


# Metrics Skeleton Working

## Create metrics.py in services

```text
# app/services/metrics.py

metrics = {
    "requests_total": 0
}
```

Middleware:

```text
metrics["requests_total"] += 1
```

Endpoint:

```text
@app.get("/metrics")
def metrics_endpoint():
    return metrics
```

# 3. Model Loader Skeleton Working


Create:

```text
# app/services/model_loader.py

def load_model():
    print("Loading model...")
    return None
```
Startup:

```text
load_model()
```

Later you can load Hugging Face or Ollama models.

# 4. Tests Passing


```text
tests/
 └── test_health.py
``` 


# 5. GitHub Actions Passing

Create:

```text
.github/workflows/tests.yml
```


```text
name: Tests

on:
  push:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - run: pip install -r requirements.txt

      - run: pytest
```

# 6. README Completed

```text
# AI-Service

## Overview

AI-Service is a FastAPI-based backend service for AI workflows and news summarization.

## FastAPI

FastAPI is a modern, high-performance Python framework for building APIs and backend services.

**Used for:**

* AI APIs
* LLM Integrations
* Semantic Search
* Embeddings
* Vector Database Operations
* AI Microservices

## Subphase 1 Status

* ✅ FastAPI Service Running
* ✅ Docker Working
* ✅ Health Endpoint Working
* ✅ Ready Endpoint Working
* ✅ Auth Middleware Working
* ✅ Logging Middleware Working
* ✅ Metrics Skeleton Working
* ✅ Model Loader Skeleton Working
* ✅ Tests Passing
* ✅ GitHub Actions Passing
* ✅ README Completed
* ✅ .env.example Completed
* ✅ Models Stored Using Volume Mount

## Current Tasks

* Complete News Summarization
* Convert News into Key Points
* Keyword Extraction for Better Search

## Author

Infimit Team

```

# 7. .env.example Completed

Create:

```text
AI_INTERNAL_KEY=your_key_here
PORT=8000
LOG_LEVEL=INFO
MODELS_CACHE_DIR=/models
ENABLE_METRICS=true
```
Never put real keys here.



# 8. Models Stored Using Volume Mount

```text
volumes:
  - ./models:/models
```

```text
VOLUME ["/models"]
```

# dependencies.py

```text
from fastapi import Header, HTTPException
from app.config import settings

def verify_internal_key(
    x_internal_key: str = Header(...)
):
    print("verify_internal_key called")
    if x_internal_key != settings.AI_INTERNAL_KEY:
        raise HTTPException(
            status_code=403,
            detail="Unauthorized"
        )

    return True
```

# models-create folder inside the app
and then create metrics_model.py

paste:-

```text
from pydantic import BaseModel

class MetricsResponse(BaseModel):
    total_requests: int
    successful_requests: int
    failed_requests: int
```

# create utils folder inside the app

## and add cache.py and text.py

# inside cache.py 

```text
# Speed up system using memory caching
import time

_cache = {}
_cache_ttl = {}


def set_cache(key: str, value, ttl: int = 60):
    """Store value with time-to-live (TTL in seconds)"""
    _cache[key] = value
    _cache_ttl[key] = time.time() + ttl


def get_cache(key: str):
    """Return cached value if not expired"""
    if key not in _cache:
        return None

    if time.time() > _cache_ttl.get(key, 0):
        # expired
        _cache.pop(key, None)
        _cache_ttl.pop(key, None)
        return None

    return _cache[key]


def delete_cache(key: str):
    _cache.pop(key, None)
    _cache_ttl.pop(key, None)


def clear_cache():
    _cache.clear()
    _cache_ttl.clear()
```

## text.py

```text
# utils/text.py

import re

def clean_text(text: str) -> str:
    """Remove extra spaces and normalize text"""
    return re.sub(r"\s+", " ", text).strip()


def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate long text safely"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def to_lower(text: str) -> str:
    """Convert text to lowercase safely"""
    return text.lower().strip()


def remove_special_chars(text: str) -> str:
    """Remove special characters"""
    return re.sub(r"[^a-zA-Z0-9\s]", "", text)
```


# inside the router ->summarize.py add this line:-


```text
from app.utils.text import clean_text, truncate_text
```

# Run this command:-

```text
python -m pip install pydantic-settings
```

