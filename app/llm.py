import os
import requests
import logging

logger = logging.getLogger(__name__)

class LLMQueryError(Exception):
    pass

def query_groq_llm(topic: str):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise LLMQueryError("GROQ_API_KEY not set in environment variables.")

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    topic_lower = topic.casefold()
    if topic_lower == "social":
        prompt = "Generate 5 Questions from Primary Social Studies - Class 3 ICSE BOARD by Frank Bros & Co on the topic: Social. Respond only as a numbered list."
    elif topic_lower == "computer":
        prompt = "Generate 5 Questions from Mastering Essential Computer Skills - Class 3 ICSE BOARD by TRACKPAD iPro Ver. 4.1 on the topic: Computer. Respond only as a numbered list."
    elif topic_lower == "Hindi":
        prompt = "Generate 5 Questions from Hindi Grammar - Class 3 ICSE BOARD. first 3 chapters. Respond only as a numbered list."
    else:
        prompt = f"Generate 5 DevOps interview questions on the topic: {topic}. Respond only as a numbered list."

    payload = {
        "model": "gemma2-9b-it",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 300
    }
    import json
    print("Sending request to Groq LLM API:")
    print(json.dumps(payload, indent=2))


    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        raise LLMQueryError("Request to Groq API timed out.")
    except requests.exceptions.RequestException as e:
        raise LLMQueryError(f"API request failed: {str(e)}")
    except ValueError as e:
        raise LLMQueryError("Failed to parse JSON response from Groq API.")
