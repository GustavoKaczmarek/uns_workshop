# main.py

import tkinter as tk
from tkinter import scrolledtext
from mqtt_client import start_mqtt_client
from openai_client import generate_response

# Start the MQTT client to subscribe and cache data
data_cache = start_mqtt_client()


# Create the Chatbot GUI using tkinter
def run_chatbot_gui():
    # Initialize the tkinter window
    root = tk.Tk()
    root.title("Operations Analysis")
    root.geometry("700x700")  # Larger window for more text visibility

    # Set font style and size for readability
    font_settings = ("Arial", 16)

    # Add a scrolled text area to display chatbot responses
    chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=30, width=80, font=font_settings)
    chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Entry box for user questions
    question_entry = tk.Entry(root, width=70, font=font_settings)
    question_entry.pack(padx=10, pady=10)

    def ask_question():
        # Get the question from the entry widget
        question = question_entry.get()
        question_entry.delete(0, tk.END)

        # Fetch the latest data from the MQTT cache
        latest_data = data_cache.get_latest_data()

        # Get a response from OpenAI
        response = generate_response(question, latest_data)

        # Display question and response in chat display
        chat_display.insert(tk.END, f"You: {question}\n", "user_text")
        chat_display.insert(tk.END, f"AI Assistant: {response}\n\n", "bot_text")

        # Scroll to the end of the text display to show the latest messages
        chat_display.see(tk.END)

    # Button to send the question
    send_button = tk.Button(root, text="Ask", command=ask_question, font=font_settings)
    send_button.pack(pady=5)

    # Bind Enter key to ask question function
    root.bind('<Return>', lambda event: ask_question())

    # Start the GUI loop
    root.mainloop()


if __name__ == "__main__":
    print("MQTT OpenAI Chatbot started. Type your question in the popup window, or close it to quit.")
    run_chatbot_gui()
