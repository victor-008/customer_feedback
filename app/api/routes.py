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