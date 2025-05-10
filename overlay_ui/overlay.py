### File: overlay_ui/overlay.py

import tkinter as tk
from tkinter import scrolledtext, messagebox
from llm_engine.api_handler import handle_prompt

class OverlayApp:
    def __init__(self, directory):
        self.directory = directory
        self.root = tk.Tk()
        self.root.title("CodeFixer Overlay")
        self.root.attributes('-topmost', True)
        self.root.geometry("400x200+1000+50")
        self.root.configure(bg='#333')

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(padx=10, pady=10)

        self.send_button = tk.Button(self.root, text="Send to LLM", command=self.send_prompt)
        self.send_button.pack(pady=5)

        self.output_box = scrolledtext.ScrolledText(self.root, height=6, width=48)
        self.output_box.pack(padx=10, pady=10)

    def send_prompt(self):
        prompt = self.entry.get()
        if not prompt.strip():
            return

        result = handle_prompt(prompt, self.directory)
        self.output_box.delete(1.0, tk.END)
        self.output_box.insert(tk.END, result)

        if messagebox.askyesno("Apply Fix?", "Apply the suggested changes?"):
            from file_manager.file_writer import apply_changes
            apply_changes(result)

    def run(self):
        self.root.mainloop()

