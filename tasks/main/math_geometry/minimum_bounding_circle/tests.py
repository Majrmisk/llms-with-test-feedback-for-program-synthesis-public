from generated_function import minimum_bounding_circle
import math

def test_single_point():
    points = [
        (1, 2)
    ]
    assert minimum_bounding_circle(points) == [0]

def test_two_points():
    points = [
        (0, 0),
        (0, 2)
    ]
    assert sorted(minimum_bounding_circle(points)) == [0, 1]

def test_triangle():
    points = [
        (0, 0),
        (2, 0),
        (1, math.sqrt(3))
    ]
    assert sorted(minimum_bounding_circle(points)) == [0, 1, 2]

def test_collinear_points():
    points = [
        (0, 0),
        (1, 0),
        (2, 0)
    ]
    assert sorted(minimum_bounding_circle(points)) == [0, 2], "The minimal circle should be defined by the two extreme endpoints"

def test_duplicate_points():
    points = [
        (0, 0),
        (0, 0),  # duplicate
        (2, 0)
    ]
    assert sorted(minimum_bounding_circle(points)) == [0, 3]

def test_duplicate_points():
    points = [
        (0, 0),
        (2, 0),    # interior
        (3, 0),
        (0, 0.5),  # interior
        (2, 1),    # interior
        (3, 1),    # interior
        (1, 2),    # interior
        (2, 2),    # interior
        (1, 2.5)
    ]
    assert sorted(minimum_bounding_circle(points)) == [0, 2, 8]
