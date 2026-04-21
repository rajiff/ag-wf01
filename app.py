from agent.simple_agent import SimpleAgent
from models.message import Message

def main():
    agent = SimpleAgent()
    
    while True:
        user_input = input("You (type 'exit' to quit): ")

        if user_input.lower() in ["exit", "quit"]:
            print("Assistant: Goodbye!")
            break

        message = Message(content=user_input)
        
        response = agent.handle(message)
        
        print(f"Assistant: {response.content}")

if __name__ == "__main__":
    main()