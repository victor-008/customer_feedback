from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from app.knowledge.kb_data import KB


model = SentenceTransformer("all-MiniLM-L6-v2")


texts = [x["problem"] for x in KB]

embeddings = model.encode(texts)

dim = embeddings.shape[1]

index = faiss.IndexFlatL2(dim)

index.add(np.array(embeddings))