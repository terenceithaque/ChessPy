""" game.py contains the logic for the game. It contains a Game class which can be used to create a new game.
"""
# Import required modules

"""pygame is used to carry out game-related things such as creating and managing the window, setting up game controls, 
   and detecting any user event that happens while playing.
"""
import pygame
pygame.init() # Init pygame to access its content
from tkinter import messagebox # Import messagebox from tkinter 
from board import * # The board.py script contains a Board class which represent the graphical board for the game
from piece import * # The piece.py script contains a GamePiece class which allows to add a piece (pawn, king,...) to the game
import os

win_width = 800 # The width of a game window
win_height = 600 # The height of a game window


def ask_quit():
    "Ask the player if he wants to quit the game and returns a boolean"
    # Ask the player if he wants to quit
    quit = messagebox.askyesno("Do you really want to quit ?", "If you quit the game, all progress will be lost. Are you sure you want to do this ?")

    return quit # Return the player's answer as a boolean

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


    def spawn_player_pieces(self):
        "Spawn all the player's pieces"
        # Spawn the player's pawns
        self.player_pieces= [] # List of the player's pieces
        for x in range(8): # For each x number between 0 included and 7 excluded
            pawn = GamePiece(self.window, board=self.board, name="pawn", color=(255,255,255), image_path=os.path.abspath("assets/images/pawn.jpg")) # Create a new pawn
            pawn.set_position(grid_x=x, grid_y=6) # Set the position of the pawn to 0 (x coordinate) and 6 (y)
            self.player_pieces.append(pawn) # Add the pawn to the list


        # Spawn other pieces for the player
        for x in range(8): # For each x number between 0 included and 7 excluded
            if x == 0 or x == 7: # If x is equal to 0 or 7
                # Spawn a rook at this position (x, y=7)
                rook = GamePiece(window=self.window, board=self.board, name="rook", color=(255,255,255), image_path=os.path.abspath("assets/images/rook.jpg"))
                rook.set_position(grid_x=x, grid_y=7) 
                self.player_pieces.append(rook) # Append the new rook to the list of the player's pieces


            if x==1 or x==6: # If x is equal to 1 or 6
                # Spawn a knight at this position
                knight = GamePiece(window=self.window, board=self.board, name="knight", color=(255,255,255), image_path=os.path.abspath("assets/images/knight.jpg"))
                knight.set_position(grid_x=x, grid_y=7)
                self.player_pieces.append(knight) # Append the new knight to the list

            if x==2 or x==5: # If x is equal to 1 or 5
                # Spawn a bishop at this position
                bishop = GamePiece(window=self.window, board=self.board, name="bishop", color=(255,255,255), image_path=os.path.abspath("assets/images/bishop.jpg"))
                bishop.set_position(grid_x=x, grid_y=7)
                self.player_pieces.append(bishop) # Append the new bishop to the list     


            if x == 3: # If x is equal to 3
                # Spawn the queen at this position
                queen = GamePiece(window=self.window, board=self.board, name="queen", color=(255,255,255), image_path=os.path.abspath("assets/images/queen.jpg"))
                queen.set_position(grid_x=x, grid_y=7)
                self.player_pieces.append(queen) # Append the queen to the list


            if x == 4: # If x is equal to 4
                # Spawn the king at this position
                king = GamePiece(window=self.window, board=self.board, name="king", color=(255,255,255), image_path=os.path.abspath("assets/images/king.jpg"))
                king.set_position(grid_x=x, grid_y=7)
                self.player_pieces.append(king)  # Append the king to the list


    def spawn_enemy_pieces(self):
        "Spawn all the enemy's pieces"
        self.enemy_pieces = [] # List of pieces owned by the enemy

        for x in range(8): # For any x number between 0 included and 8 excluded
            # Spawn a new pawn at (x=x, y=1) positions
            pawn = GamePiece(window=self.window, board=self.board, name="pawn", color=(76,39,40), image_path=os.path.abspath("assets/images/pawn.jpg"))
            pawn.set_position(grid_x=x, grid_y=1)
            self.enemy_pieces.append(pawn)


        for x in range(8):  # For any x number between 0 included and 8 excluded
            # Spawn other pieces
            if x == 0 or x == 7: # If x is equal to 0 or 7
                # Spawn a rook at this position
                rook = GamePiece(window=self.window, board=self.board, name="rook", color=(76,39,40), image_path=os.path.abspath("assets/images/rook.jpg"))
                rook.set_position(grid_x=x, grid_y=0)
                self.enemy_pieces.append(rook)

            if x == 1 or x == 6: # If x is equal to 1 or 6
                # Spawn a kinght at this position
                knight = GamePiece(window=self.window, board=self.board, name="knight", color=(76,39,40), image_path=os.path.abspath("assets/images/knight.jpg"))
                knight.set_position(grid_x=x, grid_y=0)
                self.enemy_pieces.append(knight)    

            if x == 2 or x == 5: # If x is equal to 2 or 5
                # Spawn a bishop at this position
                bishop = GamePiece(window=self.window, board=self.board, name="bishop", color=(76,39,40), image_path=os.path.abspath("assets/images/bishop.jpg"))
                bishop.set_position(grid_x=x, grid_y=0)
                self.enemy_pieces.append(bishop)

            if x == 3: # If x is stricly equal to 3
                # Spawn the queen at this position
                queen = GamePiece(window=self.window, board=self.board, name="queen", color=(76,39,40), image_path=os.path.abspath("assets/images/queen.jpg"))
                queen.set_position(grid_x=x, grid_y=0)
                self.enemy_pieces.append(queen)

            if x == 4: # If x is stricly equal to 4      
                # Spawn the king at this position
                king = GamePiece(window=self.window, board=self.board, name="king", color=(76,39,40), image_path=os.path.abspath("assets/images/king.jpg"))
                king.set_position(grid_x=x, grid_y=0)
                self.enemy_pieces.append(king) 


    def place_pieces(self):
        "Place game pieces on the board"
        self.spawn_player_pieces() # Spawn the pieces of the player
        self.spawn_enemy_pieces() # Spawn the pieces of the enemy
           
            


    def run(self): 
        "Run the game loop."
        running = True # This variable is an indicator for the current running state of the game. When True, then the game continues running, 
                       # otherwise it stops.


        self.place_pieces()

        print(f"Piece at position {(7, 6)} :", identify_piece_by_position(position=(7,6), pieces_list=self.player_pieces))

        #piece = GamePiece(self.window, board=self.board, name="king", color=(255,255,255), image_path="assets/images/king.jpg")          
        #piece.set_position(1,7)   

        player_move = pygame.USEREVENT + 1 # Event which allow the player to move a piece
        pygame.time.set_timer(player_move, 100) # The player_move event will occur every 100 milliseconds  

        while running: # While the game is still running
            
            self.window.fill((255, 255, 255)) # Fill the window
            
            self.board.draw_squares() # Draw the squares of the board


            keys = pygame.key.get_pressed() # Get the keys pressed by the player
            for event in pygame.event.get(): # Capture any event that happens during the game
                if event.type == pygame.QUIT: # If the player wants to stop playing
                    if ask_quit(): # If the player confirmed his choice
                        running = False  


                """if keys[pygame.K_UP] or keys[pygame.K_z] and event.type == player_move: # If the player presses the up arrow key or the Z key
                    piece.move_to(piece.original_grid_x, piece.original_grid_y -1) # Move the piece forward

                if keys[pygame.K_DOWN] or keys[pygame.K_s] and event.type == player_move: # If the player presses the down arrow key or the S key
                    piece.move_to(piece.original_grid_x, piece.original_grid_y + 1) # Move the piece backward

                if keys[pygame.K_LEFT] or keys[pygame.K_q] and event.type == player_move: # If the player presses the left arrow key or the Q key
                    piece.move_to(piece.original_grid_x -1, piece.original_grid_y)  # Move the piece to the left

                if keys[pygame.K_RIGHT] or keys[pygame.K_d] and event.type == player_move: # If the player presses the right arrow key or the D key
                    piece.move_to(piece.original_grid_x +1, piece.original_grid_y) # Move the piece to the right              
                """

            for piece in self.player_pieces: # For each piece of the player
                piece.draw() # Draw the piece

            for piece in self.enemy_pieces: # For each piece of the enemy
                piece.draw() # Draw the piece    

            #piece.draw()

            pygame.display.flip() # Update the display                    





         
