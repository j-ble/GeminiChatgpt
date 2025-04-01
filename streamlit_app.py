import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv('YOUR_API_KEY')
if not api_key:
    st.error("Please set the YOUR_API_KEY environment variable")
    st.stop()

# Initialize the Gemini client
client = genai.Client(api_key=api_key)

# Model configuration
MODEL_NAME = "gemini-2.5-pro-exp-03-25"

# Set page title and layout
st.set_page_config(
    page_title="Gemini Chat App",
    page_icon="💬",
    layout="centered"
)

# App title
st.title("💬 Gemini Chat")
st.caption(f"Using {MODEL_NAME}")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    role = message["role"]
    content = message["parts"][0]["text"]
    with st.chat_message(role if role != "model" else "assistant"):
        st.write(content)

# Chat input
if prompt := st.chat_input("Ask something..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "parts": [{"text": prompt}]})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=st.session_state.messages
                )
                
                # Display the response
                st.write(response.text)
                
                # Add model response to chat history
                st.session_state.messages.append(
                    {"role": "model", "parts": [{"text": response.text}]}
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Add instructions in the sidebar
with st.sidebar:
    st.subheader("Instructions")
    st.markdown("""
    1. Type your message in the chat input box
    2. Press Enter to send
    3. Wait for Gemini's response
    4. Continue the conversation naturally
    
    Your entire conversation history is maintained for context.
    """)
    
    # Add a clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
