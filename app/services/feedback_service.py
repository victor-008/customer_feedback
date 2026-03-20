""" #connects:
    NLP pipeline
    Database
    Logger
"""

from app.nlp.pipeline import run_pipeline
from app.services.db_service import save_feedback
from app.core.logger import get_logger

log = get_logger()

def process_feedback(text: str):
    try: 
        log.info("Processing feedback")
        result = run_pipeline(text)
        save_feedback(result)
        log.info("Saved to database")

        return result
    
    except Exception as e:
        log.error(str(e))
        return {"error": str(e)}