#from sentence_transformers import SentenceTransformer
import numpy as np

from app.knowledge.faiss_store import index, id_map
from app.database.db import SessionLocal
from app.database.models import Feedback
from app.knowledge.embedder import model

#model = SentenceTransformer("all-MiniLM-L6-v2", local_files_only=True)

def retrieve_from_faiss(problem, top_k=3):
    if not problem:
        return []
    q = model.encode([problem])
    D, I = index.search(np.array(q), k=top_k)
    db = SessionLocal()
    results = []
    
    for idx in I[0]:
        if idx < len(id_map):
            db_id = id_map[idx]
            row = db.query(Feedback).get(db_id)

            if row and row.final_solution:
                results.append(row.final_solution)
    db.close()
    return results