#after llm 
from app.nlp.classifier import classify
from app.nlp.problem_extractor import extract_problem
from app.nlp.solution_detector import detect_solution
from app.services.recommender import recommend
from app.llm.reasoning import analyze_feedback
#from app.knowledge.retriever import retrieve_solution
#from app.knowledge.db_retriever import retrieve_from_db
from app.knowledge.faiss_retriever import retrieve_from_faiss





def process_feedback(text):

    category = classify(text)

    problem = extract_problem(text)

    suggestion = detect_solution(text)

    #fallback if  problem is None
    if not problem or problem.strip() == "":
        problem = text

    #get multiple solutions
    #retrieved = retrieve_from_db(problem, top_k=3)
    retrieved = retrieve_from_faiss(problem, top_k=3)


    if retrieved:
        rag_solution = "\n".join(retrieved)
    else:
        rag_solution = "No similar past solutions found"

    llm_analysis = analyze_feedback(
        text,
        category,
        problem,
        suggestion,
        rag_solution
    )

    #final_solution = llm_analysis

    return {

        "text": text,

        "category": category,

        "problem": problem,

        "suggestion": suggestion,

        "rule_solution": rag_solution,

        "llm_analysis": llm_analysis,

        "final_solution": llm_analysis,
    }