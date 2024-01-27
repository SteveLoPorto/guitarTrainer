import tkinter as tk
import customtkinter
import options_display

class MenuScreen(customtkinter.CTkFrame):
    """
    A class used to represent a Menu Screen in a tkinter application.
    """

    def __init__(self, master):
        """
        Initialize the MenuScreen with a master widget.
        
        Parameters:
        master (tkinter.Tk): The parent widget.
        """
        super().__init__(master)
        self.master = master
        #Variables
        self.width = master.winfo_screenwidth()
        self.height = master.winfo_screenheight()
        self.fg_color = "#25282D"
        self.x = 0
        self.y = 0

        #Initialize the MenuScreen
        self.configure(width=self.width, height=self.height, fg_color=self.fg_color)
        self.place(x=self.x, y=self.y) 
    
        #create the options display frame
        self.options_display = MenuScreenOptionsDisplay(self)



class MenuScreenOptionsDisplay(options_display.OptionsDisplay):
    """
    A class used to represent the Menu Screen Options Display in a tkinter application. This will be a child of the MenuScreen class. The trial frame, strings frame, difficulty frame, and audio source
    frame will will be children of this class.
    """

    def __init__(self, master):
        """
        Initialize the OptionsDisplay with a master widget.
        
        Parameters:
        master (tkinter.Tk): The parent widget.
        """
        #places the container frame
        super().__init__(master)
        #Object setup
        self.master = master
        self.drawLines()

        #create the frames
        self.trails_frame = TrialsFrame(self)
        self.strings_frame = StringsFrame(self)
        self.difficulty_frame = DifficultyFrame(self)
        self.audio_source_frame = AudioSourceFrame(self)



    def drawLines(self):
        """
        Draw the lines that will separate the different options.
        """
        #draw the verticle line
        canvas=tk.Canvas(self, width=4, height=424, bg="#FFFFFF", highlightthickness=0)
        canvas.place(x=263, y=0)

        #draw the horizontal line
        canvas=tk.Canvas(self, width=524, height=4, bg="#FFFFFF", highlightthickness=0)
        canvas.place(x=0, y=213)
    


class TrialsFrame(customtkinter.CTkFrame):
    """
    A class used to represent the Trial Frame in a tkinter application. This will be a child of the MenuScreenOptionsDisplay class.
    """

    def __init__(self, master):
        """
        Initialize the MenuScreen with a master widget.
        
        Parameters:
        master (tkinter.Tk): The parent widget.
        """
        super().__init__(master)
        self.master = master
        #Variables
        self.width = 254
        self.height = 202
        self.fg_color = "#3C4250"
        self.x = 8
        self.y = 10

        #Initialize the MenuScreen
        self.configure(width=self.width, height=self.height, fg_color=self.fg_color)
        self.place(x=self.x, y=self.y) 
        self.create_widgets()

    
    def check_length(self, event):
        """
        Validate function for the entry box 
        """
        # Add your validation logic here
        if (event == '1' and len(self.trials_entry.get()) < 3) or event == '0':
            return True
        else:
            return False
    
    def create_widgets(self):
        """
        Create the widgets that will be in the frame.
        """
        #create the label
        self.trials_label = customtkinter.CTkLabel(self, text="Trials", fg_color="transparent",  font=("Microsoft Tai Le", 39, "bold"), text_color="white")
        self.trials_label.place(x=0, y=0)

        #create a frame for the dotted line and entry
        self.trials_entry_box_frame = customtkinter.CTkFrame(self, width=100, height=100, fg_color="#3C4250")
        self.trials_entry_box_frame.place(x=50, y=50)

        #create text entry
        self.trials_entry = tk.Entry(self.trials_entry_box_frame, borderwidth=0, highlightthickness=0, font=("Microsoft Tai Le", 40, "bold"), background="#3C4250", foreground="white", width=3)
        self.trials_entry.place(x=0, y=0)
        reg = self.trials_entry_box_frame.register(self.check_length)
        self.trials_entry.config(validate="key", validatecommand=(reg, "%d"))

        #creted thew dotted line
        canvas = tk.Canvas(self.trials_entry_box_frame, width=75, height=50)
        canvas.place(x=0, y=96)

        # Create a dotted line
        canvas.create_line(10, 10, 100, 10, dash=(1, 1), fill="red")
        
    
 


    
        
class StringsFrame(customtkinter.CTkFrame):
    """
    A class used to represent the Strings Frame in a tkinter application. This will be a child of the MenuScreenOptionsDisplay class.
    """

    def __init__(self, master):
        """
        Initialize the MenuScreen with a master widget.
        
        Parameters:
        master (tkinter.Tk): The parent widget.
        """
        super().__init__(master)
        self.master = master
        #Variables
        self.width = 250
        self.height = 202
        self.fg_color = "#3C4250"
        self.x = 268
        self.y = 10
 
        #Initialize the MenuScreen
        self.configure(width=self.width, height=self.height, fg_color=self.fg_color)
        self.place(x=self.x, y=self.y) 

    
        
class DifficultyFrame(customtkinter.CTkFrame):
    """
    A class used to represent the Difficulty Frame in a tkinter application. This will be a child of the MenuScreenOptionsDisplay class.
    """

    def __init__(self, master):
        """
        Initialize the MenuScreen with a master widget.
        
        Parameters:
        master (tkinter.Tk): The parent widget.
        """
        super().__init__(master)
        self.master = master
        #Variables
        self.width = 252
        self.height = 198
        self.fg_color = "#3C4250"
        self.x = 10
        self.y = 218

        #Initialize the MenuScreen
        self.configure(width=self.width, height=self.height, fg_color=self.fg_color)
        self.place(x=self.x, y=self.y) 
    
        
class AudioSourceFrame(customtkinter.CTkFrame):
    """
    A class used to represent the Audio Source Frame in a tkinter application. This will be a child of the MenuScreenOptionsDisplay class.
    """

    def __init__(self, master):
        """
        Initialize the MenuScreen with a master widget.
        
        Parameters:
        master (tkinter.Tk): The parent widget.
        """
        super().__init__(master)
        self.master = master
        #Variables
        self.width = 252
        self.height = 198
        self.fg_color = "#3C4250"
        self.x = 268
        self.y = 218

        #Initialize the MenuScreen
        self.configure(width=self.width, height=self.height, fg_color=self.fg_color)
        self.place(x=self.x, y=self.y) 
    
        



