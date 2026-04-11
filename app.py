from agent.simple_agent import SimpleAgent
from models.message import Message

def main():
    agent = SimpleAgent()
    
    while True:
        user_input = input("You: ")
        message = Message(content=user_input)
        
        response = agent.handle(message)
        
        print(f"Agent: {response.content}")

if __name__ == "__main__":
    main()