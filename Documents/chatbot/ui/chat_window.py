import tkinter as tk
from services.gemini_api import get_gemini_response

class ChatWindow:
    def __init__(self, root):
        self.root = root
        self.root.title = "Chatbot UI"
        
        self.text_area = tk.Text(root, wrap="word", height=40, width=80, state='disabled')
        self.text_area.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, width=80)
        self.entry.pack(side='left', padx=(10,0), pady=(0,10))
        self.entry.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(root, text="Verstuur", command=self.send_message, width=20)
        self.send_button.pack(side='left', padx=10, pady=(0,10))
        
    def send_message(self, event=None):
        user_message = self.entry.get().strip()
        if not user_message:
            return
        
        self.entry.delete(0, tk.END)
        self._append_text(f"Jij: {user_message}\n")
        bot_message = get_gemini_response(user_message)
        self._append_text(f"Billie: {bot_message}\n")
        
    def _append_text(self, text):
        self.text_area.configure(state='normal')
        self.text_area.insert(tk.END, text)
        self.text_area.configure(state='disabled')
        self.text_area.see(tk.END)
        