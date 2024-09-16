"piece.py contains a general GamePiece class which allow to create a generic piece for the game"
import pygame
import os
import numpy as np
from customized_exceptions import * # Import customized_exceptions to access game-specific exceptions





def identify_piece_by_position(position=(0,0), pieces_list=[], return_object=False): 
    """Iterates over a list of game pieces, compares the position of the piece to the value of the position setting, if it matches, return the name of the piece or the piece itself.
    - The position setting represent a tuple containing (x,y) where x and y are the positions of the piece to be identified
    - The pieces_list setting represent the group of pieces in which we must search a piece that have the position described by the position setting
    - return_object is a boolean with False as default value. If it's False, the function only returns the name of the piece that have the described position, otherwise it returns the whole usable piece object."""
    
    for piece in pieces_list: # For each piece of the list
        if type(piece).__name__ != "GamePiece": # If the piece is not a GamePiece object
            raise NotGamePieceException(message=f"Objects in the pieces_list setting must be GamePiece objects, not {type(piece).__name__} objects.") # Raise a NotGamePieceException error
        
        if piece.get_position() == position: # If the position of piece matches the position given to the function
            if return_object: # If we must return the whole piece object, not simply the name
                return piece # Return the piece object
            
            return piece.name # If we only have to return the name of the piece, then return just the name
        

def identify_piece_by_rect(rect=pygame.Rect(0, 0, 1, 1), pieces_list=[], return_object=False):
    """Iterates over a list of game pieces, compares the rect of the piece to the value of the rect setting, if it matches, return the name of the piece or the piece itself.
    - The rect is the rect of the piece we want to find
    - The pieces_list setting represent the group of pieces in which we must search a piece that have the rect described by the rect setting
    - return_object is a boolean with False as default value. If it's False, the function only returns the name of the piece that have the described rect, otherwise it returns the whole usable piece object."""
    
    for piece in pieces_list: # For each piece of the list
        if type(piece).__name__ != "GamePiece": # If the piece is not a GamePiece object
            raise NotGamePieceException(message=f"Objects in the pieces_list setting must be GamePiece objects, not {type(piece).__name__} objects.") # Raise a NotGamePieceException error
        
        print(f"Piece rect {piece.rect}")
        if pygame.Rect.colliderect(piece.rect, rect): # If the rect of the piece is equal to the rect value given as setting
            if return_object: # If we must return the whole object
                return piece
            
            return piece.name # Otherwise, return only the name of the piece


class GamePiece(pygame.sprite.Sprite):
    def __init__(self, window, board, name="pawn", color=(255,255,255), image_path=os.path.abspath("assets/images/pawn.jpg")):
        "The GamePiece class allows to create a game piece with general attributes"
        super().__init__() # We inherit of the Sprite object from pygame.sprite
        self.available_names = ["pawn", "rook", "knight", "bishop", "king", "queen"] # List of available names for a game piece
        self.name = name # Name of the piece (pawn, rook, king,...)
        if self.name.lower() not in self.available_names: # If the current name of the piece isn't available
            raise NameNotAvailableException(message=f"Name {self.name} is not available for GamePiece objects. Available names are {self.available_names}.") # Raise a NameNotAvailableException
        self.color = color # Color of the piece
        self.image = pygame.image.load(image_path) # Load the image which represents the piece
        self.image = pygame.transform.scale(self.image, (75, 70)) # Modify the dimensions of the image to 75x70
        self.colored_image_surf = pygame.Surface(self.image.get_size()) # Surface that will host the colored image (color setting)
        self.colored_image_surf.set_alpha(255)


        # Fill the surface with the indicated RGB color
        self.colored_image_surf.fill(color)
        

        # Draw the image
        self.colored_image_surf.blit(self.image, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
        
        self.rect = self.image.get_rect() # Get the image's rect
        self.window = window # The game window on which the piece must be displayed
        self.board = board # Game board on which the piece must appear
        
        
        # Map grid coordinates to pixel coordinates
        self.pixel_x = None 
        self.pixel_y = None


        # Store the original grid coordinates
        self.original_grid_x = None
        self.original_grid_y = None

        # Dictionnary of possible moves for each piece in the game.
        # For each piece name, we associate a list of moves, and each move has a name  of the  'move_name-max_cells_by_move' or a single letter that looks like the form of the move
        self.pieces_moves = {"pawn":["vert-1", "vert-2"], # Pawns can move vertically 1 time, but max 2 times at the beginning of the game
                             "knight":["L"], # Knights can make a 'L'-like move
                             "bishop":["angled-any"], # Bishops can move in angle for any distance they want, hence the 'any' distance
                             "rook":["vert-any"], # Rooks can move vertically for any distance they want, hence the 'any' distance
                             "king":["any-1"], # Kings can move in any direction they want, but only at a distance of 1
                             "queen":["any-any"] # Queens can move in any direction they want and for any distance they want
                             }  
        
        
        self.available_moves = self.pieces_moves[self.name] # Get the available moves for the current piece
        print(f"Available moves for {self.name} : {self.available_moves}")

    def set_position(self, grid_x, grid_y):
        "Set the position of the piece on the board"
        self.original_grid_x = grid_x # Set the x position
        self.original_grid_y = grid_y # Set the y position
        #print(f"New position for {self.name} :",  self.original_grid_x, ",", self.original_grid_y)
        self.update_pixel_coordinates() # Update the pixel coordinates of the piece to display it on the board

    def get_position(self):
        "Returns a tuple with the current x and y positions of the piece"
        #print(f"{self.name}'s position is {(self.original_grid_x, self.original_grid_y)}")
        return (self.original_grid_x, self.original_grid_y) 


    def update_pixel_coordinates(self):
        "Update pixel coordinates based on grid coordinates"
        if self.board:
            grid_width = len(self.board.grid[0]) * (75 + 1) # 75 is the square size, 1 is the spacing
            grid_height = len(self.board.grid) * (75 + 1)   

            #print(f"Grid width : {grid_width}")
            #print(f"grid height : {grid_height}")

            # Update the pixel x and y coordinates
            self.pixel_x = self.original_grid_x * (75+1)
            self.pixel_y = self.original_grid_y * (75+1)

            #print("x coordinate :", self.pixel_x)
            #print("y coordinate :", self.pixel_y)
            
            # If the piece is out of the game board
            if self.pixel_x < 0 : 
                #print(f"{self.name} is out of the board")
                self.pixel_x = 0

            if self.pixel_x > grid_width:
                #print(f"{self.name} is out of the board")
                self.pixel_x = grid_width    

            if self.pixel_y < 0:
                #print(f"{self.name} is out of the board")
                self.pixel_y = 0

            if self.pixel_y > 532:
                #print(f"{self.name} is out of the board")
                self.pixel_y = 532    
            
            self.rect.x = self.pixel_x
            self.rect.y = self.pixel_y


    def move_to(self, new_grid_x, new_grid_y):
        "Move the piece"     
        self.set_position(new_grid_x, new_grid_y) # Update the position of the piece  
            

        


    def draw(self):
        "Draw the piece on the screen"
        self.window.blit(self.colored_image_surf, (self.rect.x, self.rect.y)) # Draw the surface of the image at current x and y positions



