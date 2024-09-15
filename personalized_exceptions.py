"Personalized exceptions for the game"

class NotGamePieceException(Exception):
    "An exception that raises if an object is not of type GamePiece"
    def __init__(self, message):
        super().__init__(message)