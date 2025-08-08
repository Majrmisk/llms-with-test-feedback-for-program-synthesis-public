from typing import Dict
from generated_function import chromatic_number

class Graph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj = {i: [] for i in range(num_vertices)}
    def add_edge(self, u: int, v: int) -> None:
        self.adj[u].append(v)
        self.adj[v].append(u)

def test_empty_graph():
    g = Graph(0)
    assert chromatic_number(g) == 0

def test_four_vertices_no_edge():
    g = Graph(4)
    assert chromatic_number(g) == 1

def test_two_vertices_with_edge():
    g = Graph(2)
    g.add_edge(0, 1)
    assert chromatic_number(g) == 2

def test_star_graph():
    g = Graph(5)
    for leaf in range(1, 5):
        g.add_edge(0, leaf)
    assert chromatic_number(g) == 2

def test_complete_graph():
    n = 4
    g = Graph(n)
    for i in range(n):
        for j in range(i+1, n):
            g.add_edge(i, j)
    assert chromatic_number(g) == 4

def test_cycle_odd():
    n = 5
    g = Graph(n)
    for i in range(n):
        g.add_edge(i, (i+1) % n)
    assert chromatic_number(g) == 3

def test_cycle_even():
    n = 6
    g = Graph(n)
    for i in range(n):
        g.add_edge(i, (i+1) % n)
    assert chromatic_number(g) == 2

def test_complex_graph():
    g = Graph(9)
    g.add_edge(0, 2)
    g.add_edge(1, 0)
    g.add_edge(2, 4)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(7, 6)
    g.add_edge(6, 5)
    g.add_edge(3, 7)
    g.add_edge(5, 2)
    g.add_edge(8, 5)
    assert chromatic_number(g) == 3
