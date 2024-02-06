import tkinter as tk
import customtkinter


class CircularButton(tk.Canvas):
    """
    This is the class that will hold circular buttons
    """
    def __init__(self, master, diameter, bg_color, circle_color, outline_color, font="", text="", text_color=""):
        super().__init__(master, width=diameter, height=diameter, bg=bg_color, highlightthickness=0)
        self.master = master

        # Create a circular shape
        self.create_oval(0, 0, diameter, diameter, fill=circle_color, outline=outline_color)
        
        # Add text (optional) with custom text color
        if text:
            self.create_text(diameter // 2, diameter // 2, font=("Microsoft Tai Le", 15, "bold"), text=text, fill=text_color)