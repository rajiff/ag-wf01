from agent.base import Agent
from models.message import Message, Response

class SimpleAgent(Agent):

    def handle(self, message: Message) -> Response:
        return Response(content=f"Echo: {message.content}")