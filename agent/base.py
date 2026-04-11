from abc import ABC, abstractmethod
from models.message import Message, Response

class Agent(ABC):
    
    @abstractmethod
    def handle(self, message: Message) -> Response:
        pass