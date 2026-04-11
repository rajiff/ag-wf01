from abc import ABC, abstractmethod

class Tool(ABC):
    
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def execute(self, input: str) -> str:
        pass