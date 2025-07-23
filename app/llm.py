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

    # Build the message list based on topics
    messages = []
    if topic.lower() == "social":
        messages.append({
            "role": "user",
            "content": f"Generate 5 Questions from Primary Social Studies - Class 3 ICSE BOARD by Frank Bros & Co on the topic: {topic}. Respond only as a numbered list."
        })
    elif topic.lower() == "computer":
        messages.append({
            "role": "user",
            "content": f"Generate 5 Questions from Mastering Essential Computer Skills - Class 3 ICSE BOARD by TRACKPAD iPro Ver. 4.1 on the topic: {topic}. Respond only as a numbered list."
        })
    else:
        messages.append({
            "role": "user",
            "content": f"Generate 5 DevOps interview questions on the topic: {topic}. Respond only as a numbered list."
        })

    payload = {
        "model": "gemma-7b-it",
        "messages": messages,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
