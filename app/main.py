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
def generate(request: Request, topic: str = Form(...)):
    llm_response = query_groq_llm(topic)
    content = llm_response["choices"][0]["message"]["content"]
    questions = content.strip().split("\n")
    return templates.TemplateResponse("index.html", {"request": request, "questions": questions, "selected_topic": topic})