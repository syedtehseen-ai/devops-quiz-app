from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Topic(BaseModel):
    topic: str

@app.post("/get-questions")
def get_questions(data: Topic):
    prompt = f"Generate 3 DevOps interview questions about {data.topic}."

    # Ollama runs on localhost:11434 by default
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",  # or mistral, codellama, etc.
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return {"questions": result["response"]}