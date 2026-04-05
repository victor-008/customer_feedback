# #RAG using db
# import numpy as np
# from sqlalchemy.orm import Session
# from app.database.db import SessionLocal
# from app.database.models import Feedback
# from sentence_transformers import SentenceTransformer


# model = SentenceTransformer("all-MiniLM-L6-v2")


# def retrieve_from_db(problem, top_k=3):

#     #if not problem:
#      #   return "No known solution"

#     db = SessionLocal()

#     rows = db.query(Feedback).all()
#     if not rows:
#         return []
    
#     query_vec = model.encode([problem])[0]
#     results = []

#     for row in rows:
#         if not row.embedding:
#             continue

#         emb = np.frombuffer(row.embedding, dtype=np.float32)
#         sim = np.dot(query_vec, emb) / (np.linalg.norm(query_vec) * np.linalg.norm(emb))
#         results.append((sim, row))
#     db.close()

#     #sort y similarity
#     results.sort(key=lambda x: x[0], reverse=True)
#     top = results[:top_k]

#     return [
#         r[1].final_solution
#         for r in top
#         if r[1].final_solution
#         ]


from app.knowledge.faiss_manager import search_index
from app.database.db import SessionLocal
#from app.db.models import Feedback
from app.database.models import Feedback


def retrieve_from_db(problem: str):
    if not problem:
        return "No problem detected"

    db = SessionLocal()

    try:
        ids = search_index(problem, k=3)

        if not ids:
            return "No similar cases found"

        results = (
            db.query(Feedback)
            .filter(Feedback.id.in_(ids))
            .all()
        )

        if not results:
            return "No solutions found"

        # Combine solutions
        solutions = [
            r.final_solution for r in results if r.final_solution
        ]

        return " | ".join(solutions[:2])  # keep short

    finally:
        db.close()