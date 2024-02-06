import tkinter as tk
import customtkinter
import button_classes

background_color = '#3c4250'
secondary_color = '#25282D'

class GameScreen(customtkinter.CTkFrame):

    #define the constructor
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        #Variables
        self.width = master.winfo_screenwidth()
        self.height = master.winfo_screenheight()
        self.fg_color = secondary_color
        self.name = "GameScreen"
        self.configure(width=self.width, height=self.height, fg_color=self.fg_color)

        #create the frame
        self.create_widgets()

    def create_widgets(self):

        #ionitalize thew note string variable
        self.note = tk.StringVar()
        self.string = tk.StringVar()
        self.octave = tk.StringVar()
        self.sharp = tk.StringVar()
        self.score = tk.StringVar()

        #this is the container for the note that should be played information
        self.note_frame = DisplayedNoteFrame(self)
        self.note_frame.place(x=275, y=200)

        #this is the container for the score
        self.score_frame = ScoreContainer(self)
        self.score_frame.place(x=20, y=20)

        #this is the container for the pause button
        self.pause_button = PauseButton(self, 50, secondary_color, background_color, secondary_color)
        self.pause_button.place(x=725, y=20)



    
class DisplayedNoteFrame(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.size = 240
        self.fg_color = secondary_color
        self.bg_color = background_color
        self.configure(width=self.size, height=self.size, fg_color=self.fg_color, bg_color=self.bg_color)
        self.create_widgets()

    def create_widgets(self):
        
        #this is the containter for the note that should be played information
        self.note_container = NoteContainer(self, self.size, secondary_color, background_color, secondary_color)
        self.note_container.place(x=0, y=0)


class NoteContainer(button_classes.CircularButton):

    def __init__(self, master, diameter, bg_color, circle_color, outline_color):
        super().__init__(master, diameter, bg_color, circle_color, outline_color)
        self.master = master

        #create widgets
        self.create_widgets()
    
    def create_widgets(self):
        #this is the label that will hold the note that should be played
        self.note_label = customtkinter.CTkLabel(self, text=self.master.master.note, font=("Microsoft Tai Le", 115, "bold"), fg_color=background_color, bg_color=background_color, justify="center")
        self.note_label.place(x=70, y=60)

        #this is the string label 
        self.string_label = customtkinter.CTkLabel(self, text=self.master.master.string, font=("Microsoft Tai Le", 40, "bold"), fg_color=background_color, bg_color=background_color)
        self.string_label.place(x=110, y=20)

        #this is the octave label
        self.octave_label = customtkinter.CTkLabel(self, text=self.master.master.octave, font=("Microsoft Tai Le", 35, "bold"), fg_color=background_color , bg_color=background_color)
        self.octave_label.place(x=175, y=130)

        #this is the sharp label
        self.sharp_label = customtkinter.CTkLabel(self, text=self.master.master.sharp, font=("Microsoft Tai Le", 35, "bold"), fg_color=background_color, bg_color=background_color)
        self.sharp_label.place(x=150, y=70)

class ScoreContainer(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.height = 65
        self.width = 155
        self.fg_color = background_color
        self.bg_color = secondary_color
        self.configure(width=self.width, height=self.height, fg_color=self.fg_color, bg_color=self.bg_color, corner_radius=20)
        self.create_widgets()

    def create_widgets(self):
        #this is the label that will hold the score
        self.score_label = customtkinter.CTkLabel(self, text=self.master.score, font=("Microsoft Tai Le", 30, "bold"), fg_color=background_color, bg_color=background_color, justify="center")
        self.score_label.place(x=37, y=15)

class PauseButton(button_classes.CircularButton):

    def __init__(self, master, diameter, bg_color, circle_color, outline_color):
        super().__init__(master, diameter, bg_color, circle_color, outline_color)
        self.master = master
        






