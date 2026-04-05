from fastapi import FastAPI

from app.core.logger import get_logger
from app.api.routes import router

from app.knowledge.faiss_builder import build_faiss_index

from app.knowledge.faiss_manager import add_to_index
from app.database.db import SessionLocal
from app.database.models import Feedback



log = get_logger()

app = FastAPI(
    title="Customer Feedback AI System",
    version="1.0"
)

@app.on_event("startup")
def startup_event():
    log.info("Feedback AI System Started")

    build_faiss_index()

def load_faiss():
    db = SessionLocal()

    try:
        feedbacks = db.query(Feedback).all()
        for f in feedbacks:
            if f.problem:
                add_to_index(f.problem, f.id)
        print(f"FAISS loaded with {len(feedbacks)} records")
    finally:
        db.close()

        

@app.get("/")
def root():
    return {"message": "API running"}

# include API routes
app.include_router(router)