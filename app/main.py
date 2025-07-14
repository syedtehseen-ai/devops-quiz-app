from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get-questions", response_class=HTMLResponse)
def get_questions(request: Request, topic: str = Form(...)):
    prompt = f"Generate 5 DevOps interview questions on the topic: {topic}. Respond only as a numbered list."

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",  # or llama3, mistral
            "prompt": prompt,
            "stream": False
        }
    )

    output = response.json()["response"]
    # Convert to list of questions (split by line)
    questions = [line.strip() for line in output.split('\n') if line.strip()]
    return templates.TemplateResponse("index.html", {"request": request, "questions": questions, "topic": topic})
