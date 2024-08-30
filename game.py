""" game.py contains the logic for the game. It contains a Game class which can be used to create a new game.
"""
# Import required modules

"""pygame is used to carry out game-related things such as creating and managing the window, setting up game controls, 
   and detecting any user event that happens while playing.
"""
import pygame
pygame.init() # Init pygame to access its content
from board import * # The board.py script contains a Board method which represent the graphical board for the game

win_width = 800 # The width of a game window
win_height = 600 # The height of a game window

class Game:
    def __init__(self):
        "The Game class represents an instance of the game which is independent of the others."
        self.window = pygame.display.set_mode((win_width, win_height)) # Create a game window with the win_width, win_height dimensions
        pygame.display.set_caption("Chess !") # Set a caption for the game window

        self.grid = [[0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0]] # The grid which represent the game board for the program. Here, 0 means a cell is empty. Eeach list in the grid represent a row.
        

        self.board = Board(self.window, self.grid) # Create a new graphical game board
        self.board.draw_squares() # Draw the squares of the board

    def run(self): 
        "Run the game loop."
        running = True # This variable is an indicator for the current running state of the game. When True, then the game continues running, 
                       # otherwise it stops.

        while running: # While the game is still running
            for event in pygame.event.get(): # Capture any event that happens during the game
                if event.type == pygame.QUIT: # If the player wants to stop playing
                    running = False       


            pygame.display.flip() # Update the display                    





         
