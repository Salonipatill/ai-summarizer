from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

from ai_service import summarize_text

app = FastAPI()

templates = Jinja2Templates(directory="templates")


# Show homepage
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Handle summarization request
@app.post("/summarize")
def summarize(request: Request, text: str = Form(...)):
    summary = summarize_text(text)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "original_text": text,
            "summary": summary
        }
    )