from generated_function import largest_strongly_connected_component

class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj = {i: [] for i in range(num_vertices)}
    def add_edge(self, u: int, v: int) -> None:
        self.adj[u].append(v)

def test_empty_graph():
    assert largest_strongly_connected_component(Graph(0)) == 0

def test_single_vertex():
    assert largest_strongly_connected_component(Graph(1)) == 1

def test_simple_cycle():
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    assert largest_strongly_connected_component(g) == 3

def test_multiple_sccs():
    g = Graph(6)
    # SCC1
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    # SCC2
    g.add_edge(3, 4)
    g.add_edge(4, 3)

    g.add_edge(5, 4)
    g.add_edge(2, 3)
    assert largest_strongly_connected_component(g) == 3

def test_multiple_same_size():
    g = Graph(6)
    # SCC1
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    # SCC2
    g.add_edge(3, 4)
    g.add_edge(4, 3)
    g.add_edge(4, 5)
    g.add_edge(5, 4)

    g.add_edge(2, 3)
    assert largest_strongly_connected_component(g) == 3

def test_complex_graph():
    g = Graph(9)
    # SCC1
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 0)
    g.add_edge(2, 4)
    g.add_edge(4, 0)
    g.add_edge(4, 1)

    # SCC2
    g.add_edge(5, 7)
    g.add_edge(7, 6)
    g.add_edge(6, 5)

    g.add_edge(3, 1)
    g.add_edge(3, 6)
    g.add_edge(3, 7)
    g.add_edge(5, 2)
    g.add_edge(8, 5)
    assert largest_strongly_connected_component(g) == 4
