from generated_function import resolution_prover

def test_empty_clause_set():
    clauses = []
    assert resolution_prover(clauses) is False

def test_simple_unsatisfiable():
    clauses = [["P"], ["~P"]]
    assert resolution_prover(clauses) is True

def test_simple_satisfiable():
    clauses = [["P", "Q"], ["~P"]]
    assert resolution_prover(clauses) is False

def test_complex_unsatisfiable():
    clauses = [["P", "Q"], ["~P", "R"], ["~Q"], ["~R"]]
    assert resolution_prover(clauses) is True

def test_complex_satisfiable():
    clauses = [["P", "Q"], ["~P", "R"], ["~Q", "S"], ["~R", "~S"]]
    assert resolution_prover(clauses) is False
