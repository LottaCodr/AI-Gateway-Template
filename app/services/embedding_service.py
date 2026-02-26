import uuid

from app.models.clip_model import clip_model
from app.core.vector_store import vector_store

def generate_embedding(crop):
    vector = clip_model.embed(crop)
    embedding_id = str(uuid.uuid4())

    # Vector DB insertion happens later
    vector_store.upsert(embedding_id, vector)

    return embedding_id