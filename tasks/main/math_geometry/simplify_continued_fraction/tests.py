from generated_function import simplify_continued_fraction

def test_simplify_continued_fraction_1_2_2():
    assert simplify_continued_fraction([1,2,2]) == (7,5)

def test_simplify_continued_fraction_2_1_2():
    assert simplify_continued_fraction([2,1,2]) == (8,3)

def test_simplify_continued_fraction_3():
    assert simplify_continued_fraction([3]) == (3,1)

def test_simplify_continued_fraction_single_value():
    assert simplify_continued_fraction([4]) == (4,1)

def test_simplify_continued_fraction_4_1_1_1():
    assert simplify_continued_fraction([4,1,1,1]) == (14,3)
