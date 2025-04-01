# Gemini API Chatbot Example Project

This project demonstrates how to build chat applications using the Google Gemini API. It includes both a command-line chat interface and a web-based UI with Streamlit.

## Setup Instructions

### 1. Prerequisites

*   Python 3.x installed on your system.

### 2. Create a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies. Navigate to the project directory in your terminal and run:

```bash
python3 -m venv venv
```

Activate the virtual environment:

*   **macOS / Linux:**
    ```bash
    source venv/bin/activate
    ```
*   **Windows:**
    ```bash
    .\venv\Scripts\activate
    ```

You should see `(venv)` at the beginning of your terminal prompt.

### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

The requirements.txt file includes:
- google-generativeai: Google's official Python SDK for Gemini API
- python-dotenv: For loading environment variables
- streamlit: For the web interface
- Other supporting libraries (requests, pydantic)

### 4. Configure Environment Variables

This project uses an API key for the Google Generative AI service.

1.  Create the `.env` file if it doesn't exist:
    ```bash
    touch .env
    ```
2.  Add your API key to the `.env` file like this:

    ```env
    YOUR_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
    ```

    Replace `"YOUR_ACTUAL_API_KEY_HERE"` with your real API key. **Important:** Do not commit your `.env` file (or your API key directly) to version control. Add `.env` to your `.gitignore` file.

## Running the Applications

This project provides two different ways to interact with the Gemini AI:

### Command Line Interface (CLI)

The CLI version provides a simple terminal-based chat interface:

```bash
python app.py
```

- Type your messages directly in the terminal
- The conversation history is maintained throughout the session
- Type 'quit' or 'exit' to end the chat

### Web Interface (Streamlit)

The Streamlit app provides a more user-friendly web interface:

```bash
streamlit run streamlit_app.py
```

Features:
- Clean chat UI with user/assistant message bubbles
- Conversation history persists between interactions
- Clear chat button to start a new conversation
- Instructions sidebar with usage guidance

## Project Components

- `app.py`: Command-line chat interface
- `streamlit_app.py`: Web-based chat interface
- `requirements.txt`: Project dependencies
- `.env`: Configuration for API keys (not included in repo)

## Troubleshooting

If you encounter any issues:

1. Make sure your API key is properly set in the `.env` file
2. Ensure all dependencies are installed with `pip install -r requirements.txt`
3. Check that you're using the correct model name (this project uses "gemini-2.5-pro-exp-03-25")
4. If the Streamlit interface fails, try the CLI version first to verify API connectivity
