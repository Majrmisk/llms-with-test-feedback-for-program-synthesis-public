from generated_function import minimax_tic_tac_toe

def test_terminal_x_win():
    board = [
        ["X", "X", "X"],
        ["O", "O", ""],
        ["", "", ""]
    ]
    assert minimax_tic_tac_toe(board, True) == 1
    assert minimax_tic_tac_toe(board, False) == 1

def test_terminal_o_win():
    board = [
        ["O", "O", "O"],
        ["X", "X", ""],
        ["", "", ""]
    ]
    assert minimax_tic_tac_toe(board, True) == -1
    assert minimax_tic_tac_toe(board, False) == -1

def test_terminal_draw():
    board = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"]
    ]
    assert minimax_tic_tac_toe(board, True) == 0
    assert minimax_tic_tac_toe(board, False) == 0

def test_o_best_draw():
    board = [
        ["", "", "X"],
        ["", "X", ""],
        ["O", "", ""]
    ]
    assert minimax_tic_tac_toe(board, False) == 0

def test_almost_empty():
    board = [
        ["", "", "X"],
        ["", "", ""],
        ["O", "", ""]
    ]
    assert minimax_tic_tac_toe(board, True) == 1
    assert minimax_tic_tac_toe(board, False) == -1
