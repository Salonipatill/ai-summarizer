```text
User → Router → Service → Loader → Groq API
                      ↓
                   Cache system
```

## When a user sends text, the request goes to FastAPI router. Router calls the service layer which handles business logic. Before calling Groq API, the service checks cache. If cached result exists, it returns instantly. Otherwise it calls Groq via loader, gets response, stores it in cache, and returns result.