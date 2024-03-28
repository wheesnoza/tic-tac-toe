from typing import List

class InvalidBoardDimension(Exception):
    def __init__(self, message="The board should have a dimension where have a center square."):
        self.message = message
        super().__init__(self.message)

class Piece:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value

class Player:
    def __init__(self, name: str, piece: Piece):
        self.name = name
        self.piece = piece

class Position:
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)
    
    def equal(self, another_position: 'Position'):
        return self.x == another_position.x and self.y == another_position.y

class Square:
    piece = Piece(' ')
    def __init__(self, position: Position):
        self.position = position
    
    def take(self, piece: Piece):
        self.piece = piece
        return self

    def isNotEmpty(self):
        return self.piece != ' '

class SquareList(List[List[Square]]):
    def __init__(self, *args: List[List[Square]], **kwargs: List[List[Square]]):
        super().__init__(*args, **kwargs)
    
    def at(self, x: int, y: int) -> Square:
        return self[x][y]

    def at_position(self, position: Position) -> Square:
        return self.at(position.x, position.y)

class Board:
    def __init__(self, squares: SquareList):
        self.squares = squares

class BoardBuilder:
    def __init__(self, dimensions: int):
        if not dimensions % 2:
            raise InvalidBoardDimension
        self.dimensions = dimensions
    
    def build(self):
        squares = SquareList([Square(Position(x, y)) for y in range(self.dimensions)] for x in range(self.dimensions))
        return Board(squares)

class Line(List[Square]):
    def __init__(self, *args: List[Square], **kwargs: List[Square]):
        super().__init__(*args, **kwargs)
    
    def is_all_equals(self):
        return all(square.piece == self[0].piece for square in self)
    
class Lines:
    horizontal: Line
    vertical: Line
    diagonal: Line
    def __init__(self, horizontal: Line, vertical: Line, diagonal: Line):
        self.horizontal = horizontal
        self.vertical = vertical
        self.diagonal = diagonal



def rowDrawer(row: List[Square]):
        print('|'.join([str(square.piece) for square in row]))
    

def boardDrawer(board: Board):
    for square in board.squares:
        rowDrawer(square)


def adjacent_lines(board: Board, square: Square) -> Lines:
    number_of_available_directions_range = range(0, 3)
    position = square.position
    middle = Position(1, 1)
    
    if position.equal(middle):
        number_of_available_directions_range = range(1, 4)

    horizontal_adjacent_squares = Line()
    vertical_adjacent_squares = Line()
    diagonal_adjacent_squares = Line()
    
    for direction in number_of_available_directions_range:
        adjacent_x = abs(position.y - direction)
        adjacent_y = abs(position.x - direction)
        horizontalSquare = board.squares.at(position.x, adjacent_y)
        verticalSquare = board.squares.at(adjacent_x, position.y)
        diagonalSquare = board.squares.at(position.x, adjacent_y)
        if horizontalSquare.isNotEmpty():
            horizontal_adjacent_squares.append(horizontalSquare)
        if verticalSquare.isNotEmpty():
            vertical_adjacent_squares.append(verticalSquare)
        if diagonalSquare.isNotEmpty():
            diagonal_adjacent_squares.append(diagonalSquare)
    
    return Lines(horizontal_adjacent_squares, vertical_adjacent_squares, diagonal_adjacent_squares)


def tree_in_line():
    adjacent_squares = adjacent_lines(board, square)
    return adjacent_squares.horizontal.is_all_equals() or adjacent_squares.vertical.is_all_equals() or adjacent_squares.diagonal.is_all_equals()

if __name__ == '__main__':
    # Define the board size.
    dimensions = int(input('Enter the dimensions of the board (example: 3):'))
    
    # Define the 2 players of the game with name and piece.
    name, piece = input('Enter the player 1 name and the piece to use (ecample: John,o): ').split(',')
    player1 = Player(name, Piece(piece))
    name, piece = input('Enter the player 2 name and the piece to use (ecample: John,o): ').split(',')
    player2 = Player(name, Piece(piece))
    
    # Define the max movements until the game end.
    remaining_movements = dimensions ** 2
    
    # Define all players list.
    players = [player2, player1]

    # Build the board.
    board = BoardBuilder(dimensions).build()

    # Start and continue the game while there are remaining movements.
    while remaining_movements > 0:
        player = players[remaining_movements % 2]
        boardDrawer(board)
        x, y = input(f"{player.name} movement(example: 1,1): ").split(',')
        position_to_take = Position(x, y)
        square = board.squares.at_position(position_to_take)
        square.take(player.piece)
        remaining_movements -= 1

        if tree_in_line():
            boardDrawer(board)
            print(f"{player.name} wins.")
            break
    
    # If not have more remaining movements then is a draw.
    if not remaining_movements:
        boardDrawer(board)
        print('Draw')