from app.llm.llama_engine import ask_llama

def analyze_feedback(text, category, problem, suggestion):


#def analyze_feedback(text, category, problem,suggestion):
    prompt = f"""
You are an industrial customer feedack analysis AI.

Feedback: {text}
Category: {category}
Detected problem: {problem}
Customer suggestion: {suggestion}

Tasks:
1. Explain the problem
2. Evaluate the suggestion
3. Give best solution
4. Give short answer


Output format:

Problem:
Suggestion evaluation:
Reccomended solution:
Explanation:
"""
    
    return ask_llama(prompt)