import pickle
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load df and embeddings from pickle
file_path = os.path.join(os.path.dirname(__file__), "bot_data.pkl")
with open(file_path, "rb") as f:
    df, embeddings = pickle.load(f)

# Load the model separately
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

def search_query(query, top_k=3):
    query_embedding = model.encode([query])
    similarity_scores = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = similarity_scores.argsort()[-top_k:][::-1]

    results = []
    for idx in top_indices:
        row = df.iloc[idx]
        results.append({
            "topic": row["topic"],
            "category": row["category"],
            "description_en": row["description_en"],
            "advice_en": row["advice_en"],
            "description_hi": row["description_hi"],
            "advice_hi": row["advice_hi"]
        })

    return results
