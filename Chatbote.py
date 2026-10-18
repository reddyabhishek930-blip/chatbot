import random
import sys
import tkinter as tk
from tkinter import scrolledtext

# ---------------------------------------------------------
# 1. Global User State & Predefined Dictionary of Responses
# ---------------------------------------------------------
USER_NAME = "Abhi"  # Default user name
RESPONSES = {
    "greetings": {
        "keywords": ["hello", "hi", "hey", "greetings", "good morning", "good evening"],
        "answers": [
            "Hello! How can I help you today?",
            "Hi there! What would you like to chat about?",
            "Hey! Hope you are having a great day."
        ]
    },
    "how_are_you": {
        "keywords": ["how are you", "how's it going", "how do you do"],
        "answers": [
            "I'm just a Python program, but I'm running smoothly! How about you?",
            "Doing great and ready to assist you!"
        ]
    },
    "bot_name": {
        "keywords": ["your name", "who are you", "what is your name", "call you"],
        "answers": [
            "I am PyBot, a simple rule-based Python chatbot!",
            "You can call me PyBot."
        ]
    },
    "user_name": {
        "keywords": ["my name", "who am i", "what is my name", "do you know my name", "what's my name"],
        "answers": [
            "Your name is {USER_NAME}! You are the developer of this Python project.",
            "I know you! Your name is {USER_NAME}."
        ]
    },
    "help": {
        "keywords": ["help", "what can you do", "options", "commands"],
        "answers": [
            "I can answer questions! Try asking 'what is my name', 'what is GUI', 'tell me about python', 'what is python used for', or type 'exit' to quit."
        ]
    },
    "gui": {
        "keywords": ["gui", "what is gui", "graphical user interface", "tkinter gui", "ui"],
        "answers": [
            "GUI stands for Graphical User Interface! It allows users to interact with software using visual elements like windows, buttons, text fields, and icons instead of plain text commands.",
            "In Python, Tkinter is the standard built-in GUI library used to build window applications—just like the PyBot window you are using right now!",
            "Fun Fact: Graphical User Interfaces (GUIs) were popularized by Xerox PARC and Apple in the 1980s, making computers easy to use for everyone!"
        ]
    },
    "python": {
        "keywords": ["python", "code", "programming", "language", "why python", "guido", "features", "uses"],
        "answers": [
            "Python is a high-level, interpreted programming language famous for its clean, readable syntax.",
            "Python is widely used in Artificial Intelligence (AI), Machine Learning, Data Science, Web Development, Automation, and GUI apps.",
            "Fun Fact: Python was created by Guido van Rossum in 1991 and named after the comedy show 'Monty Python's Flying Circus'!",
            "Python supports multiple programming styles: Object-Oriented, Functional, and Procedural programming.",
            "Python has an awesome ecosystem with libraries like NumPy, Pandas, Django, Flask, PyTorch, and Tkinter!"
        ]
    },
    "farewell": {
        "keywords": ["bye", "exit", "quit", "goodbye", "see you"],
        "answers": [
            "Goodbye! Have a wonderful day ahead!",
            "Bye! Feel free to chat anytime.",
            "See you later!"
        ]
    }
}

# ---------------------------------------------------------
# 2. Response Matching Logic (String Methods & Loops)
# ---------------------------------------------------------
def get_bot_response(user_input: str):
    """
    Normalizes input using string methods (.strip(), .lower()),
    searches keywords in dictionary, supports dynamic user name,
    and returns (response_text, is_exit_flag).
    """
    global USER_NAME
    cleaned_input = user_input.strip().lower()

    if not cleaned_input:
        return "Please type a message!", False

    # Check for exit commands
    exit_keywords = ["exit", "quit", "bye", "goodbye"]
    if cleaned_input in exit_keywords:
        farewell_msg = random.choice(RESPONSES["farewell"]["answers"])
        return farewell_msg, True

    # Check if user is setting a new name (e.g., "my name is Alex" or "call me Sam")
    if cleaned_input.startswith("my name is "):
        new_name = user_input.strip()[11:].strip().title()
        if new_name:
            USER_NAME = new_name
            return f"Nice to meet you, {USER_NAME}! I will remember your name.", False
    elif cleaned_input.startswith("call me "):
        new_name = user_input.strip()[8:].strip().title()
        if new_name:
            USER_NAME = new_name
            return f"Got it! I will call you {USER_NAME}.", False

    # Check "what is my name" or "who am i"
    user_name_keywords = ["my name", "who am i", "what is my name", "do you know my name", "what's my name"]
    if any(k in cleaned_input for k in user_name_keywords):
        answers = RESPONSES["user_name"]["answers"]
        chosen_answer = random.choice(answers).format(USER_NAME=USER_NAME)
        return chosen_answer, False

    # Search keywords in responses dictionary
    for category, data in RESPONSES.items():
        if category == "user_name":
            continue
        for keyword in data["keywords"]:
            if keyword in cleaned_input:
                return random.choice(data["answers"]), False

    # Default response if no keyword matched
    fallback_answers = [
        f"I'm not sure I understand that, {USER_NAME}. Type 'help' to see what I know!",
        "Sorry, I don't have an answer for that yet. Type 'help' for options.",
        "Hmm, I haven't learned that phrase yet! Try asking about Python or your name."
    ]
    return random.choice(fallback_answers), False


