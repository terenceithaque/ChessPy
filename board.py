"board.py contains a Board class which represent the graphical game board"
import pygame # Import the pygame module

class Board:
    def __init__(self, window, grid=[]):
        "A graphical chess board for the game based on a grid list"
        self.window = window # The game window in which we must display the graphical board
        self.grid = grid # The grid on which the graphical board is based

        self.square_colors = [(255, 228, 196 ), (0, 0, 0)] # Colors for the squares on the board, in RGB encoding. The first one stands for "bisque", and the second one for "black".

        self.square_surfs = [] # List of all squares in the board, where each square is a surface

        print(f"Board dimensions : {self.get_dimensions()}")

        self.square_size = 75 # Size of each square

        self.square_spacing = 1 # Spacing between each square on the board

    def draw_squares(self):
        "Draws all board squares based on the length of the grid"

        for row in range(len(self.grid)): # For each row of the grid
            #print(self.grid[row])
            for col in range(len(self.grid[row])): # For each column of the row
                square_surf = pygame.Surface((self.square_size, self.square_size)) # Create a surface to contain the square

                x = col * (self.square_size + self.square_spacing) # x position for the current square
                y = row * (self.square_size + self.square_spacing) # y position for the current square

                square_color = self.square_colors[(row + col) % len(self.square_colors)]  # Color of the current square
                
                square_surf.fill(square_color) # Fill the surface with the square's color


                self.square_surfs.append((square_surf, x, y)) # Append the square's surface  and position to the list of surfaces


            self.window.fill((255,255,255))
            for surf, x,y in self.square_surfs:
                self.window.blit(surf, (x,y))


    def get_surface_at_position(self, position=(0,0)):
        "Returns a surface representing a square which have the specified position"
        
        position_rect = pygame.Rect(position[0], position[1], 1, 1) # Create a rect object corresponding to the given position
        for surf_object, x, y in self.square_surfs: # For each surface representing a square
            surf_rect = surf_object.get_rect() # Get the rect of the surface
            if pygame.Rect.colliderect(surf_rect, position_rect): # If the surface is in collision with the position's rect, then it is the surface we're looking for
                return surf_object # Return the surface


    
    def draw_on_square(self, width=10, height=10, color=(255,255,255), square_pos=(0,0)):
        "Draws a form on a square"
        surface = self.get_surface_at_position(square_pos) # Get the surface object which corresponds to the given position
        #print(f"Drawing on surface {surface} located at {square_pos}")

        if surface: # If there is a surface at the given position
            #print(f"A surface was found at {square_pos}")
            rect = (square_pos[0], square_pos[1], width,height) # Create a tuple containing the attributes of the rect object to be drawn
            # Draw the rect
            displayed_rect = pygame.draw.rect(surface, color, rect)
            # Update the display
            pygame.display.update(displayed_rect)   
            self.window.blit(surface, square_pos) # Draw the up-to-dates surface
             



        else: # If there is no surface at the given position
            print(f"No surface found at {square_pos}")    

    
    def get_dimensions(self):
        "Return the dimensions of the board as a tuple of int numbers"
        width = len(self.grid[0]) 
        height = len(self.grid) 
        return (width, height)