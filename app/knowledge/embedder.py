import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    if not text:
        return None
    
    vec = model.encode([text])[0]

    return vec.tobytes()
