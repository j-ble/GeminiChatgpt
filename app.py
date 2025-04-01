from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('YOUR_API_KEY')
if not api_key:
    raise ValueError("Please set the YOUR_API_KEY environment variable")

# Initialize the Gemini client
client = genai.Client(api_key=api_key)

# Use gemini-2.5-pro-exp-03-25 as specified in the original code
MODEL_NAME = "gemini-2.5-pro-exp-03-25"

print(f"Chatting with {MODEL_NAME}. Type 'quit' or 'exit' to end.")
print("-" * 50)

# Keep track of conversation history
chat_history = []

# Main chat loop
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Exiting chat.")
            break

        if not user_input:
            continue

        # Add user message to history
        chat_history.append({"role": "user", "parts": [{"text": user_input}]})
        
        # Send the entire chat history to maintain context
        response = client.models.generate_content(
            model=MODEL_NAME, 
            contents=chat_history
        )
        
        # Add model response to history
        chat_history.append({"role": "model", "parts": [{"text": response.text}]})
        
        # Print AI response
        print(f"Gemini: {response.text}")

    except KeyboardInterrupt:
        print("\nExiting chat.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")