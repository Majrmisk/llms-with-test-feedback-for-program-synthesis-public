from generated_function import custom_regex_match


def test_literal_characters_match():
    assert custom_regex_match("hello", "hello") is True

def test_literal_characters_no_match():
    assert custom_regex_match("hello", "ello") is False

def test_wildcard_dot_match():
    assert custom_regex_match("abc", "a.c") is True

def test_wildcard_dot_no_match():
    assert custom_regex_match("abc", "a..c") is False

def test_kleene_star_match():
    assert custom_regex_match("abbbc", "ab*c") is True

def test_kleene_star_no_match():
    assert custom_regex_match("aabbbc", "ab*c") is False

def test_plus_quantifier_match():
    assert custom_regex_match("aaa", "a+") is True

def test_plus_quantifier_no_match():
    assert custom_regex_match("", "a+") is False

def test_question_mark_not_special():
    assert custom_regex_match("ac", "ab?c") is False

def test_no_special_characteers():
    assert custom_regex_match("a)aa[-][??", "a)aa[-][??") is True
