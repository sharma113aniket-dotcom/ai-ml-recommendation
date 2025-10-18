import pandas as pd
import numpy as np
import faiss
from sklearn.metrics.pairwise import cosine_similarity
from embeddings import EmbeddingService

class Recommender:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        # create a combined text field for better semantics
        self.df['combined_text'] = (
            self.df['title'].fillna('') + ' ' +
            self.df['brand'].fillna('') + ' ' +
            self.df['description'].fillna('') + ' ' +
            self.df['categories'].fillna('')
        )
        self.embedder = EmbeddingService()
        self.embeddings = None
        self.index = None
        self._build_index()

    def _build_index(self):
        texts = self.df['combined_text'].tolist()
        self.embeddings = self.embedder.embed_texts(texts)
        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)
        faiss.normalize_L2(self.embeddings)
        self.index.add(self.embeddings.astype('float32'))

    def recommend(self, query, top_k=5):
        q_emb = self.embedder.embed_text(query).astype('float32')
        faiss.normalize_L2(q_emb.reshape(1, -1))
        D, I = self.index.search(q_emb.reshape(1, -1), top_k)
        results = []
        for idx in I[0]:
            row = self.df.iloc[int(idx)].fillna('N/A').to_dict()   # NaN safe here!
            results.append(row)
        return results

    def get_all_stats(self):
        stats = {
            'num_products': len(self.df),
            'unique_brands': int(self.df['brand'].nunique()),
            'categories_count': int(self.df['categories'].nunique())
        }
        return stats
