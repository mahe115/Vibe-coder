### File: file_manager/directory_selector.py

import tkinter as tk
from tkinter import filedialog

def select_directory():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Select Project Directory")
