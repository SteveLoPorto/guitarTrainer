import tkinter as tk
import customtkinter

class OptionsDisplay(customtkinter.CTkFrame):
    """
    A class that is the container for the interactive options menu
    """
    def __init__(self, master):
        super().__init__(master)
        """
        Initialize the OptionDisplay with a master widget.
        
        Parameters:
        master (tkinter.Frame): The parent widget.
        """
        #Variables
        self.width = 525
        self.height = 425
        self.fg_color = "#3C4250"
        self.x = 136
        self.y = 87


        #Initialize the OptionDisplay
        self.configure(width=self.width, height=self.height, fg_color=self.fg_color, corner_radius=28)
        
        self.place(x=self.x, y=self.y)

