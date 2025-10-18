# embeddings.py
from sentence_transformers import SentenceTransformer
import numpy as np

# Load a small, fast model suitable for recommendations
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

class EmbeddingService:
    def __init__(self, model_name=EMBEDDING_MODEL_NAME):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts):
        """
        Takes a list of strings and returns a numpy array of embeddings.
        """
        return self.model.encode(texts, show_progress_bar=False, convert_to_numpy=True)

    def embed_text(self, text):
        """
        Takes a single string and returns its embedding as a 1D numpy array.
        """
        return self.embed_texts([text])[0]
