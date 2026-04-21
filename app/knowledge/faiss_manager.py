import faiss
import numpy as np
#from sentence_transformers import SentenceTransformer
from app.knowledge.embedder import model

DIM = 384

index = faiss.IndexFlatL2(DIM)

# Mapping FAISS → DB id
id_map = []


def embed_text(text: str):
    return model.encode([text])[0]


def add_to_index(text: str, db_id: int):
    """
    Add new feedback to FAISS
    """
    vector = embed_text(text)

    index.add(np.array([vector]).astype("float32"))

    id_map.append(db_id)


def search_index(query: str, k=3):
    """
    Search similar problems
    """
    if index.ntotal == 0:
        return []

    q = embed_text(query)

    D, I = index.search(np.array([q]).astype("float32"), k)

    results = []
    for idx in I[0]:
        if idx < len(id_map):
            results.append(id_map[idx])

    return results