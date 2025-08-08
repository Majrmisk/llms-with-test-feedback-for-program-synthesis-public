from generated_function import solve_linear_system
import pytest

def test_identity():
    matrix = [[1, 0], [0, 1]]
    b = [5, -3]
    assert solve_linear_system(matrix, b) == pytest.approx([5, -3], rel=1e-5)

def test_2x2():
    matrix = [[2, 1], [1, 3]]
    b = [5, 6]
    assert solve_linear_system(matrix, b) == pytest.approx([1.8, 1.4], rel=1e-5)

def test_3x3():
    matrix = [
        [3, 2, -1],
        [2, -2, 4],
        [-1, 0.5, -1]
    ]
    b = [1, -2, 0]
    assert solve_linear_system(matrix, b) == pytest.approx([1.0, -2.0, -2.0], rel=1e-5)

def test_singular_matrix():
    matrix = [[1, 2], [2, 4]]
    b = [3, 6]
    with pytest.raises(ValueError):
        solve_linear_system(matrix, b)

def test_near_singular():
    matrix = [[1, 2], [2, 4.001]]
    b = [3, 6.001]
    assert solve_linear_system(matrix, b) == pytest.approx([1.0, 1.0], rel=1e-5)

def test_4x4_solution():
    matrix = [
        [2, -1, 0, 3],
        [1, 0, 2, -1],
        [3, 2, -1, 1],
        [0, 1, 1, 2]
    ]
    b = [12, 3, 8, 13]
    assert solve_linear_system(matrix, b) == pytest.approx([1, 2, 3, 4], rel=1e-5)
