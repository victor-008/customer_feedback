# from fastapi import APIRouter
# from app.services.feedback_service import process_feedback
# from app.services.db_service import get_all_feedback


# router = APIRouter()

# @router.post("/feedback")
# def feedback(text: str):
#     return process_feedback(text)
    
# @router.get("/feedback")
# def read_feedback():

#     return get_all_feedback()

# @router.get("/health")
# def health():
#     return {"status": "ok"}


#after llm
from fastapi import APIRouter
from app.nlp.pipeline import process_feedback
from app.services.feedback_service import save_feedback

router = APIRouter()


@router.post("/feedback")
def feedback(text: str):

    result = process_feedback(text)

    #addition
    #result["text"] = text

    save_feedback(result)

    return result

#chat endpoint
@router.post("/chat")
def chat(text: str):
    result = process_feedback(text)
    save_feedback(result)
    
    return{
        "reply": result["final_solution"]
    }