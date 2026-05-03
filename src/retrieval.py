# retrieval.py – FAISS index (placeholder)

import faiss
import numpy as np

# Simple Graph2Vec‑like encoder (random for demo)

def encode_graph(g):
    # Produce a fixed‑size 128‑dim vector (random placeholder)
    rng = np.random.default_rng(seed=g.number_of_nodes())
    return rng.random(128).astype('float32')

def build_index(vectors):
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    return index
