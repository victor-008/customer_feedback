# # def analyze_feedback(text, category, problem, suggestion):


# # #def analyze_feedback(text, category, problem,suggestion):
# #     prompt = f"""
# # You are an industrial customer feedack analysis AI.

# # Feedback: {text}
# # Category: {category}
# # Detected problem: {problem}
# # Customer suggestion: {suggestion}

# # Tasks:
# # 1. Explain the problem
# # 2. Evaluate the suggestion
# # 3. Give best solution
# # 4. Give short answer


# # Output format:

# # Problem:
# # Suggestion evaluation:
# # Reccomended solution:
# # Explanation:
# # """
    
# #     return ask_llama(prompt)
# from app.llm.llama_engine import ask_llama
# import requests

# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL = "llama3"
# #Suggested: {suggestion}
# def analyze_feedback(text, category, problem, suggestion, context=""):

#     prompt = f"""

#     You are a customer support AI

#     Feedback: {text}

#     Category: {category}
#     Problem: {problem}
    
#     Customer suggestion: {suggestion}

#     Known solution: {context}

#     Give final recommended solution.
#     Keep answer short
#     """

#     payload = {
#             "model": MODEL,
#             "prompt" : prompt,
#             "stream": False,
#         }
#     try:
#             r = requests.post(
#                 OLLAMA_URL,
#                 json=payload,
#                 timeout=60
#             )
#             data = r.json()
#             return data["response"]
#     except Exception as e:


#             return str(e)
    







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