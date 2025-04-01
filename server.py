# server.py
from mcp.server.fastmcp import FastMCP
from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Google AI client
api_key = os.getenv('YOUR_API_KEY')
if not api_key:
    raise ValueError("Please set the YOUR_API_KEY environment variable")

client = genai.Client(api_key=api_key)

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a Gemini AI query tool
@mcp.tool()
def generate_ai_content(prompt: str) -> str:
    """Generate content using Google's Gemini AI model"""
    response = client.models.generate_content(
        model="gemini-2.5-pro-exp-03-25", contents=prompt
    )
    return response.text


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Run the MCP server
    mcp.run(transport="stdio")