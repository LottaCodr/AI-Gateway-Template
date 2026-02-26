class InMemoryVectorStore:
    def __init__(self) -> None:
        self.store = {}

    def upsert(self, embedding_id: str, vector: list):
        self.store[embedding_id] = vector

    def get(self, embedding_id: str):
        return self.store.get(embedding_id)

vector_store = InMemoryVectorStore()