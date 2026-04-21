import requests
from config.settings import DEFAULT_MODEL, MODEL_NAME
from llm.base import LLM

class LocalLLM(LLM):

    def __init__(self, model: str = MODEL_NAME or DEFAULT_MODEL):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str) -> str:
        try:
            response = requests.post(
                self.url, 
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }, 
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            if "response" not in data:
                return "[LLM Error] Unexpected response format from model"

            return data["response"]
        except requests.exceptions.ConnectionError:
            return "[LLM Error] Cannot connect to Ollama. Is it running?"

        except requests.exceptions.Timeout:
            return "[LLM Error] LLM request timed out"

        except requests.exceptions.HTTPError as e:
            return f"[LLM Error] HTTP error: {str(e)}"

        except Exception as e:
            return f"[LLM Error] Unexpected error: {str(e)}"
