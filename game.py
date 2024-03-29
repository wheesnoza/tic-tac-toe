import exceptions
from typing import List

class Piece:
    def __init__(self, value: str):
        self.value = value

    def is_equal(self, anotherPiece: 'Piece'):
        return self.value == anotherPiece.value

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
    
    def plain(self):
        return self.x, self.y
    
    def equal(self, another_position: 'Position'):
        return self.x == another_position.x and self.y == another_position.y

class Square:
    piece = Piece(' ')
    def __init__(self, position: Position):
        self.position = position
    
    def take(self, piece: Piece):
        self.piece = piece
        return self

    def is_not_blank(self):
        return self.piece.value != ' '

class SquareList(List[List[Square]]):
    def __init__(self, *args: List[List[Square]], **kwargs: List[List[Square]]):
        super().__init__(*args, **kwargs)
    
    def at(self, x: int, y: int) -> Square:
        return self[x][y]

    def at_position(self, position: Position) -> Square:
        return self.at(position.x, position.y)
    
class BoundaryRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.range = [x for x in range(self.start, self.end)]

class Board:
    def __init__(self, dimensions: int, squares: SquareList, boundary_range: BoundaryRange):
        self.dimensions = dimensions
        self.squares = squares
        self.boundary_range = boundary_range

class BoardBuilder:
    MAX_DIMENSIONS = 7
    def __init__(self, dimensions: int):
        if dimensions > self.MAX_DIMENSIONS:
            raise exceptions.BoardDimensionsOutOfRange
        if not dimensions % 2:
            raise exceptions.InvalidBoardDimensions
        self.dimensions = dimensions
    
    def build(self):
        # Iterate board squares by dimensions.
        squares = SquareList([Square(Position(x, y)) for y in range(self.dimensions)] for x in range(self.dimensions))
        boundary_range = BoundaryRange(0, self.dimensions)
        return Board(self.dimensions, squares, boundary_range)

class Line(List[Square]):
    def __init__(self, *args: List[Square], **kwargs: List[Square]):
        super().__init__(*args, **kwargs)
    
class Lines:
    vertical: Line
    horizontal: Line
    left_diagonal: Line
    right_diagonal: Line
    
    def __init__(self, vertical: Line, horizontal: Line, left_diagonal: Line, right_diagonal: Line):
        self.vertical = vertical
        self.horizontal = horizontal
        self.left_diagonal = left_diagonal
        self.right_diagonal = right_diagonal
    
    def all(self):
        return [self.vertical, self.horizontal, self.left_diagonal, self.right_diagonal]

def adjacent_lines(board: Board, square: Square) -> Lines:
    placed_position = square.position
    
    positive_direction = board.boundary_range.range
    negative_direction = board.boundary_range.range[::-1]

    horizontal_adjacent_squares = Line()
    vertical_adjacent_squares = Line()
    left_diagonal_adjacent_squares = Line()
    right_diagonal_adjacent_squares = Line()

    for direction in board.boundary_range.range:
        vertical_adjacent_squares.append(board.squares.at(positive_direction[direction], placed_position.y))
        horizontal_adjacent_squares.append(board.squares.at(placed_position.x, positive_direction[direction]))
        left_diagonal_adjacent_squares.append(board.squares.at(positive_direction[direction], positive_direction[direction]))
        right_diagonal_adjacent_squares.append(board.squares.at(negative_direction[direction], positive_direction[direction]))
    
    return Lines(vertical_adjacent_squares, horizontal_adjacent_squares, left_diagonal_adjacent_squares,right_diagonal_adjacent_squares)

def is_tree_in_line(board: Board, square: Square):
    line = adjacent_lines(board, square)
    
    tree_in_horizontal = len([square.piece.value for square in line.horizontal if square.is_not_blank() and square.piece.is_equal(square.piece)]) == board.dimensions
    tree_in_vertical = len([square.piece.value for square in line.vertical if square.is_not_blank() and square.piece.is_equal(square.piece)]) == board.dimensions
    tree_in_left_diagonal = len([square.piece.value for square in line.left_diagonal if square.is_not_blank() and square.piece.is_equal(square.piece)]) == board.dimensions
    tree_in_right_diagonal = len([square.piece.value for square in line.right_diagonal if square.is_not_blank() and square.piece.is_equal(square.piece)]) == board.dimensions

    return any([tree_in_horizontal, tree_in_vertical, tree_in_left_diagonal, tree_in_right_diagonal])