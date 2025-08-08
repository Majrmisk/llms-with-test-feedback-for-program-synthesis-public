from generated_function import compute_convex_hull

def test_single_point():
    points = [
        (1, 1)
    ]
    assert compute_convex_hull(points) == [0]

def test_two_points():
    points = [
        (1, 2),
        (3, 4)
    ]
    assert compute_convex_hull(points) == [0, 1]

def test_triangle():
    points = [
        (1, 0),
        (0, 1),
        (0, 0)
    ]
    assert compute_convex_hull(points) == [2, 0, 1]

def test_collinear_points():
    points = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3)
    ]
    assert compute_convex_hull(points) == [0, 3], "For collinear points, only the two extreme endpoints are expected."

def test_duplicate_points():
    points = [
        (0, 0),
        (1, 1),
        (0, 0),  # duplicate
        (1, 0),
        (0, 1)
    ]
    assert compute_convex_hull(points) == [0, 3, 1, 4], "Expected unique extreme points."

def test_interior_point():
    points = [
        (0, 0),
        (2, 0),
        (1, 0.5),  # interior
        (2, 2),
        (0, 2)
    ]
    assert compute_convex_hull(points) == [0, 1, 3, 4]

def test_multiple_interior_points():
    points = [
        (0, 0),
        (2, 0),
        (1, 1),  # interior
        (2, 2),
        (0, 2),
        (1, 2),  # interior
        (2, 1)   # interior
    ]
    assert compute_convex_hull(points) == [0, 1, 3, 4]

def test_complex_shape():
    points = [
        (2, -1),
        (0, 0),
        (2, 0),  # interior
        (4, 0),
        (1, 2),  # interior
        (3, 2),  # interior
        (5, 2),
        (-1, 3),
        (0, 3),  # interior
        (2, 3),  # interior
        (2, 4),
        (4, 4)
    ]
    assert compute_convex_hull(points) == [7, 1, 0, 3, 6, 11, 10]
