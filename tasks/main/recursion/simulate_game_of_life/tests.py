from generated_function import simulate_game_of_life

def test_empty_grid():
    initial = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    final = simulate_game_of_life(initial, 5)
    assert final == initial

def test_block_stable():
    initial = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    final = simulate_game_of_life(initial, 100)
    assert final == initial

def test_blinker_oscillator():
    initial = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    step1 = simulate_game_of_life(initial, 1)
    expected_step1 = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert step1 == expected_step1
    step2 = simulate_game_of_life(initial, 2)
    assert step2 == initial

def test_edge_cells():
    initial = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    expected = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    final = simulate_game_of_life(initial, 1)
    assert final == expected

def test_large():
    initial = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    expected = [
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0]
    ]
    final = simulate_game_of_life(initial, 8)
    assert final == expected

def test_input_not_mutated():
    initial = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    original = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    simulate_game_of_life(initial, 1)
    assert initial == original, "The function should not mutate the input grid"
