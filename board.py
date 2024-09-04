"board.py contains a Board class which represent the graphical game board"
import pygame # Import the pygame module

class Board:
    def __init__(self, window, grid=[]):
        "A graphical chess board for the game based on a grid list"
        self.window = window # The game window in which we must display the graphical board
        self.grid = grid # The grid on which the graphical board is based

        self.square_colors = [(255, 228, 196 ), (0, 0, 0)] # Colors for the squares on the board, in RGB encoding. The first one stands for "bisque", and the second one for "black".

        self.squares = [] # List of all squares in the board

    def draw_squares(self):
        "Draws all board squares based on the length of the grid"

        square_size = 75 # Size for each square on the board
        square_spacing = 1 # Spacing between squares
        for row in range(len(self.grid)): # For each row of the grid
            #print(self.grid[row])
            for col in range(len(self.grid[row])): # For each column of the row

                x = col * (square_size + square_spacing) # x position for the current square
                y = row * (square_size + square_spacing) # y position for the current square

                square_color = self.square_colors[(row + col) % len(self.square_colors)]  # Color of the current square

                pygame.draw.rect(self.window, square_color, (x,y, square_size, square_size)) # Draw the square