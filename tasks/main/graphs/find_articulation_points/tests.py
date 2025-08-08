from generated_function import find_articulation_points

class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj = {i: [] for i in range(num_vertices)}
    def add_edge(self, u: int, v: int) -> None:
        self.adj[u].append(v)
        self.adj[v].append(u)

def test_empty_graph():
    graph = Graph(0)
    assert find_articulation_points(graph) == []

def test_one_vertex():
    graph = Graph(1)
    assert find_articulation_points(graph) == []

def test_isolated_vertices():
    graph = Graph(3)
    assert find_articulation_points(graph) == []

def test_star_graph():
    graph = Graph(5)
    for i in range(1, 5):
        graph.add_edge(0, i)
    assert sorted(find_articulation_points(graph)) == [0]

def test_chain_graph():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    assert sorted(find_articulation_points(graph)) == [1, 2]

def test_cycle_graph():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)
    assert sorted(find_articulation_points(graph)) == []

def test_disconnected_graph():
    graph = Graph(6)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    assert sorted(find_articulation_points(graph)) == [0, 4]

def test_large_graph():
    graph = Graph(7)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    assert sorted(find_articulation_points(graph)) == [3, 4]
