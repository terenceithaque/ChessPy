This game is a digital implementation of the popular chess game. It was made using the pygame library for Python. 

This game uses several scripts to work. 

* main.py is the entry point of the game. It imports the Game class from game.py, runs a first game, and one first game has ended, it enters a loop to ask the user if   he wants to replay

* game.py contains a Game class which handles the logic of the game

* board.py contains a Board class. This Board object can be displayed into the window with colored squares.

* piece.py contains a GamePiece class which handles a single piece on the board.

* customized_exceptions.py stores exceptions related to the game coding rules. If these rules aren't respected, Python raises one of these exceptions.

If you want to learn about the pygame library, please visit the official website located at https://www.pygame.org .