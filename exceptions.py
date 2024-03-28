class InvalidBoardDimensions(Exception):
    def __init__(self, message="The board should have a dimensions where have a center square."):
        self.message = message
        super().__init__(self.message)

class BoardDimensionsOutOfRange(Exception):
    def __init__(self, message="The board should have a max of 7 dimensions"):
        self.message = message
        super().__init__(self.message)