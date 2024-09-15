"Personalized exceptions for the game"

class NotGamePieceException(Exception):
    "An exception that raises if an object is not of type GamePiece"
    def __init__(self, message="Not a GamePiece object"):
        super().__init__(message) # Init the exception with the message setting


class NameNotAvailableException(Exception):
    "An exception that raises if a string 'name' is not available for an  object" 
    def __init__(self, message="Name not available for object"):
        super().__init__(message) # Init the exception with the message setting



        