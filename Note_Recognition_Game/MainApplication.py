import tkinter as tk
import customtkinter

import game_screen
import menu_screen
import pause_screen
import results_screen
import copy


#control the flow between the different screens
class MainApplication(customtkinter.CTk):
    #define the constructor
    def __init__(self):
        #initalizes self to be a root/window 
        super().__init__()
        self.title("Note Recognition App")
        self.geometry('800x600')
        self.resizable(False, False)
        self.initalialize_screen()

    def initalialize_screen(self):
        #instantiate every screen
        self.current_screen = menu_screen.MenuScreen(self)
        self.current_screen.place(x=0, y=0)
    
    #run the main loop
    def switch_screens(self, event, destination_screen):
        if destination_screen == "GameScreen":
            screen = game_screen.GameScreen(self)
        if destination_screen == "MenuScreen":
            screen = menu_screen.MenuScreen(self)
        if destination_screen == "PauseScreen":
            screen = pause_screen.PauseScreen(self)
        if destination_screen == "ResultsScreen":
            screen = results_screen.ResultsScreen(self)
        self.current_screen.destroy()
        self.current_screen = screen
        self.current_screen.place(x=0, y=0)

    


        
def main():
    app = MainApplication()
    app.mainloop()

if __name__ == '__main__':
    main()