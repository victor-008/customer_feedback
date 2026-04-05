#RAG using db
import numpy as np

from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.database.models import Feedback

from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve_from_db(problem):

    if not problem:
        return "No known solution"

    db = SessionLocal()

    rows = db.query(Feedback).all()

    db.close()

    if not rows:
        return "No knowledge yet"

    query_vec = model.encode([problem])[0]

    best = None
    best_score = 1e9

    for r in rows:

        if not r.embedding:
            continue

        vec = np.frombuffer(r.embedding)

        score = np.linalg.norm(vec - query_vec)

        if score < best_score:
            best_score = score
            best = r.final_solution

    if best:
        return best

    return "No similar case"