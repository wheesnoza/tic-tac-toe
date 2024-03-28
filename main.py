from game import *
from drawer import *

if __name__ == '__main__':
    # Define the board size.
    dimensions = int(input('Enter the dimensions of the board (example: 3):'))

    # Build the board.
    board = BoardBuilder(dimensions).build()
    
    # Define the 2 players of the game with name and piece.
    name, piece = input('Enter the player 1 name and the piece to use (ecample: John,o): ').split(',')
    player1 = Player(name, Piece(piece))
    name, piece = input('Enter the player 2 name and the piece to use (ecample: John,o): ').split(',')
    player2 = Player(name, Piece(piece))
    
    # Define the max movements until the game end.
    remaining_movements = dimensions ** 2
    
    # Define all players list.
    players = [player2, player1]

    # Start and continue the game while there are remaining movements.
    while remaining_movements > 0:
        player = players[remaining_movements % 2]
        boardDrawer(board)
        x, y = input(f"{player.name} movement(example: 1,1): ").split(',')
        position_to_take = Position(x, y)
        square = board.squares.at_position(position_to_take)
        square.take(player.piece)
        remaining_movements -= 1

        if is_tree_in_line(board, square):
            boardDrawer(board)
            print(f"{player.name} wins.")
            break
    
    # If not have more remaining movements then is a draw.
    if not remaining_movements:
        boardDrawer(board)
        print('Draw')