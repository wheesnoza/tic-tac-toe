import tkinter as tk
from tkinter import messagebox
from game import *

# Define the board size.
dimensions = int(input('Enter the dimensions of the board (example: 3):'))

# Build the board.
board = BoardBuilder(dimensions).build()

# Define the 2 players of the game with name and piece.
name, piece = input('Enter the player 1 name and the piece to use (ecample: John,o): ').split(',')
player1 = Player(name, Piece(piece))
name, piece = input('Enter the player 2 name and the piece to use (ecample: John,o): ').split(',')
player2 = Player(name, Piece(piece))

# Define all players list.
players = [player2, player1]

# Define the max movements until the game end.
remaining_movements = dimensions ** 2

def button_click(x, y):
    global board
    global remaining_movements
    player = players[remaining_movements % 2]
    buttons[x][y].config(text=str(player.piece), state='disabled')
    position_to_take = Position(x, y)
    square = board.squares.at_position(position_to_take)
    square.take(player.piece)
    remaining_movements -= 1

    if is_tree_in_line(board, square):
        messagebox.showinfo("Info", f"{player.name} wins.")
        window.quit()

    # If not have more remaining movements then is a draw.
    if not remaining_movements:
        messagebox.showinfo("Info", f"Draw.")
        window.quit()

window = tk.Tk()
window.title("TicTacToe")

# ウィンドウサイズを設定
window.geometry(f"{board.dimensions}00x{board.dimensions}00")

# 各行と列のサイズを均等に設定
for i in range(board.dimensions):
    window.grid_rowconfigure(i, weight=1, minsize=100)
    window.grid_columnconfigure(i, weight=1, minsize=100)

buttons = []

# ボタンの作成と配置
for i in range(board.dimensions):
    row_buttons = []
    for j in range(board.dimensions):
        button = tk.Button(window, font=("Helvetica", 50, "bold"), disabledforeground="white")
        button.grid(row=i, column=j, sticky="nsew")
        button.bind('<ButtonRelease>', lambda event, x=i, y=j: button_click(x, y))
        row_buttons.append(button)
    buttons.append(row_buttons)


window.mainloop()