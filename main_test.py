import main

def test_vertical_judgement():
    mock_board = [
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0],
    ]

    assert main.judge(mock_board) == 1

    mock_board = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]

    assert main.judge(mock_board) == 1

    mock_board = [
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
    ]

    assert main.judge(mock_board) == 1

    mock_board = [
        [-1, 0, 0],
        [-1, 0, 0],
        [-1, 0, 0],
    ]

    assert main.judge(mock_board) == 0

    mock_board = [
        [0, -1, 0],
        [0, -1, 0],
        [0, -1, 0],
    ]

    assert main.judge(mock_board) == 0

    mock_board = [
        [0, 0, -1],
        [0, 0, -1],
        [0, 0, -1],
    ]

    assert main.judge(mock_board) == 0

def test_horizontal_judgement():
    mock_board = [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0],
    ]

    assert main.judge(mock_board) == 1

    mock_board = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0],
    ]

    assert main.judge(mock_board) == 1

    mock_board = [
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1],
    ]

    assert main.judge(mock_board) == 1

    mock_board = [
        [-1, -1, -1],
        [0, 0, 0],
        [0, 0, 0],
    ]

    assert main.judge(mock_board) == 0

    mock_board = [
        [0, 0, 0],
        [-1, -1, -1],
        [0, 0, 0],
    ]

    assert main.judge(mock_board) == 0

    mock_board = [
        [0, 0, 0],
        [0, 0, 0],
        [-1, -1, -1],
    ]

    assert main.judge(mock_board) == 0

def test_left_diagonal_judgement():
    mock_board = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]

    assert main.judge(mock_board) == 1

    mock_board = [
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, -1],
    ]

    assert main.judge(mock_board) == 0

def test_right_diagonal_judgement():
    mock_board = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
    ]

    assert main.judge(mock_board) == 1

    mock_board = [
        [0, 0, -1],
        [0, -1, 0],
        [-1, 0, 0],
    ]

    assert main.judge(mock_board) == 0

def test_draw_judgement():
    mock_board = [
        [1, -1, 1],
        [-1, 1, -1],
        [-1, 1, -1],
    ]

    assert main.judge(mock_board) == None