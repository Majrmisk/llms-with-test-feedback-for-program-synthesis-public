from generated_function import solve_n_queens

def test_n_queens_n1():
    solutions = solve_n_queens(1)
    assert solutions == [["Q"]]

def test_n_queens_n2():
    solutions = solve_n_queens(2)
    assert solutions == []

def test_n_queens_n3():
    solutions = solve_n_queens(3)
    assert solutions == []

def test_n_queens_n4():
    solutions = solve_n_queens(4)
    expected = [
        [".Q..",
         "...Q",
         "Q...",
         "..Q."],
        ["..Q.",
         "Q...",
         "...Q",
         ".Q.."]
    ]
    assert sorted(solutions) == sorted(expected)
