# healthcare_bot.py

import pandas as pd
import numpy as np
import os
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

#  Set the correct CSV path
DATASET_PATH = "/Users/chinmayee/Documents/Health_Bridge/data/accessible_healthcare_prototype_dataset_large.csv"  # update to your actual CSV file if needed

#  Load dataset
print(" Loading dataset...")
df = pd.read_csv(DATASET_PATH)

#  Combine English and Hindi text into one searchable field
df['corpus'] = (
    df['topic'].fillna('') + " " +
    df['description_en'].fillna('') + " " +
    df['advice_en'].fillna('') + " " +
    df['description_hi'].fillna('') + " " +
    df['advice_hi'].fillna('')
)

#  Load sentence-transformer model
print(" Loading multilingual sentence-transformer model...")
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

#  Generate embeddings
print("  Generating embeddings (this may take a minute)...")
embeddings = model.encode(df['corpus'].tolist(), show_progress_bar=True)

#  Save df and embeddings to pickle (exclude model!)
OUTPUT_PATH = os.path.join("model", "bot_data.pkl")
os.makedirs("model", exist_ok=True)

with open(OUTPUT_PATH, "wb") as f:
    pickle.dump((df, embeddings), f)

print(f" Data and embeddings saved to {OUTPUT_PATH}")

# Optional CLI for testing queries manually
def get_answer(query, top_k=3):
    print("\n Searching for the most relevant information...\n")
    query_embedding = model.encode([query])
    similarity_scores = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = similarity_scores.argsort()[-top_k:][::-1]

    for i, idx in enumerate(top_indices, 1):
        row = df.iloc[idx]
        print(f"\nResult {i}:")
        print(f" Topic: {row['topic']}")
        print(f" Category: {row['category']}")
        print(" English:")
        print(f"  Description: {row['description_en']}")
        print(f"  Advice: {row['advice_en']}")
        print(" Hindi:")
        print(f"  विवरण: {row['description_hi']}")
        print(f"  सलाह: {row['advice_hi']}")
        print("-" * 50)

if __name__ == "__main__":
    print(" Healthcare Info Bot is ready!")
    print("Type your question below (in English or Hindi). Type 'exit' to quit.\n")

    while True:
        user_query = input(" You: ")
        if user_query.lower() in ["exit", "quit", "q"]:
            print(" Goodbye!")
            break
        get_answer(user_query)
