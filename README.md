# Product Recommendation Web App (AI/ML Intern Assignment)

## Overview
This project demonstrates a full-stack product recommendation web app combining:
- semantic search-based recommendation (embeddings + FAISS),
- NLP clustering,
- a CV inference endpoint (pretrained ResNet),
- a frontend React app,
- GenAI integration suggestions via LangChain & transformers.

## Repo Structure
(see earlier directory tree)

## Setup - Backend
1. Install Python 3.9+ and a virtualenv:
python -m venv venv
source venv/bin/activate # on Windows: venv\Scripts\activate
pip install -r backend/app/requirements.txt


2. Place the dataset CSV at `backend/app/data/products.csv`. (Download link provided in assignment)

3. Optionally precompute embeddings:
- Run the model training notebook to create `embeddings.npy`.
- Or backend will compute embeddings at startup (may take a few minutes).

4. Start backend:
cd backend/app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload


## Setup - Frontend
1. From repository root:
cd frontend
npm install
npm start

2. Frontend expects backend at `http://localhost:8000`. Adjust API URLs in `src/components` if needed.

## Notes & Customization
- Vector DB: This project uses FAISS (local) for embeddings. To use Pinecone:
- Install `pinecone-client`, set your API key and alter `recommender.py` to push/query Pinecone.
- GenAI: Implemented using HuggingFace transformers (GPT-2 family). For higher quality descriptions, consider using OpenAI or larger HF models.
- CV: `cv_model.py` uses pretrained ResNet for quick inference. For fine-tuned classification, include a training loop in `model_training.ipynb`.

## How to submit
- Push the whole repository to GitHub.
- Fill the provided Google Form with:
- GitHub Link
- Deployed Link (optional)
- Any attachments (notebooks / spreadsheets)

## Contact
If anything is broken during evaluation, please check logs and ensure dataset is placed correctly.


