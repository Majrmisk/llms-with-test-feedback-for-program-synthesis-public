from typing import List, Tuple
from generated_function import solve_8_puzzle

def apply_moves(initial_state: List[List[int]], moves: List[str]) -> List[List[int]]:
    board = [row[:] for row in initial_state]

    def find_blank(board: List[List[int]]) -> Tuple[int, int]:
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    return i, j
        raise ValueError("Blank (0) not found on the board.")

    for move in moves:
        i, j = find_blank(board)
        if move == "up":
            ni, nj = i - 1, j
        elif move == "down":
            ni, nj = i + 1, j
        elif move == "left":
            ni, nj = i, j - 1
        elif move == "right":
            ni, nj = i, j + 1
        else:
            raise ValueError(f"Invalid move: {move}")
        if not (0 <= ni < 3 and 0 <= nj < 3):
            raise ValueError(f"Move {move} moves blank out of bounds.")
        board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
    return board

def test_already_solved():
    solved_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    moves = solve_8_puzzle(solved_board)
    assert moves == []

def test_simple_solvable():
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]
    ]
    moves = solve_8_puzzle(board)
    # Applying the returned moves
    final_board = apply_moves(board, moves)
    expected = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    assert final_board == expected

def test_unsolvable():
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [8, 7, 0]
    ]
    moves = solve_8_puzzle(board)
    assert moves is None

def test_complex_solvable():
    board = [
        [7, 2, 4],
        [5, 0, 6],
        [8, 3, 1]
    ]
    moves = solve_8_puzzle(board)
    assert moves is not None
    # Applying the returned moves
    final_board = apply_moves(board, moves)
    expected = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    assert final_board == expected
