from generated_function import kth_smallest_pair_sum

def test_small_array_k1():
    assert kth_smallest_pair_sum([1, 2, 3], 1) == 3

def test_small_array_k2():
    assert kth_smallest_pair_sum([1, 2, 3], 2) == 4

def test_small_array_k3():
    assert kth_smallest_pair_sum([1, 2, 3], 3) == 5

def test_duplicates():
    assert kth_smallest_pair_sum([1, 1, 2], 2) == 3

def test_negative_numbers():
    assert kth_smallest_pair_sum([-1, 2, 3], 2) == 2

def test_unsorted():
    assert kth_smallest_pair_sum([3, 1, 2], 1) == 3

def test_large_array():
    assert kth_smallest_pair_sum([8, 6, 10, 1, 5, 3, 7], 4) == 8

def test_many_duplicates():
    assert kth_smallest_pair_sum([2, 2, 3, 3, 4, 4], 10) == 6

def test_negatives_duplicates():
    assert kth_smallest_pair_sum([-10, -10, 0, 5, 5, 10], 10) == 5
