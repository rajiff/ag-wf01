from agent.base import Agent
from models.message import Message, Response
from llm.local_llm import LocalLLM

class SimpleAgent(Agent):

    def __init__(self):
        self.llm = LocalLLM()

    def handle(self, message: Message) -> Response:
        prompt = f"User: {message.content}\nAssistant:"
        
        output = self.llm.generate(prompt)

        if output.startswith("[LLM Error]"):
            return Response(content=output, source="error")

        return Response(content=output)