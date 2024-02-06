import tkinter as tk
import customtkinter
import options_display
import button_classes
import game_screen
from PIL import Image

#This is the 
background_color = '#3c4250'
secondary_color = '#25282D'

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
        self.fg_color = secondary_color
        self.name = "MenuScreen"
    
        #Initialize the MenuScreen
        self.configure(width=self.width, height=self.height, fg_color=self.fg_color)
        self.create_widgets()

    def create_widgets(self):

        #create the options display frame
        self.options_display = MenuScreenOptionsDisplay(self)

        #this is the trials frame entry
        self.trails_frame_entry = self.options_display.trails_frame.trials_entry_box_frame.entry

        #this is the strings frame entry
        self.strings_frame_entry = self.options_display.strings_frame.stringButtons
        
        #this is the difficulty frame entry
        self.difficulty_frame_entry = self.options_display.difficulty_frame.difficulty_entry_box_frame.entry
        #this is the go button, destination screen
        switch_to_game_screen = self.master.switch_screens
        
        #create the go button
        self.go_button = GoButton(self, switch_to_game_screen = switch_to_game_screen, diameter=60, bg_color=secondary_color, circle_color="#d9d9d9", outline_color=secondary_color, font=("Microsoft Tai Le", 39, "bold"), text="Go", text_color="#2f6405")
        self.go_button.place(x=372, y=520) 

