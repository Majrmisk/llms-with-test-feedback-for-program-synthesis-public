import math
from generated_function import dijkstra_shortest_paths

class GraphWeighted:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj = {i: [] for i in range(num_vertices)}
    def add_edge(self, u: int, v: int, weight: float) -> None:
        self.adj[u].append((v, weight))

def test_empty_graph():
    graph = GraphWeighted(0)
    assert dijkstra_shortest_paths(graph, 0) == []

def test_single_vertex():
    graph = GraphWeighted(1)
    assert dijkstra_shortest_paths(graph, 0) == [0]

def test_simple_graph():
    graph = GraphWeighted(2)
    graph.add_edge(0, 1, 5.0)
    assert dijkstra_shortest_paths(graph, 0) == [0, 5.0]

def test_unreachable_vertex():
    graph = GraphWeighted(3)
    graph.add_edge(0, 1, 10.0)
    assert dijkstra_shortest_paths(graph, 0) == [0, 10.0, math.inf]

def test_multiple_paths():
    graph = GraphWeighted(5)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 7)
    graph.add_edge(2, 4, 3)
    graph.add_edge(2, 3, 2)
    graph.add_edge(3, 4, 1)
    assert dijkstra_shortest_paths(graph, 0) == [0, 2, 3, 5, 6]

def test_cycle_non_negative():
    graph = GraphWeighted(4)
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 0, 1)
    graph.add_edge(2, 3, 1)
    assert dijkstra_shortest_paths(graph, 0) == [0, 1, 2, 3]

def test_complex_graph():
    graph = GraphWeighted(7)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 5)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 3)
    graph.add_edge(2, 3, 1)
    graph.add_edge(2, 4, 2)
    graph.add_edge(3, 4, 1)
    graph.add_edge(3, 5, 5)
    graph.add_edge(4, 5, 2)
    graph.add_edge(4, 6, 3)
    graph.add_edge(5, 6, 1)

    assert dijkstra_shortest_paths(graph, 0) == [0, 2, 3, 4, 5, 7, 8]
