#from sentence_transformers import SentenceTransformer
import numpy as np

from app.knowledge.vector_store import index
from app.knowledge.kb_data import KB
from app.knowledge.embedder import model


#model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_solution(problem):
    if not problem:
        return "No known solution"

    q = model.encode([problem])

    D, I = index.search(np.array(q), k=1)

    idx = I[0][0]

    return KB[idx]["solution"]