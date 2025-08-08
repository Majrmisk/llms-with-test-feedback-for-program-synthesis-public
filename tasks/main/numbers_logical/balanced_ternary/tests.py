from generated_function import balanced_ternary

def test_balanced_ternary_zero():
    assert balanced_ternary(0) == "0"

def test_balanced_ternary_positive_1():
    assert balanced_ternary(1) == "+"

def test_balanced_ternary_negative_1():
    assert balanced_ternary(-1) == "-"

def test_balanced_ternary_two():
    assert balanced_ternary(2) == "+-"

def test_balanced_ternary_negative_two():
    assert balanced_ternary(-2) == "-+"

def test_balanced_ternary_five():
    assert balanced_ternary(5) == "+--"

def test_balanced_ternary_negative_four():
    assert balanced_ternary(-4) == "--"

def test_balanced_ternary_nine():
    assert balanced_ternary(9) == "+00"

def test_balanced_ternary_negative_nine():
    assert balanced_ternary(-9) == "-00"

def test_balanced_ternary_42():
    assert balanced_ternary(42) == "+---0"

def test_balanced_ternary_negative_152():
    assert balanced_ternary(-153242) == "-0++-0-+0+0+"
