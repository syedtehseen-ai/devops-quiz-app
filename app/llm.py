import os
import requests

def query_groq_llm(topic):
    api_key = os.environ.get("GROQ_API_KEY")
    
    if not api_key:
        raise EnvironmentError("GROQ_API_KEY not set.")
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gemma-7b-it",  # fast, lightweight
        "messages": [
            {"role": "user", "content": f"Generate 5 DevOps interview questions on {topic}"}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
