[README.md](https://github.com/user-attachments/files/33628542/README.md)
# 🤖 Rule-Based Python Chatbot (PyBot)

A lightweight, rule-based Python Chatbot built with a **Tkinter Graphical User Interface (GUI)** adhering strictly to beginner Python fundamentals.

---

## 📌 Project Overview
- **File Structure**: Single `main.py` script under `chatbot/`.
- **GUI Framework**: Python Built-in `tkinter`.
- **Rules Engine**: Predefined Python Dictionaries and Keyword lists (No AI APIs or external dependencies required).
- **File Handling**: Automatically logs conversation history into `chat_history.txt`.

---

## 📁 File Structure
```text
chatbot/
├── main.py            # Complete Chatbot source code (GUI + Logic)
├── chat_history.txt   # Automatically created when chat sessions are saved
└── README.md          # Project documentation
```

---

## 🛠️ Requirements & Installation
**No external extensions or pip packages are required!**  
All required modules (`tkinter`, `random`) are part of Python's standard library.

### How to Run:
Open Command Prompt or Terminal in this directory and execute:

```cmd
# Run GUI Mode (Default)
python main.py

# Run CLI / Terminal Mode
python main.py --cli
```

---

## 🧠 Technical Features & Python Concepts Used
1. **Tkinter GUI (`ChatbotGUI` class)**: Rendered window, scrolled text chat area, input entry, and send button.
2. **Dictionary Rule Database (`RESPONSES`)**: Maps categories to keywords and array of response strings.
3. **Input Normalization (`.strip().lower()`)**: Ensures case-insensitive keyword matching.
4. **Keyword Loop Matching**: Scans user queries against keyword rules.
5. **File I/O (`save_chat_log`)**: Appends saved session transcripts to `chat_history.txt`.
