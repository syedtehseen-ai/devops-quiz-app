from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import os
import logging
from dotenv import load_dotenv
load_dotenv()
from app.llm import query_groq_llm, LLMQueryError
    


# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Allow CORS if needed (e.g., frontend hosted elsewhere)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get-questions", response_class=HTMLResponse)
def generate(request: Request, topic: str = Form(...)):
    if not topic.strip():
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": "Topic must not be empty."
        })

    try:
        llm_response = query_groq_llm(topic.strip())
        content = llm_response.get("choices", [{}])[0].get("message", {}).get("content", "")

        if not content:
            raise ValueError("No content returned from LLM")

        questions = [q.strip() for q in content.strip().split("\n") if q.strip()]
        return templates.TemplateResponse("index.html", {
            "request": request,
            "questions": questions,
            "selected_topic": topic
        })

    except (LLMQueryError, ValueError) as e:
        logger.error(f"LLM query failed: {e}")
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": f"Failed to fetch questions: {str(e)}"
        })
    except Exception as e:
        logger.exception("Unexpected error:")
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": "Unexpected error occurred. Please try again later."
        })
