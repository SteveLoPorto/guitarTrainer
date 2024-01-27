import tkinter as tk
import customtkinter

import game_screen
import menu_screen
import pause_screen
import results_screen


#control the flow between the different screens
class MainApplication(customtkinter.CTk):
    #define the constructor
    def __init__(self):
        #initalizes self to be a root/window 
        super().__init__()
        self.title("Note Recognition App")
        self.geometry('800x600')
        self.resizable()

        #instantiate every screen
        self.menu_screen = menu_screen.MenuScreen(self)
        self.game_screen = game_screen.gameScreen(self)
        self.results_screen = results_screen.resultsScreen(self)

        #run the main loop


    #Functions that will load and switch screens
    def showMenuScreen(self):
        pass
        










        
        

        

    



        



        

def main():
    app = MainApplication()
    app.mainloop()

if __name__ == '__main__':
    main()