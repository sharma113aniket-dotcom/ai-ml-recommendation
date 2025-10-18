from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from app.recommender import Recommender
from cv_model import CVModel
import os

DATA_CSV = os.path.join(os.path.dirname(__file__), 'data', 'products.csv')

app = FastAPI(title="Product Recommendation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# initialize modules
recommender = Recommender(DATA_CSV)
cv_model = CVModel()

class QueryIn(BaseModel):
    prompt: str
    k: int = 5

@app.post("/api/recommend")
def recommend(q: QueryIn):
    """Return top-k semantic recommendations for a prompt."""
    results = recommender.recommend(q.prompt, top_k=q.k)
    return {"query": q.prompt, "results": results}

@app.get("/api/analytics")
def analytics():
    """Return simple dataset statistics."""
    return recommender.get_all_stats()

@app.post("/api/infer-image")
async def infer_image(file: UploadFile = File(...)):
    """Run CV model inference on uploaded image."""
    content = await file.read()
    res = cv_model.infer_image_bytes(content)
    return res

@app.get("/")
def root():
    return {"message": "Backend running!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
