import tkinter as tk
from tkinter import filedialog

def get_image_path():
    """Opens a file picker and returns the selected file path"""
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="Select image of Tic Tac Toe board",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )