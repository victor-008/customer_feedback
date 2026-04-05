#after llm 
from app.nlp.classifier import classify
from app.nlp.problem_extractor import extract_problem
from app.nlp.solution_detector import detect_solution
from app.services.recommender import recommend
from app.llm.reasoning import analyze_feedback
#from app.knowledge.retriever import retrieve_solution
from app.knowledge.db_retriever import retrieve_from_db


def process_feedback(text):

    category = classify(text)

    problem = extract_problem(text)

    suggestion = detect_solution(text)

    #rule_solution = recommend(problem)

    
    if problem:
        rag_solution = retrieve_from_db(problem)
    else:
        rag_solution = "No problem detected"

    llm_analysis = analyze_feedback(
        text,
        category,
        problem,
        suggestion,
        rag_solution
    )

    final_solution = llm_analysis

    return {

        "text": text,

        "category": category,

        "problem": problem,

        "suggestion": suggestion,

        "rule_solution": rag_solution,

        "llm_analysis": llm_analysis,

        "final_solution": final_solution,
    }