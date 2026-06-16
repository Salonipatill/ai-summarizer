# Finalize multi-stage Dockerfile (image size, security, non-root, healthcheck).


Final Dockerfile:
Multi-stage, non-root user app.
Builder stage installs deps; runner has only runtime.
Healthcheck against /v1/healthz.
Image size target: ≤ 1.5 GB.
Pin CPU-only torch wheels.
HF_HUB_OFFLINE=1 if model is bundled into the image (decide based on staging hosting); otherwise rely on volume.



# Builder
FROM python:3.11-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*
COPY pyproject.toml requirements.txt ./
RUN pip wheel --wheel-dir /wheels --no-deps --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt

# Runner
FROM python:3.11-slim
RUN useradd --create-home --uid 1001 app && mkdir -p /models && chown -R app /models
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*.whl && rm -rf /wheels
COPY app/ app/
USER app
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/v1/healthz', timeout=3)" || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]



# Deploy ai-service to staging via root CI; reachable from backend's staging deployment.

Staging deploy automation:
GitHub Actions workflow .github/workflows/ai-service-deploy.yml:
On push to main: build → push GHCR → deploy to Render/Railway.
Post-deploy: poll /v1/healthz until 200; fail deploy on timeout.
Optionally trigger a one-time /v1/summarize warm-up call from CI as a post-deploy step.


# Configure model storage strategy in staging (volume mount + pre-warmed by deploy step).

WARM_ON_STARTUP=true recommended (predictable first request).
READY_REQUIRES_MODEL=true so the load balancer doesn't send traffic until model loaded.
EXPOSE_DOCS=false.
LRU_CAPACITY=2048, LRU_TTL_SEC=86400.
Internal key rotated from dev value.

# Run a staging soak test (30 min, 50 concurrent users) and capture results.

30 minutes, 50 concurrent users mixed cache-hit + cache-miss.
Capture p50/p95/p99, RSS, cache hit ratio, Sentry errors.
Write to ai-service/docs/staging-soak.md.


# Finalize Grafana dashboard spec and Sentry integration.



Update + freeze on-call runbook for staging.
Write Phase 2 readiness report (gap analysis, recommended sequence for /keywords → /recommend → /moderate).
Tag v0.5.0. MVP complete from AI side.