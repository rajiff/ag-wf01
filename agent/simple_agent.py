from agent.base import Agent
from models.message import Message, Response
from llm.local_llm import LocalLLM
from tools.retrieval_tool import RetrievalTool

# Query → LLM (decide) → (Retrieve?) → LLM → Response

class SimpleAgent(Agent):

    def __init__(self):
        self.llm = LocalLLM()
        self.retrieval_tool = RetrievalTool()

    def should_skip_rag(self, query: str) -> bool:
        if len(query.split()) < 4:
            return True
        return False
    
    def handle(self, message: Message) -> Response:
        query = message.content

        # Step 1: Decide if retrieval is needed
        decision_prompt = f"""
You are an AI assistant.

Retrieval from external documents is expensive and should be used only if necessary.

If the question can be answered using general knowledge, say NO.
If the question requires specific or unknown information, say YES.

Answer ONLY with YES or NO.

Question:
{query}
"""
        if self.should_skip_rag(query):
            use_rag = False
        else:
            decision = self.llm.generate(decision_prompt).strip().upper()
            
            use_rag = "YES" in decision

        print(f"[Decision] use_rag={use_rag}")

        # Step 2: Conditional retrieval
        if use_rag:
            context = self.retrieval_tool.execute(query)

            prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""
        else:
            prompt = f"""
Answer the question directly.

Question:
{query}

Answer:
"""

        # Step 3: Generate final answer
        output = self.llm.generate(prompt)

        return Response(content=output.strip())
    