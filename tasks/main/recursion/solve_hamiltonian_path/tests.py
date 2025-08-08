from generated_function import solve_hamiltonian_path

def is_valid_path(graph, path):
    n = len(graph)
    if len(path) != n or sorted(path) != list(range(n)):
        return False
    for i in range(n - 1):
        if graph[path[i]][path[i + 1]] == 0:
            return False
    return True

def test_empty_graph():
    assert solve_hamiltonian_path([]) == []

def test_single_vertex():
    assert solve_hamiltonian_path([[0]]) == [0]

def test_two_vertices():
    graph = [
        [0, 1],
        [1, 0]
    ]
    assert is_valid_path(graph, solve_hamiltonian_path(graph))

def test_line_graph_3():
    graph = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    assert is_valid_path(graph, solve_hamiltonian_path(graph))

def test_disconnected_graph():
    graph = [
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]
    assert solve_hamiltonian_path(graph) == []

def test_complete_graph_4():
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0]
    ]
    assert is_valid_path(graph, solve_hamiltonian_path(graph))

def test_cycle_graph_4():
    graph = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    assert is_valid_path(graph, solve_hamiltonian_path(graph))

def test_bipartite_k_2_4_no_path():
    graph = [
        [0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0]
    ]
    assert solve_hamiltonian_path(graph) == []

def test_complex():
    graph = [
        [0, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0]
    ]
    assert is_valid_path(graph, solve_hamiltonian_path(graph))
