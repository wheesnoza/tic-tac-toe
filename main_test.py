import main
import pytest

def test_non_middle_square_board_can_not_be_builded():
    with pytest.raises(main.InvalidBoardDimensions):
        main.BoardBuilder(2).build()

def test_board_with_dimensions_out_of_range_can_not_be_builded():
    with pytest.raises(main.BoardDimensionsOutOfRange):
        main.BoardBuilder(9).build()

def test_board_can_be_builded():
    board = main.BoardBuilder(3).build()
    assert isinstance(board, main.Board)

def test_horizontal_is_tree_in_line():
    piece = main.Piece('o')
    squares = main.SquareList([
        [main.Square(main.Position(0,0)).take(piece),main.Square(main.Position(0,1)),main.Square(main.Position(0,2))],
        [main.Square(main.Position(1,0)).take(piece),main.Square(main.Position(1,1)),main.Square(main.Position(1,2))],
        [main.Square(main.Position(2,0)).take(piece),main.Square(main.Position(1,2)),main.Square(main.Position(2,2))],
    ])

    boundary_range = main.BoundaryRange(0, 3)
    board = main.Board(3, squares, boundary_range)
    assert main.is_tree_in_line(board, main.Square(main.Position(0,0)).take(piece)) == True

def test_vertical_is_tree_in_line():
    piece = main.Piece('o')
    squares = main.SquareList([
        [main.Square(main.Position(0,0)).take(piece),main.Square(main.Position(0,1)).take(piece),main.Square(main.Position(0,2)).take(piece)],
        [main.Square(main.Position(1,0)),main.Square(main.Position(1,1)),main.Square(main.Position(1,2))],
        [main.Square(main.Position(2,0)),main.Square(main.Position(1,2)),main.Square(main.Position(2,2))],
    ])

    boundary_range = main.BoundaryRange(0, 3)
    board = main.Board(3, squares, boundary_range)
    assert main.is_tree_in_line(board, main.Square(main.Position(0,0)).take(piece)) == True

def test_diagonal_is_tree_in_line():
    piece = main.Piece('o')
    squares = main.SquareList([
        [main.Square(main.Position(0,0)).take(piece),main.Square(main.Position(0,1)),main.Square(main.Position(0,2))],
        [main.Square(main.Position(1,0)),main.Square(main.Position(1,1)).take(piece),main.Square(main.Position(1,2))],
        [main.Square(main.Position(2,0)),main.Square(main.Position(1,2)),main.Square(main.Position(2,2)).take(piece)],
    ])

    boundary_range = main.BoundaryRange(0, 3)
    board = main.Board(3, squares, boundary_range)

    assert main.is_tree_in_line(board, main.Square(main.Position(0,0)).take(piece)) == True

    piece = main.Piece('o')
    squares = main.SquareList([
        [main.Square(main.Position(0,0)),main.Square(main.Position(0,1)),main.Square(main.Position(0,2)).take(piece)],
        [main.Square(main.Position(1,0)),main.Square(main.Position(1,1)).take(piece),main.Square(main.Position(1,2))],
        [main.Square(main.Position(2,0)).take(piece),main.Square(main.Position(1,2)),main.Square(main.Position(2,2))],
    ])

    boundary_range = main.BoundaryRange(0, 3)
    board = main.Board(3, squares, boundary_range)

