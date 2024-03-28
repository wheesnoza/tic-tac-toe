from game import Square, Board
from typing import List

def rowDrawer(row: List[Square]):
    print('|'.join([str(square.piece) for square in row]))
    

def boardDrawer(board: Board):
    for square in board.squares:
        rowDrawer(square)