# ---------------------------------------------------------
# 3. File Handling: Save Chat Log
# ---------------------------------------------------------
def save_chat_log(history_list, filename="chat_history.txt"):
    """Saves conversation history to a local text file using file I/O."""
    if not history_list:
        return
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write("\n--- Chat Session ---\n")
            for line in history_list:
                f.write(line + "\n")
    except Exception as e:
        print(f"Error saving chat history: {e}")

# ---------------------------------------------------------
# 4. GUI Application (Tkinter Interface)
# ---------------------------------------------------------
class ChatbotGUI:
    """Tkinter Graphical User Interface for the Chatbot."""
    def __init__(self, root):
        self.root = root
        self.root.title("PyBot - Python Rule-Based Chatbot")
        self.root.geometry("460x560")
        self.root.configure(bg="#1e1e2e")

        self.chat_history = []

        # Header Title Frame
        header_frame = tk.Frame(root, bg="#313244", pady=10)
        header_frame.pack(fill=tk.X)

        header_label = tk.Label(
            header_frame, text="🤖 PyBot Assistant", font=("Segoe UI", 14, "bold"),
            bg="#313244", fg="#cdd6f4"
        )
        header_label.pack()

        subtitle_label = tk.Label(
            header_frame, text="Rule-Based Python Chatbot", font=("Segoe UI", 9),
            bg="#313244", fg="#a6adc8"
        )
        subtitle_label.pack()

        # Chat Display Window (ScrolledText)
        self.chat_display = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, state="disabled", font=("Segoe UI", 10),
            bg="#181825", fg="#cdd6f4", insertbackground="white", relief=tk.FLAT
        )
        self.chat_display.pack(padx=12, pady=12, fill=tk.BOTH, expand=True)

        # Bottom Input Area Frame
        input_frame = tk.Frame(root, bg="#1e1e2e")
        input_frame.pack(padx=12, pady=(0, 12), fill=tk.X)

        # Entry Widget for User Input
        self.entry_field = tk.Entry(
            input_frame, font=("Segoe UI", 11), bg="#313244", fg="#cdd6f4",
            insertbackground="white", relief=tk.FLAT
        )
        self.entry_field.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=7, padx=(0, 8))
        self.entry_field.bind("<Return>", self.send_message)
        self.entry_field.focus_set()

        # Send Button
        send_button = tk.Button(
            input_frame, text="Send", font=("Segoe UI", 10, "bold"),
            bg="#89b4fa", fg="#11111b", relief=tk.FLAT, cursor="hand2",
            command=self.send_message, padx=18, pady=5
        )
        send_button.pack(side=tk.RIGHT)

        # Initial Greeting
        self.display_message("PyBot", "Hello! I am PyBot, your Python rule-based assistant. Type 'help' to see what I can do!", "#a6e3a1")

    def display_message(self, sender: str, text: str, color: str):
        """Displays a styled message in the chat window."""
        self.chat_display.config(state="normal")
        tag_name = sender + str(len(self.chat_history))
        self.chat_display.insert(tk.END, f"{sender}: {text}\n\n", tag_name)
        self.chat_display.tag_config(tag_name, foreground=color)
        self.chat_display.config(state="disabled")
        self.chat_display.yview(tk.END)

    def send_message(self, event=None):
        """Handles sending user message and retrieving bot response."""
        user_text = self.entry_field.get().strip()
        if not user_text:
            return

        self.entry_field.delete(0, tk.END)

        # Display User Message
        self.display_message("You", user_text, "#89b4fa")
        self.chat_history.append(f"You: {user_text}")

        # Get Bot Response
        bot_reply, is_exit = get_bot_response(user_text)
        self.display_message("PyBot", bot_reply, "#a6e3a1")
        self.chat_history.append(f"PyBot: {bot_reply}")

        # Exit Handling
        if is_exit:
            save_chat_log(self.chat_history)
            self.entry_field.config(state="disabled")
            self.root.after(1500, self.root.destroy)

def run_cli_mode():
    """Runs the chatbot in command-line (CLI) mode."""
    print("=" * 50)
    print("       [PyBot] Rule-Based Python Chatbot")
    print("=" * 50)
    print("Type 'help' to see options, or 'exit' to quit.\n")
    
    history = []
    greeting = "Hello! I am PyBot, your Python rule-based assistant. Type 'help' to see what I can do!"
    print(f"PyBot: {greeting}")
    history.append(f"PyBot: {greeting}")
    
    while True:
        try:
            user_input = input("\nYou: ")
        except (KeyboardInterrupt, EOFError):
            print("\nPyBot: Goodbye! Have a wonderful day ahead!")
            break
        
        history.append(f"You: {user_input}")
        response, is_exit = get_bot_response(user_input)
        print(f"PyBot: {response}")
        history.append(f"PyBot: {response}")
        
        if is_exit:
            save_chat_log(history)
            break

# ---------------------------------------------------------
# 5. Program Entry Point (Launches GUI or CLI)
# ---------------------------------------------------------
if __name__ == "__main__":
    if "--cli" in sys.argv:
        run_cli_mode()
    else:
        try:
            root = tk.Tk()
            app = ChatbotGUI(root)
            root.mainloop()
        except Exception as e:
            print(f"GUI launch failed ({e}), falling back to CLI mode...")
            run_cli_mode()

