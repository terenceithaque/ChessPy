""" game.py contains the logic for the game. It contains a Game class which can be used to create a new game.
"""
# Import required modules

"""pygame is used to carry out game-related things such as creating and managing the window, setting up game controls, 
   and detecting any user event that happens while playing.
"""
import pygame
pygame.init() # Init pygame to access its content
from board import * # The board.py script contains a Board class which represent the graphical board for the game
from piece import * # The piece.py script contains a GamePiece class which allows to add a piece (pawn, king,...) to the game

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
        

    def run(self): 
        "Run the game loop."
        running = True # This variable is an indicator for the current running state of the game. When True, then the game continues running, 
                       # otherwise it stops.


        piece = GamePiece(self.window, board=self.board, name="king", color=(255,255,255), image_path="assets/images/king.jpg")          
        piece.set_position(1,7)   

        player_move = pygame.USEREVENT + 1 # Event which allow the player to move a piece
        pygame.time.set_timer(player_move, 100) # The player_move event will occur every 100 milliseconds  

        while running: # While the game is still running
            
            self.window.fill((255, 255, 255)) # Fill the window
            
            self.board.draw_squares() # Draw the squares of the board


            keys = pygame.key.get_pressed() # Get the keys pressed by the player
            for event in pygame.event.get(): # Capture any event that happens during the game
                if event.type == pygame.QUIT: # If the player wants to stop playing
                    running = False  


                if keys[pygame.K_UP] or keys[pygame.K_z] and event.type == player_move: # If the player presses the up arrow key or the Z key
                    piece.move_to(piece.original_grid_x, piece.original_grid_y -1) # Move the piece forward

                if keys[pygame.K_DOWN] or keys[pygame.K_s] and event.type == player_move: # If the player presses the down arrow key or the S key
                    piece.move_to(piece.original_grid_x, piece.original_grid_y + 1) # Move the piece backward

                if keys[pygame.K_LEFT] or keys[pygame.K_q] and event.type == player_move: # If the player presses the left arrow key or the Q key
                    piece.move_to(piece.original_grid_x -1, piece.original_grid_y)  # Move the piece to the left

                if keys[pygame.K_RIGHT] or keys[pygame.K_d] and event.type == player_move: # If the player presses the right arrow key or the D key
                    piece.move_to(piece.original_grid_x +1, piece.original_grid_y) # Move the piece to the right              

            piece.draw()

            pygame.display.flip() # Update the display                    





         
