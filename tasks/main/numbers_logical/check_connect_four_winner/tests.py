from generated_function import check_connect_four_winner

def test_c4_horizontal_win():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    assert check_connect_four_winner(board) == 1

def test_c4_vertical_win():
    board = [
        [0, 2, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    assert check_connect_four_winner(board) == 2

def test_c4_diagonal_win():
    board = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 2, 0, 0, 0],
        [0, 1, 2, 2, 0, 0, 0],
        [1, 2, 2, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    assert check_connect_four_winner(board) == 1

def test_c4_no_winner():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0],
        [0, 2, 2, 1, 0, 0, 0],
        [0, 1, 1, 2, 0, 0, 0],
        [2, 2, 1, 1, 0, 0, 0]
    ]
    assert check_connect_four_winner(board) is None

def test_overlapping_win():
    board = [
        [0, 1, 0, 2, 0, 0, 0],
        [0, 1, 2, 1, 0, 0, 0],
        [0, 2, 1, 1, 0, 0, 0],
        [2, 1, 1, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    assert check_connect_four_winner(board) == 2

def test_interrupted_win():
    board = [
        [1, 1, 1, 0, 2, 2, 1],
        [2, 1, 2, 1, 1, 1, 2],
        [1, 2, 0, 2, 2, 1, 1],
        [2, 1, 0, 1, 0, 2, 2],
        [1, 2, 0, 2, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 2]
    ]
    assert check_connect_four_winner(board) is None
