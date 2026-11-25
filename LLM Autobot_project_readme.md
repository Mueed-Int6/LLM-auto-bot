# Llama Conversational Assistant (`llama-gradio-chat`)

An interactive web-based conversational AI assistant built with **Python**, **Gradio**, and the **Together AI API**. It supports multi-turn conversation history and streaming large language model responses through a clean chat interface.

---

## Features

- **Interactive Web UI:** Built using Gradio Blocks (`gr.Blocks`) and `gr.Chatbot`.
- **Multi-Turn Conversation Context:** Maintains prior user and assistant messages throughout the session.
- **Streaming LLM Responses:** Streams tokens from Together AI's chat completions API for responsive replies.
- **Secure API Configuration:** Reads the API key from the `TOGETHER_API_KEY` environment variable rather than hardcoding credentials.

---

## Tech Stack

- **Language:** Python 3.9+
- **Frontend UI:** [Gradio](https://www.gradio.app/)
- **LLM Provider SDK:** [Together Python SDK](https://docs.together.ai/)

---

## Project Structure

```text
llama-gradio-chat/
├── chatbot.py          # Main Gradio chatbot application
├── requirements.txt    # Python dependencies
├── .gitignore          # Files and secrets excluded from Git
└── README.md           # Project documentation
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/llama-gradio-chat.git
cd llama-gradio-chat
```

### 2. Install Dependencies

```bash
pip install gradio together
```

*(Or create a `requirements.txt` containing `gradio` and `together` and run `pip install -r requirements.txt`.)*

### 3. Set Your Together AI API Key

Generate an API key from your [Together AI Dashboard](https://api.together.ai/settings/api-keys) and set it as an environment variable:

**Linux / macOS / Google Colab:**
```bash
export TOGETHER_API_KEY="your_together_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set TOGETHER_API_KEY=your_together_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:TOGETHER_API_KEY="your_together_api_key_here"
```

### 4. Run the Application

```bash
python chatbot.py
```

Open the local URL printed in your terminal (typically `http://127.0.0.1:7860`) in your browser to start chatting.

---

## Security Note

Never commit your `TOGETHER_API_KEY` or `.env` files to GitHub. Add `.env` to your `.gitignore` file before pushing changes.

---

## License

This project is open-source and available under the [MIT License](LICENSE).