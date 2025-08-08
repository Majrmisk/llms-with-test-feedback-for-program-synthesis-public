from generated_function import collatz_steps_to_reach

def test_collatz_steps_same_start_and_target():
    assert collatz_steps_to_reach(5, 5) == 0

def test_collatz_steps_example_13_to_1():
    assert collatz_steps_to_reach(13, 1) == 9

def test_collatz_steps_simple_even():
    assert collatz_steps_to_reach(2, 1) == 1

def test_collatz_steps_simple_odd():
    assert collatz_steps_to_reach(3, 1) == 7

def test_collatz_steps_zero_never_reaches_one():
    assert collatz_steps_to_reach(0, 1) == -1

def test_collatz_steps_negative_start():
    assert collatz_steps_to_reach(-5, 1) == -1

def test_large_number_1000000():
    assert collatz_steps_to_reach(1000000, 1) == 152

def test_collatz_steps_other_target():
    assert collatz_steps_to_reach(7, 10) == 10

def test_large_number_837799():
    assert collatz_steps_to_reach(837799, 1) == 524

def test_collatz_steps_target_not_1_large():
    assert collatz_steps_to_reach(27, 40) == 103
