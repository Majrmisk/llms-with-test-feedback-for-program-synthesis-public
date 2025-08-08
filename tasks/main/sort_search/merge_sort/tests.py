from generated_function import merge_sort

def test_empty_list():
    assert merge_sort([]) == []

def test_single_element():
    assert merge_sort([42]) == [42]

def test_two_elements_unsorted():
    assert merge_sort([2, 1]) == [1, 2]

def test_two_elements_sorted():
    assert merge_sort([1, 2]) == [1, 2]

def test_multiple_elements():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_duplicates():
    assert merge_sort([5, 3, 3, 5, 2, 2, 1]) == [1, 2, 2, 3, 3, 5, 5]

def test_already_sorted():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_large_random_list():
    import random
    arr = [random.randint(0, 1000) for _ in range(1000)]
    assert merge_sort(arr) == sorted(arr)
