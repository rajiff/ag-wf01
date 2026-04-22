import pathlib
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

class Retriever:

    def __init__(self):
        db_path = pathlib.Path(__file__).parent.parent / "chroma_db" # Path should map the ingested path
        self.client = PersistentClient(path=str(db_path))
        self.collection = self.client.get_or_create_collection("docs")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def retrieve(self, query: str, top_k: int = 2):
        query_embedding = self.model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results["documents"][0]