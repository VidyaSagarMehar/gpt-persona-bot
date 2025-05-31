# 🤖 gpt-persona-bot

A lightweight, terminal-based chatbot powered by OpenAI's GPT model with persistent conversational context and structured JSON responses. Customize your AI's persona using a system prompt, and interact seamlessly from your command line.

---

## 🧠 Features

- ✅ Maintains full conversation history (user + assistant messages)
- ✅ Uses OpenAI's `gpt-4o-mini` model (configurable)
- ✅ Reads the system prompt from an external file for easy persona customization
- ✅ Parses structured JSON responses from the model
- ✅ Graceful fallback if the response is not valid JSON

---

## 📁 Project Structure

gpt-persona-bot/<br>
├── main.py # Entry point – chat loop logic <br>
├── prompt.py # System prompt stored here <br>
├── requirements.txt # Python dependencies <br>
└── README.md # You’re reading it! <br>


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gpt-persona-bot.git
cd gpt-persona-bot
```

### 2. Install Dependencies
 ```bash
pip install -r requirements.txt
```

### 3. Set Up Your API Key -     Create a .env file and setup the api key - refer .env.example

```bash
pip install -r requirements.txt
```

### 4. Run the Bot
 ```bash
python main.py
```