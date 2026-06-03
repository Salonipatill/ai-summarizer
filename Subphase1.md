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
