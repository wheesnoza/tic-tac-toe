from game import *
from exceptions import *
import pytest

def test_non_middle_square_board_can_not_be_builded():
    with pytest.raises(InvalidBoardDimensions):
        BoardBuilder(2).build()

def test_board_with_dimensions_out_of_range_can_not_be_builded():
    with pytest.raises(BoardDimensionsOutOfRange):
        BoardBuilder(9).build()

def test_board_can_be_builded():
    board = BoardBuilder(3).build()
    assert isinstance(board, Board)

def test_horizontal_is_tree_in_line():
    piece = Piece('o')
    squares = SquareList([
        [Square(Position(0,0)).take(piece),Square(Position(0,1)),Square(Position(0,2))],
        [Square(Position(1,0)).take(piece),Square(Position(1,1)),Square(Position(1,2))],
        [Square(Position(2,0)).take(piece),Square(Position(1,2)),Square(Position(2,2))],
    ])

    boundary_range = BoundaryRange(0, 3)
    board = Board(3, squares, boundary_range)
    assert is_tree_in_line(board, Square(Position(0,0)).take(piece)) == True

def test_vertical_is_tree_in_line():
    piece = Piece('o')
    squares = SquareList([
        [Square(Position(0,0)).take(piece),Square(Position(0,1)).take(piece),Square(Position(0,2)).take(piece)],
        [Square(Position(1,0)),Square(Position(1,1)),Square(Position(1,2))],
        [Square(Position(2,0)),Square(Position(1,2)),Square(Position(2,2))],
    ])

    boundary_range = BoundaryRange(0, 3)
    board = Board(3, squares, boundary_range)
    assert is_tree_in_line(board, Square(Position(0,0)).take(piece)) == True

def test_diagonal_is_tree_in_line():
    piece = Piece('o')
    squares = SquareList([
        [Square(Position(0,0)).take(piece),Square(Position(0,1)),Square(Position(0,2))],
        [Square(Position(1,0)),Square(Position(1,1)).take(piece),Square(Position(1,2))],
        [Square(Position(2,0)),Square(Position(1,2)),Square(Position(2,2)).take(piece)],
    ])

    boundary_range = BoundaryRange(0, 3)
    board = Board(3, squares, boundary_range)

    assert is_tree_in_line(board, Square(Position(0,0)).take(piece)) == True

    piece = Piece('o')
    squares = SquareList([
        [Square(Position(0,0)),Square(Position(0,1)),Square(Position(0,2)).take(piece)],
        [Square(Position(1,0)),Square(Position(1,1)).take(piece),Square(Position(1,2))],
        [Square(Position(2,0)).take(piece),Square(Position(1,2)),Square(Position(2,2))],
    ])

    boundary_range = BoundaryRange(0, 3)
    board = Board(3, squares, boundary_range)

