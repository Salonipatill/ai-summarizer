# Target Response

```text
{
  "summary": "...",
  "confidence": 0.87,
  "model": "llama3-8b-8192",
  "tokensIn": 1240,
  "tokensOut": 55,
  "cached": false
}
```

# Step 1: Install required tools
```text
pip install transformers torch fastapi pydantic
```

```text
pip install cachetools
```

# Step 2: Create Pydantic Schemas

## request + response contract

```text
from pydantic import BaseModel, Field
from typing import Literal

class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=1)
    maxWords: int = Field(..., ge=20, le=200)
    style: Literal["neutral", "engaging", "academic"]

class SummarizeResponse(BaseModel):
    summary: str
    confidence: float
    model: str
    tokensIn: int
    tokensOut: int
    cached: bool
```

# Step 3: Load model



# step 4 : Step 4: Token counter utility
```text
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

def count_tokens(text: str) -> int:
    return len(tokenizer.encode(text))
```



#  Step 5: Simple cache

```text
# utils/cache.py

import time
import hashlib
from typing import Any, Dict, Optional

# -------------------------
# IN-MEMORY STORAGE
# -------------------------
_cache: Dict[str, Any] = {}
_cache_ttl: Dict[str, float] = {}


# -------------------------
# CACHE KEY GENERATION
# -------------------------
def get_cache_key(text: str, maxWords: int, style: str, model: str = "default") -> str:
    """
    Generate a stable and collision-safe cache key using hashing.
    """
    raw = f"{text.strip()}|{maxWords}|{style}|{model}"
    return hashlib.sha256(raw.encode()).hexdigest()


# -------------------------
# SET CACHE
# -------------------------
def set_cache(key: str, value: dict, ttl: int = 60) -> None:
    """
    Store value with TTL (time-to-live in seconds)
    """
    _cache[key] = value
    _cache_ttl[key] = time.time() + ttl


# -------------------------
# GET CACHE
# -------------------------
def get_cache(key: str) -> Optional[dict]:
    """
    Return cached value if exists and not expired
    """
    if key not in _cache:
        return None

    # check expiry
    if time.time() > _cache_ttl.get(key, 0):
        _cache.pop(key, None)
        _cache_ttl.pop(key, None)
        return None

    return _cache[key]


# -------------------------
# DELETE CACHE
# -------------------------
def delete_cache(key: str) -> None:
    """
    Remove specific cache entry
    """
    _cache.pop(key, None)
    _cache_ttl.pop(key, None)


# -------------------------
# CLEAR ALL CACHE
# -------------------------
def clear_cache() -> None:
    """
    Clear entire cache (use carefully)
    """
    _cache.clear()
    _cache_ttl.clear()


# -------------------------
# CHECK IF CACHE EXISTS
# -------------------------
def is_cached(key: str) -> bool:
    """
    Check if key exists and is not expired
    """
    return key in _cache and time.time() <= _cache_ttl.get(key, 0)


# -------------------------
# OPTIONAL: CACHE SIZE (DEBUGGING)
# -------------------------
def cache_size() -> int:
    """
    Returns number of active cache entries
    """
    return len(_cache)
```


#  Step 6: FastAPI endpoint implementation

```text
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

MODEL_NAME = "facebook/bart-large-cnn"

@router.post("/v1/summarize", response_model=SummarizeResponse)
def summarize(req: SummarizeRequest):

    # -------------------------
    # 1. CACHE CHECK
    # -------------------------
    key = get_cache_key(req.text, req.maxWords, req.style)

    if key in cache:
        return {
            **cache[key],
            "cached": True
        }

    # -------------------------
    # 2. TOKEN COUNT (INPUT)
    # -------------------------
    tokens_in = count_tokens(req.text)

    # -------------------------
    # 3. MODEL INFERENCE
    # -------------------------
    result = summarizer(
        req.text,
        max_length=req.maxWords,
        min_length=20,
        do_sample=False
    )[0]["summary_text"]

    # -------------------------
    # 4. TOKEN COUNT (OUTPUT)
    # -------------------------
    tokens_out = count_tokens(result)

    # -------------------------
    # 5. CONFIDENCE (simple heuristic)
    # -------------------------
    confidence = min(0.95, 0.6 + (req.maxWords / 200))

    # -------------------------
    # 6. BUILD RESPONSE
    # -------------------------
    response = {
        "summary": result,
        "confidence": round(confidence, 2),
        "model": MODEL_NAME,
        "tokensIn": tokens_in,
        "tokensOut": tokens_out,
        "cached": False
    }

    # -------------------------
    # 7. SAVE CACHE
    # -------------------------
    cache[key] = response

    return response
```