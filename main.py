def judge(board):
    player1win = -3
    player2win = 3
    # 縦判定
    for x in range(3):
        result = 0
        for y in range(3):
            result += board[y][x]
        if result == player1win:
            return 0
        elif result == player2win:
            return 1
    # 横判定
    for x in range(3):
        result = 0
        for y in range(3):
            result += board[x][y]
        if result == player1win:
            return 0
        elif result == player2win:
            return 1
    # 左斜めチェック
    result = 0
    for x in range(3):
        result += board[x][x]
        if result == player1win:
            return 0
        elif result == player2win:
            return 1
    # 右斜めチェック
    result = 0
    for x, y in zip(range(3), range(2, -1, -1)):
        result += board[x][y]
        if result == player1win:
            return 0
        elif result == player2win:
            return 1

def drawBoard(board):
    pieces = {-1: 'o', 0: ' ', 1: 'x'}
    for line in board:
        print(pieces[line[0]], '|', pieces[line[1]], '|', pieces[line[2]])
        

def game():
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    figures = [-1,1]
    player = 0
    movements = 0
    while True:
        drawBoard(board)
        try:
            inp = input(f"プレイヤー{player + 1}の取るマスの座標を指定してください。")
            if int(inp) == -1:
                print('ゲームを終了します。')
                break
            coordinates = inp.split(',')
            x = int(coordinates[0])
            y = int(coordinates[1])
        except:
            print('正しい値を入力してください。')
            continue
        if board[x][y] != 0:
            print('別のマスを指定してください。')
            continue
        board[x][y] = figures[player]
        if player >= 1:
            player = 0
        else:
            player += 1

        judgement = judge(board)
        if judgement == 0:
            drawBoard(board)
            print('プレイヤー１の勝ち')
            break
        elif judgement == 1:
            drawBoard(board)
            print('プレイヤー２の勝ち')
            break
        movements += 1
        if movements >= 9:
            drawBoard(board)
            print('引き分けです。')
            break

if __name__ == '__main__':
    game()