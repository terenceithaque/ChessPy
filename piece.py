"piece.py contains a general GamePiece class which allow to create a generic piece for the game"
import pygame
import os
import numpy as np

class GamePiece(pygame.sprite.Sprite):
    def __init__(self, window, board, name="pawn", color=(255,255,255), image_path=os.path.abspath("assets/images/pawn.jpg")):
        "The GamePiece class allows to create a game piece with general attributes"
        self.name = name # Name of the piece (pawn, rook, king,...)
        self.color = color # Color of the piece
        self.image = pygame.image.load(image_path) # Load the image which represents the piece
        self.image = pygame.transform.scale(self.image, (75, 70)) # Modify the dimensions of the image to 75x70
        
        self.rect = self.image.get_rect() # Get the image's rect
        self.window = window # The game window on which the piece must be displayed
        self.board = board # Game board on which the piece must appear
        
        
        # Map grid coordinates to pixel coordinates
        self.pixel_x = None 
        self.pixel_y = None


        # Store the original grid coordinates
        self.original_grid_x = None
        self.original_grid_y = None


    def set_position(self, grid_x, grid_y):
        "Set the position of the piece on the board"
        self.original_grid_x = grid_x # Set the x position
        self.original_grid_y = grid_y # Set the y position
        self.update_pixel_coordinates() # Update the pixel coordinates of the piece to display it on the board


    def update_pixel_coordinates(self):
        "Update pixel coordinates based on grid coordinates"
        if self.board:
            grid_width = len(self.board.grid[0]) * (75 + 1) # 75 is the square size, 1 is the spacing
            grid_height = len(self.board.grid) * (75 + 1)   

            # Update the pixel x and y coordinates
            self.pixel_x = self.original_grid_x * (75+1)
            self.pixel_y = self.original_grid_y * (75+1)


            self.rect.x = self.pixel_x
            self.rect.y = self.pixel_y


    def move_to(self, new_grid_x, new_grid_y):
        "Move the piece"     
        self.set_position(new_grid_x, new_grid_y) # Update the position of the piece  
            

        


    def draw(self):
        "Draw the piece on the screen"
        self.window.blit(self.image, (self.rect.x, self.rect.y)) # Draw the image at the current x and y positions    



