from game import Square, Board
from typing import List

def squaresDrawer(squares: List[Square]):
    print('|'.join([str(square.piece) for square in squares]))

def boardDrawer(board: Board):
    for square in board.squares:
        squaresDrawer(square)