from tools.base import Tool
from rag.retriever import Retriever

class RetrievalTool(Tool):

    def __init__(self):
        self.retriever = Retriever()

    def name(self) -> str:
        return "retrieval"

    def execute(self, input: str) -> str:
        docs, distances = self.retriever.retrieve(input)
        return "\n".join(docs), distances