class GoButton(button_classes.CircularButton):
    """
    class that is the go button that lives in the menu frame and its binding function
    """
    def __init__(self, master, switch_to_game_screen, diameter, bg_color, circle_color, outline_color, font, text="", text_color=""):
        """
        This function will 
        """
        super().__init__(master, diameter, bg_color, circle_color, outline_color, font, text, text_color)
        """
        This function initializes the go button
        parameters:
        master (tkinter.Tk): The parent widget.
        diameter (int): The diameter of the button
        bg_color (string): The background color of the canvas
        circle_color (string): The color of the circle
        outline_color (string): The color of the outline
        font (string): The font of the text
        text (string): The text of the button
        text_color (string): The color of the text
        """
        self.master = master
        self.bind("<Button-1>", lambda event, screen="GameScreen": switch_to_game_screen(event, screen))



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
        self.trails_frame.place(x=8, y=10)
        self.strings_frame = StringsFrame(self)
        self.strings_frame.place(x = 268, y = 10)
        self.difficulty_frame = DifficultyFrame(self)
        self.difficulty_frame.place(x=10, y=218)
        self.audio_source_frame = AudioSourceFrame(self)
        self.audio_source_frame.place(x=268, y=218)



    def drawLines(self):
        """
        Draw the lines that will separate the trials, 
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
        self.fg_color = background_color

        #Initialize the MenuScreen
        self.configure(width=self.width, height=self.height, fg_color=self.fg_color)
        self.create_widgets()

    def create_widgets(self):
        """
        Create the widgets that will be in the frame.
        """
        #create the label
        self.trials_label = customtkinter.CTkLabel(self, text="Trials", fg_color="transparent",  font=("Microsoft Tai Le", 39, "bold"), text_color="white")
        self.trials_label.place(x=0, y=0)

        #Entry box
        self.trials_entry_box_frame = DottedLineEntryBox(self)
        self.trials_entry_box_frame.place(x=64,y=60)

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
        self.fg_color = background_color

        #Initialize the MenuScreen
        self.configure(width=self.width, height=self.height, fg_color=self.fg_color)
        self.create_widgets()
    

    def create_widgets(self):
        """
        Create the widgets that will be in the frame.
        """
        #create the label
        self.difficulty_label = customtkinter.CTkLabel(self, text="Difficulty", fg_color="transparent",  font=("Microsoft Tai Le", 39, "bold"), text_color="white")
        self.difficulty_label.place(x=0, y=0)

        #Entry box
        self.difficulty_entry_box_frame = DottedLineEntryBox(self)
        self.difficulty_entry_box_frame.place(x=64, y=60)
        
# This class is used as the trials frame and difficulty frame entry box
class DottedLineEntryBox(customtkinter.CTkFrame):
    """
    A class used to represent a dotted lined entry box in a tkinter application. Does not place the Frame

    customtkinter.CTkFrame
    Parameters:
    master (customtkinter.CTkFrame): the parent widget the trials frame
    """
    def __init__(self, master): 
        """
        Initalizing the frame.
        """
        super().__init__(master)
        self.master = master
        self.configure(width=92, height=75, fg_color=background_color)
        self.create_widgets()
        


    def check_length(self, input_type, new_char):
        """
        Validate function for the entry box 
        
        Parameters:
        input_type (int) : type of opperation attempted on the entry box, 1 for insert, 0 for deleter, -1 for other
        new_char (string): the character that is being instered
        """
        #Denies entry if the first value is as 0
        if(input_type == '1' and len(self.entry.get()) == 0 and new_char == '0'):
            return False
        # Allows entry if the value is less that 3 and a digit.
        if (input_type == '1' and len(self.entry.get()) < 3 and new_char.isdigit()) or input_type == '0':
            return True
        else:
            return False


    def create_widgets(self):
        """
        This function creates and displays the widgets
        """
        #create text entry 3C4250 
        self.entry = tk.Entry(self, borderwidth=0, highlightthickness=0, font=("Microsoft Tai Le", 40, "bold"), background=background_color, foreground="white", width=3, justify='center')
        self.entry.place(x=0, y=0)

        #set validation requirements
        reg = self.register(self.check_length)
        self.entry.config(validate="key", validatecommand=(reg, "%d", "%S"))


        #creted thew dotted line
        canvas = tk.Canvas(self, width=100, height=4, background=background_color, highlightthickness=0)
        canvas.place(x=0, y=70)

        # Create a dotted line
        canvas.create_line(0, 4, 100, 4, dash=(1, 1), fill="white", width=5)
        

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
        self.fg_color = background_color

 
        #Initialize the MenuScreen
        self.configure(width=self.width, height=self.height, fg_color=self.fg_color)
        self.create_widgets()

    #This function will place
    def place_string_buttons(self, starting_x, starting_y, x_step, y_step):
        """
        This function will place the button in a cascading fashion

        Parameters:
        starting_x (int): This controls where the first button x position
        starting_y (int): This controls where the first button y position
        x_step (int): This controls the x translation between each button num
        y_step (int): This controls the y translation between each button num
        """
        #String Buttons, holds the string buttons awith button "6" starting at index 0
        self.stringButtons = [0 for x in range(0, 6)]
        string_names = ['e', 'B', 'G', 'D', 'A', 'E']

        for iter in range(0, 6):
            self.stringButtons[5-iter] = StringButton(self, string_names[iter])
            self.stringButtons[5-iter].place(x= starting_x + (x_step * (iter)), y= starting_y + (y_step * (iter)))

    def create_widgets(self):
        """
        Create the widgets that will be in the frame.
        """
        #String label
        self.strings_label = customtkinter.CTkLabel(self, text="Strings", fg_color="transparent",  font=("Microsoft Tai Le", 39, "bold"), text_color="white")
        self.strings_label.place(x=10, y=0)

    
        #Place the string buttons
        starting_x = 40
        starting_y = 50
        x_step = 25
        y_step = 20
        self.place_string_buttons(starting_x, starting_y, x_step, y_step)

class StringButton(customtkinter.CTkButton):
    """
    Creates the template for the string buttons
    """

    def on_click_then_exit(self, event):
        """
        This handles string button click, if clicked it sets the background color to blue and will set the clicked value to 1
        """
        if(self.clicked == 0):
            self.configure(fg_color="#558afa", hover_color=background_color)
            self.clicked = 1
        elif(self.clicked == 1):
            self.configure(fg_color="transparent", hover_color="#558afa")
            self.clicked = 0

    def __init__(self, master, buttonText):
        """
        This is a button initializer
        """
        super().__init__(master)
        self.master = master
        self.clicked = 0
        self.configure(text=buttonText, fg_color="transparent", font=("Microsoft Tai Le", 18, "bold"), width=0, height=0, border_spacing=0, border_width=0, hover_color="#558afa")

        self.set_commands()
    
    def set_commands(self):
        self.bind("<Enter><Button-1><Leave>", self.on_click_then_exit)   
        
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
        self.fg_color = background_color


        #Initialize the MenuScreen
        self.configure(width=self.width, height=self.height, fg_color=self.fg_color)
        self.create_widgets()

    def create_widgets(self):
        """
        Create the widgets that will be in the frame.
        """
        #create the label
        self.audio_source_label = customtkinter.CTkLabel(self, text="Audio Source", fg_color="transparent",  font=("Microsoft Tai Le", 37, "bold"), text_color="white")
        self.audio_source_label.place(x=10, y=0)

        #create the buttom
        self.audio_source_button = AudioSouceButton(self)
        self.audio_source_button.place(x=90, y=90)
        
class AudioSouceButton(customtkinter.CTkButton):
    """
    Audio Source button, will have controls to open a window when clicked
    """
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        #declaring the hovering photo
        image_path = "pics/audioSourceButtonHoveringImg.png"
        self.audioSourceButtonHoveringImage = customtkinter.CTkImage(light_image=Image.open(image_path), size=(54, 33))

        #declaring the photo default
        image_path = "pics/audioSourceButtonImg.png"
        self.audioSourceButtonImage = customtkinter.CTkImage(light_image=Image.open(image_path), size=(54, 33))

        #configuring
        self.configure(image=self.audioSourceButtonImage, height=33, width=54, text="", border_width = 0, border_spacing=0, fg_color="transparent", hover=False)

        #set the commands 
        self.set_commands()

    def on_enter(self, event):
        self.configure(image=self.audioSourceButtonHoveringImage)

    def on_leave(self, event):
        self.configure(image=self.audioSourceButtonImage)

    def set_commands(self):
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)


