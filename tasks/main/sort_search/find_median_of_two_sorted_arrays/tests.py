from generated_function import find_median_of_two_sorted_arrays

def test_one_empty_array():
    assert find_median_of_two_sorted_arrays([1, 3, 5], []) == 3.0

def test_equal_length_even():
    assert find_median_of_two_sorted_arrays([1, 3], [2, 4]) == 2.5

def test_equal_length_odd():
    assert find_median_of_two_sorted_arrays([1, 2, 3], [4, 5, 6]) == 3.5

def test_different_lengths():
    assert find_median_of_two_sorted_arrays([1, 2], [3, 4, 5]) == 3.0

def test_both_single_element():
    assert find_median_of_two_sorted_arrays([2], [3]) == 2.5

def test_negative_numbers():
    assert find_median_of_two_sorted_arrays([-5, -3, -1], [2, 4, 6]) == 0.5

def test_complex():
    assert find_median_of_two_sorted_arrays([-19, -5, 1, 3, 6, 12], [-98, -5, -1, 0, 2, 4, 6, 9, 19, 100]) == 2.5

def test_complex_2():
    assert find_median_of_two_sorted_arrays([-10, -5, 0, 1, 1, 3, 7, 9], [-3, 2, 2, 4, 5, 10, 15, 20, 30]) == 3.0
