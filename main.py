def judge(board, player, x, y):
    number_of_available_directions_range = range(0, 3)
    middle = [1, 1]
    condition_to_win = 3
    horizontal = 0
    vertical = 0
    diagonal = 0
    
    if [x, y] == middle:
        number_of_available_directions_range = range(1, 4) 
    
    for direction in number_of_available_directions_range:
        adjacent_y = abs(x - direction)
        adjacent_x = abs(y - direction)
        horizontal_value = board[x][adjacent_y]
        vertical_value = board[adjacent_x][y]
        diagonal_value = board[adjacent_x][adjacent_y]
        if horizontal_value == player:
            horizontal += 1
        if vertical_value == player:
            vertical += 1
        if diagonal_value == player:
            diagonal += 1
    if horizontal == condition_to_win or vertical == condition_to_win or diagonal == condition_to_win:
        return True
    
    return False

def drawBoard(board):
    pieces = {-1: ' ', 0: 'o', 1: 'x'}
    for line in board:
        print(pieces[line[0]], '|', pieces[line[1]], '|', pieces[line[2]])
        

def game():
    board = [[-1, -1, -1],[-1, -1, -1],[-1, -1, -1]]
    player = 0
    movements = 0
    while True:
        drawBoard(board)
        try:
            coordinates = input(f"プレイヤー{player + 1}の取るマスの座標を指定してください。").split(',')
            if int(coordinates[0]) == -1:
                print('ゲームを終了します。')
                break
            x = int(coordinates[0])
            y = int(coordinates[1])
        except:
            print('正しい値を入力してください。')
            continue
        if board[x][y] != -1:
            print('別のマスを指定してください。')
            continue
        board[x][y] = player

        have_winner = judge(board, player, x, y)

        if have_winner:
            drawBoard(board)
            print(f"プレイヤー{player + 1}の勝ち")
            break
        movements += 1
        if movements >= 9:
            drawBoard(board)
            print('引き分けです。')
            break
        if player:
            player = 0
        else:
            player = 1

if __name__ == '__main__':
    # print(-1 + -1 + -1, 1 + 1 + 1)
    # examine([
    #     ['0,0', '0,1', '0,2'],
    #     ['1,0', '1,1', '1,2'],
    #     ['2,0', '2,1', '2,2']
    # ], 1, 1)
    # print(judge([
    #     [0, -1, 0],
    #     [1, 1, 0],
    #     [0, 0, 0]
    # ], 1, 0))
    game()