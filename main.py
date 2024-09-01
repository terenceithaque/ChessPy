"""main.py is the starting point for the game.
   It starts a first game, and when finished, it enters a loop which allows the player to play as many times as they want."""
import pygame # Import pygame to ensure all required functionalities are present
pygame.init() # Init pygame
from game import * # Import game.py, which is the script that handles the logic of the game
from tkinter import messagebox # We'll use the messagebox module from tkinter to display dialog boxes to the player



# Let's start and run a first game immediatly
game = Game()
game.run() 
pygame.quit() # Quit pygame


# After the first game has ended, enter a loop to allow the player to replay

while True:
    replay = messagebox.askyesno("Replay ?", "Do you want to replay ?") # Ask the player if he wants to play a new game
    if replay: # If the player answered 'yes'
        # Start a new game
        pygame.init()
        game = Game() 
        game.run()

    else: # If the player answered 'no'
        pygame.quit() # Quit pygame
        break # Break the loop and then completely stop the program    
        
    

    