from agent.base import Agent
from models.message import Message, Response
from llm.local_llm import LocalLLM
from tools.retrieval_tool import RetrievalTool

class SimpleAgent(Agent):

    def __init__(self):
        self.llm = LocalLLM()
        self.retrieval_tool = RetrievalTool()

    # def handle(self, message: Message) -> Response:
    #     prompt = f"User: {message.content}\nAssistant:"
        
    #     output = self.llm.generate(prompt)

    #     if output.startswith("[LLM Error]"):
    #         return Response(content=output, source="error")

    #     return Response(content=output)

    def handle(self, message: Message) -> Response:
        query = message.content

        # Step 1: retrieve context
        context = self.retrieval_tool.execute(query)

        # Step 2: construct prompt
        prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

        output = self.llm.generate(prompt)

        return Response(content=output.strip())