# Gemini API Chatbot Example Project

This project demonstrates a simple interaction with the Google Gemini API using the Python client library and potentially uses MCP features.

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
pip install -q -U google-genai python-dotenv "mcp[cli]"
```

*(Optional but recommended: Create a `requirements.txt` file containing the dependencies, then use `pip install -r requirements.txt`)*

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

### 5. Run the Application

With the virtual environment activated and the `.env` file configured, you can run the main script (assuming it's `app.py`):

```bash
python3 app.py
```

Or potentially run MCP commands if using `server.py`:

```bash
mcp serve server:mcp
```

The script will load the API key, connect to the Gemini API, send a prompt, and print the response.
