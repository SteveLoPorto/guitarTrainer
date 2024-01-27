import tkinter as tk
from tkinter import ttk

class PauseScreen(ttk.Frame):

    #define the constructor
    def __init__(self, master):
        super().__init__(master)

    #set the width of the frame
    def add_width(self, widthValue):
        self.configure(width=widthValue)
    #set the height of the frame
    def add_height(self, heightValue):  
        self.configure(height=heightValue)
    #set the background color of the frame
    def add_background(self, colorValue):
        self.configure(background=colorValue)
    

        

        


        #create the frame


        