#new after llm
from app.database.db import SessionLocal
from app.database.models import Feedback
from app.knowledge.emedder import get_embedding
from app.knowledge.faiss_manager import add_to_index


def save_feedback(data):

    db = SessionLocal()
    emb = get_embedding(data.get("problem", ""))

    fb = Feedback(

        text=data.get("text"),

        category=data.get("category"),

        problem=data.get("problem"),

        suggestion=data.get("suggestion"),

        rule_suggestion=data.get("rule_solution"),

        llm_analysis=data.get("llm_analysis"),

        final_solution=data.get("final_solution"),
        embedding = emb,

    )

    db.add(fb)
    db.commit()
    db.refresh(fb)

    if fb.problem:
        add_to_index(
            text=fb.problem,
            db_id=fb.id
        )

    db.close() 

    return fb
