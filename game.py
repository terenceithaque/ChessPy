""" game.py contains the logic for the game. It contains a Game class which can be used to create a new game.
"""
# Import required modules

"""pygame is used to carry out game-related things such as creating and managing the window, setting up game controls, 
   and detecting any user event that happens while playing.
"""
import pygame
pygame.init() # Init pygame to access its content

win_width = 800 # The width of a game window
win_height = 600 # The height of a game window

class Game:
    "The Game class represents an instance of the game which is independent of the others."
    def __init__(self):
        "This is the constructor of the Game class"
        self.window = pygame.display.set_mode((win_width, win_height)) # Create a game window with the win_width, win_height dimensions
        pygame.display.set_caption("Chess !") # Set a caption for the game window

    def run(self): 
        "Run the game loop."
        running = True # This variable is an indicator for the current running state of the game. When True, then the game continues running, 
                       # otherwise it stops.

        while running: # While the game is still running
            for event in pygame.event.get(): # Capture any event that happens during the game
                if event.type == pygame.QUIT: # If the player wants to stop playing
                    running = False # Stop the game now               





         
