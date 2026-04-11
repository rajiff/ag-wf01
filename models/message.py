from dataclasses import dataclass

@dataclass
class Message:
    content: str


@dataclass
class Response:
    content: str
    source: str = "agent"
