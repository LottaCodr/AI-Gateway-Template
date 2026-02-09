import uuid

def generate_embedding(crop):
    vector = clip_model.embed(crop)
    embedding_id = str(uuid.uuid4())

    # Vector DB insertion happens later
    # vector_Store.upsert(embedding_id, vector)

    return embedding_id