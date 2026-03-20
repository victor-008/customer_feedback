from app.database.models import Feedback
from app.database.db import SessionLocal

def save_feedback(result: dict):
    
    db = SessionLocal()

    fb = Feedback(
        text=result["text"],
        category=result["category"],
        problem=result["problem"],
        customer_solution=result["customer_solution"],
        solution_valid=result["solution_valid"],
        recommended_solution=result["recommended_solution"],
    )

    db.add(fb)
    db.commit()
    db.close()