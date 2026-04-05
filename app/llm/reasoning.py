import requests


OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "llama3"


def analyze_feedback(
    text,
    category,
    problem,
    suggestion,
    context=""
):

    prompt = f"""
You are a customer support AI.

Feedback: {text}

Category: {category}

Problem: {problem}

Customer suggestion: {suggestion}

Known solution: {context}

Give final recommended solution.
Keep answer short.
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
    }

    try:

        r = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60
        )

        data = r.json()

        return data["response"]

    except Exception as e:

        return str(e)