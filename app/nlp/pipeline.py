from  app.nlp.preprocess import clean_text
from app.nlp.classifier import classify
from app.nlp.problem_extractor import extract_problem
from app.nlp.solution_detector import detect_solution
from app.nlp.solution_evaluator import evaluate_solution
from app.nlp.recommender import recommend

def run_pipeline(text: str):
    text_clean = clean_text(text)
    category = classify(text_clean)

    problem = None
    solution_given = None
    solution_valid = None
    recommended = None

    if category == "complaint":
        problem = extract_problem(text_clean)
        if detect_solution(text_clean):
            solution_given = text
            solution_valid = evaluate_solution(text_clean)
        recommended = recommend(problem)

    return{
        "text": text,
        "category": category,
        "problem": problem,
        "customer_solution": solution_given,
        "solution_valid": solution_valid,
        "recommended_solution": recommended
    }