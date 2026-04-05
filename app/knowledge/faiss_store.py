import faiss
import numpy as np

#dimension for a miniLM
DIM = 384
index = faiss.IndexFlatL2(DIM)

#store mapping: vector index >> Db id
id_map = []