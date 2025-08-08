from generated_function import in_place_merge

def test_empty_merge():
    arr = []
    in_place_merge(arr, 0, 0, 0)
    assert arr == []

def test_single_element_empty_first():
    arr = [5]
    in_place_merge(arr, 0, 0, 1)
    assert arr == [5]

def test_single_element_empty_second():
    arr = [5]
    in_place_merge(arr, 0, 1, 1)
    assert arr == [5]

def test_merge_two_sorted_halves():
    arr = [1, 3, 5, 2, 4, 6]
    in_place_merge(arr, 0, 3, 6)
    assert arr == [1, 2, 3, 4, 5, 6]

def test_merge_interleaved():
    arr = [2, 3, 6, 1, 4, 5, 7, 8, 9]
    in_place_merge(arr, 0, 3, 9)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_merge_entire_array():
    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    in_place_merge(arr, 0, 5, 10)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
