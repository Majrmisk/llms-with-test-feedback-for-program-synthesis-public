from generated_function import can_measure

def test_target_zero():
    assert can_measure(3, 5, 0, 0) is True

def test_exact_capacity_jug2():
    assert can_measure(3, 5, 5, 1) is True

def test_exact_capacity_jug1():
    assert can_measure(3, 5, 3, 1) is True

def test_standard_case_sufficient_moves():
    assert can_measure(3, 5, 4, 6) is True

def test_standard_case_insufficient_moves():
    assert can_measure(3, 5, 4, 4) is False

def test_impossible_target():
    assert can_measure(3, 5, 9, 10) is False

def test_small_jugs_exact_measure():
    assert can_measure(1, 4, 3, 3) is True

def test_unsolvable_case():
    assert can_measure(2, 6, 5, 10) is False

def test_complex_possible():
    assert can_measure(8, 13, 7, 12) is True

def test_complex_insufficient_moves():
    assert can_measure(8, 13, 7, 11) is False
