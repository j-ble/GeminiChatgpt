from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('YOUR_API_KEY')
if not api_key:
    raise ValueError("Please set the YOUR_API_KEY environment variable")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-pro-exp-03-25", contents="Explain how AI works in a few words"
)
print(response.text)