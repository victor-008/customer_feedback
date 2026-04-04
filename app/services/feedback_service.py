# """ #connects:
#     NLP pipeline
#     Database
#     Logger
# """

# from app.nlp.pipeline import run_pipeline
# from app.services.db_service import save_feedback
# from app.core.logger import get_logger

# log = get_logger()

# def process_feedback(text: str):
#     try: 
#         log.info("Processing feedback")
#         result = run_pipeline(text)
#         save_feedback(result)
#         log.info("Saved to database")

#         return result
    
#     except Exception as e:
#         log.error(str(e))
#         return {"error": str(e)}









#new after llm
from app.database.db import SessionLocal
from app.database.models import Feedback
from app.knowledge.emedder import get_embedding


def save_feedback(data):

    db = SessionLocal()
    emb = get_embedding(data["problem"])

    fb = Feedback(

        text=data["text"],

        category=data["category"],

        problem=data["problem"],

        suggestion=data["suggestion"],

        rule_suggestion=data["rule_solution"],

        llm_analysis=data["llm_analysis"],

        final_solution=data["final_solution"],
        embedding = emb,

    )

    db.add(fb)

    db.commit()
    db.refresh(fb)

    db.close() 

    return fb