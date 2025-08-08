from generated_function import solve_cryptarithmetic

def evaluate_puzzle(puzzle, mapping):
    left, right = puzzle.split("=")
    left_terms = left.split("+")
    def word_value(word):
        return int("".join(str(mapping[ch]) for ch in word))
    return sum(word_value(term) for term in left_terms), word_value(right)

def get_letters(puzzle):
    return {ch for ch in puzzle if ch.isalpha()}

def test_single_letter_terms():
    puzzle = "A+B=C"
    solution = solve_cryptarithmetic(puzzle)
    assert solution is not None, "No solution found"
    assert len(set(solution.values())) == len(solution.values()), "Digits are not unique"
    letters = get_letters(puzzle)
    assert set(solution.keys()) == letters, "Mapping must contain exactly the original letters."
    lhs, rhs = evaluate_puzzle(puzzle, solution)
    assert lhs == rhs

def test_trivial():
    puzzle = "A=A"
    solution = solve_cryptarithmetic(puzzle)
    assert solution is not None, "No solution found"
    assert len(set(solution.values())) == len(solution.values()), "Digits are not unique"
    assert set(solution.keys()) == {"A"}, "Mapping should only contain the letter A"
    lhs, rhs = evaluate_puzzle(puzzle, solution)
    assert lhs == rhs

def test_unsolvable():
    puzzle = "A+B=BA"
    solution = solve_cryptarithmetic(puzzle)
    assert solution is None, "Expected no solution"

def test_send_more_money():
    puzzle = "SEND+MORE=MONEY"
    solution = solve_cryptarithmetic(puzzle)
    assert solution is not None, "No solution found"
    letters = get_letters(puzzle)
    assert set(solution.keys()) == letters, "Mapping must contain exactly the original letters."
    assert len(set(solution.values())) == len(solution.values()), "Digits are not unique"
    for term in puzzle.replace("=", "+").split("+"):
        if len(term) > 1:
            assert solution[term[0]] != 0, f"Leading zero found in term {term}"
    lhs, rhs = evaluate_puzzle(puzzle, solution)
    assert lhs == rhs
