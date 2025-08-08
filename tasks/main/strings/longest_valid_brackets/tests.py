from generated_function import longest_valid_brackets

def test_empty_string():
    assert longest_valid_brackets("") == 0

def test_single_valid_pair():
    assert longest_valid_brackets("(adfa)") == 2, "Ignoring asfa, the longest valid brackets are () with the length of 2"

def test_nested_valid_pairs():
    assert longest_valid_brackets("({[]})") == 6, "All brackets should be supported"

def test_adjacent_valid_pairs():
    assert longest_valid_brackets("(asdf)dsf[asfd]") == 4

def test_unmatched_left_parenthesis():
    assert longest_valid_brackets("([]") == 2

def test_unmatched_right_parenthesis():
    assert longest_valid_brackets("{})") == 2

def test_mixed_validity():
    assert longest_valid_brackets(")()[](") == 4

def test_complex_nested():
    assert longest_valid_brackets("{()()}") == 6

def test_incomplete_segments():
    assert longest_valid_brackets("()(()") == 2

def test_valid_inside_invalid():
    assert longest_valid_brackets("]][asdf[fsd]safd]as][s[") == 4

def test_fully_nested():
    assert longest_valid_brackets("(a{sd(fsd)a}a(sd))") == 8

def test_multiple_segments():
    assert longest_valid_brackets("()   ((asdf  )dasf))()") == 6

def test_alternating_pattern():
    assert longest_valid_brackets("[]}{()}(){]") == 6

def test_long_valid_string():
    s = "s()" * 10000
    expected = 20000
    assert longest_valid_brackets(s) == expected

def test_long_invalid_string():
    assert longest_valid_brackets(1000 * "[" + ")" * 1000) == 0
