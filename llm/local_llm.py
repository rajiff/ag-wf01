import requests
from config.settings import DEFAULT_MODEL, MODEL_NAME
from llm.base import LLM

class LocalLLM(LLM):

    def __init__(self, model: str = MODEL_NAME or DEFAULT_MODEL):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str) -> str:
        response = requests.post(self.url, json={
            "model": self.model,
            "prompt": prompt,
            "stream": False
        })

        return response.json()['response']