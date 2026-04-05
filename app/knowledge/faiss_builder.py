from app.database.db import SessionLocal
from app.database.models import Feedback
import numpy as np
from app.knowledge.faiss_store import index, id_map

def build_faiss_index():
    db = SessionLocal()
    rows = db.query(Feedback).all()
    vectors = []
    for row in rows:
        if row.embedding:
            emb = np.frombuffer(row.embedding, dtype=np.float32)
            vectors.append(emb)
            id_map.append(row.id)
    if vectors:
        index.add(np.array(vectors))
    db.close()
    print(f"FAISS index built with {len(vectors)} vectors")