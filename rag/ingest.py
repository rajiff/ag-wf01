# Run once python rag/ingest.py
import pathlib
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

def ingest():
    db_path = pathlib.Path(__file__).parent.parent / "chroma_db"
    client = PersistentClient(path=str(db_path))
    
    collection = client.get_or_create_collection("docs")

    model = SentenceTransformer("all-MiniLM-L6-v2")

    with open("data/docs.txt", "r") as f:
        docs = [line.strip() for line in f.readlines() if line.strip()]

    embeddings = model.encode(docs).tolist()
    ids = [str(i) for i in range(len(docs))]

    collection.add(
        documents=docs,
        embeddings=embeddings,
        ids=ids
    )
    print("Ingestion complete")


if __name__ == "__main__":
    ingest()