from generated_function import check_graph_isomorphism

class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj = {i: [] for i in range(num_vertices)}

    def add_edge(self, u: int, v: int) -> None:
        self.adj[u].append(v)
        self.adj[v].append(u)

def test_empty_graphs():
    g1 = Graph(0)
    g2 = Graph(0)
    assert check_graph_isomorphism(g1, g2) is True

def test_single_vertex_graphs():
    g1 = Graph(1)
    g2 = Graph(1)
    assert check_graph_isomorphism(g1, g2) is True

def test_different_vertex_graphs():
    g1 = Graph(1)
    g2 = Graph(0)
    assert check_graph_isomorphism(g1, g2) is False

def test_identical_graphs():
    g1 = Graph(3)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)

    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    assert check_graph_isomorphism(g1, g2) is True

def test_isomorphic_graphs_different_order():
    g1 = Graph(3)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 0)

    g2 = Graph(3)
    g2.add_edge(0, 2)
    g2.add_edge(2, 1)
    g2.add_edge(1, 0)

    assert check_graph_isomorphism(g1, g2) is True

def test_non_isomorphic_graphs():
    g1 = Graph(3)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 0)

    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    assert check_graph_isomorphism(g1, g2) is False

def test_complex_isomorphic():
    g1 = Graph(9)
    g1.add_edge(0, 2)
    g1.add_edge(1, 2)
    g1.add_edge(1, 0)
    g1.add_edge(7, 6)
    g1.add_edge(6, 5)
    g1.add_edge(3, 1)
    g1.add_edge(5, 2)
    g1.add_edge(8, 5)

    g2 = Graph(9)
    g2.add_edge(6, 5)
    g2.add_edge(8, 5)
    g2.add_edge(8, 6)
    g2.add_edge(7, 0)
    g2.add_edge(0, 2)
    g2.add_edge(3, 8)
    g2.add_edge(2, 5)
    g2.add_edge(1, 2)

    assert check_graph_isomorphism(g1, g2) is True

def test_complex_not_isomorphic():
    g1 = Graph(9)
    g1.add_edge(0, 2)
    g1.add_edge(1, 2)
    g1.add_edge(1, 0)
    g1.add_edge(7, 6)
    g1.add_edge(6, 5)
    g1.add_edge(3, 1)
    g1.add_edge(5, 2)
    g1.add_edge(8, 5)

    g2 = Graph(9)
    g2.add_edge(6, 5)
    g2.add_edge(8, 5)
    g2.add_edge(8, 4)
    g2.add_edge(7, 0)
    g2.add_edge(0, 2)
    g2.add_edge(3, 8)
    g2.add_edge(2, 5)
    g2.add_edge(1, 2)

    assert check_graph_isomorphism(g1, g2) is False
