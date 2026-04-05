#import requests
from app.llm.llama_engine import ask_llama


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
    You are an expert telecom customer support AI.

    Customer feedback: {text}

    Detected category: {category}

    Detected problem: {problem}

    Customer suggestion: {suggestion}

    Relevant past solutions: {context}

    Instructions:
    - Give a clear and actionable solution
    - be specific (no generic advice)
    - if similar solutions exist, adapt them
    - if no solution exists, say: "No known solution yet"
    - Keep response professional and concise

    Final Answer:
    """

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        }

    return ask_llama(prompt)
# try:

#     r = requests.post(
#         OLLAMA_URL,
#         json=payload,
#         timeout=60
#         )

#     data = r.json()

#         return data["response"]

# except Exception as e:

#     return str(e)