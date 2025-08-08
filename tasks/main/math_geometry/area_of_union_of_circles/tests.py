import math
import pytest
from generated_function import area_of_union_of_circles

def test_empty_list():
    assert area_of_union_of_circles([]) == pytest.approx(0.0, rel=0.1)

def test_single_circle():
    assert area_of_union_of_circles([(0, 0, 1)]) == pytest.approx(math.pi, rel=0.1)

def test_two_non_overlapping():
    assert area_of_union_of_circles([(0, 0, 1), (10, 10, 1)]) == pytest.approx(2 * math.pi, rel=0.1)

def test_two_overlapping():
    intersection_area = (2 * math.acos(0.5)) - 0.5 * math.sqrt(3)
    expected = 2 * math.pi - intersection_area
    assert area_of_union_of_circles([(0, 0, 1), (1, 0, 1)]) == pytest.approx(expected, rel=0.1)

def test_coincident_circles():
    assert area_of_union_of_circles([(0, 0, 1), (0, 0, 1)]) == pytest.approx(math.pi, rel=0.1)

def test_three_tangent_circles():
    circles = [(0, 0, 1), (2, 0, 1), (1, math.sqrt(3), 1)]
    expected = 3 * math.pi
    assert area_of_union_of_circles(circles) == pytest.approx(expected, rel=0.1)

def test_three_in_line():
    overlap_area = (2 * math.acos(0.5)) - 0.5 * math.sqrt(3)
    expected = 3 * math.pi - 2 * overlap_area
    circles = [(0, 0, 1), (1, 0, 1), (2, 0, 1)]
    assert area_of_union_of_circles(circles) == pytest.approx(expected, rel=0.1)

def test_two_overlapping_and_one_far():
    overlap_area = (2 * math.acos(0.5)) - 0.5 * math.sqrt(3)
    expected = (2 * math.pi - overlap_area) + math.pi
    circles = [(0, 0, 1), (1, 0, 1), (5, 5, 1)]
    assert area_of_union_of_circles(circles) == pytest.approx(expected, rel=0.1)
