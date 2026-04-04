# from  app.nlp.preprocess import clean_text
# from app.nlp.classifier import classify
# from app.nlp.problem_extractor import extract_problem
# from app.nlp.solution_detector import detect_solution
# from app.nlp.solution_evaluator import evaluate_solution
# from app.nlp.recommender import recommend

# #from app.llm.reasoning import analyze_feedback
# from app.llm.reasoning import analyze_feedback


# # def run_pipeline(text: str):
# #     text_clean = clean_text(text)
# #     category = classify(text_clean)

# #     problem = None
# #     solution_given = None
# #     solution_valid = None
# #     recommended = None

# #     if category == "complaint":
# #         problem = extract_problem(text_clean)
# #         if detect_solution(text_clean):
# #             solution_given = text
# #             solution_valid = evaluate_solution(text_clean)
# #         recommended = recommend(problem)

# #     return{
# #         "text": text,
# #         "category": category,
# #         "problem": problem,
# #         "customer_solution": solution_given,
# #         "solution_valid": solution_valid,
# #         "recommended_solution": recommended
# #     }

# def process_feedback(text):
#     category = classify(text)
#     problem = extract_problem(text)
#     suggestion = detect_solution(text)
#     rule_solution = recommend(problem)
#     llm_result = analyze_feedback(
#         text,
#         category,
#         problem,
#         suggestion
#     )

#     return{
#         "category" : category,
#         "problem" : problem,
#         "suggestion" : suggestion,
#         "rule_solution" : rule_solution,
#         "llm_analytics" : llm_result
#     }





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