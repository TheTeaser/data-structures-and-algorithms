from Challenge35.graph import Graph
import pytest

def test_graph():
    # Create a graph
    graph = Graph()

    # 1. Add vertices
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_c = graph.add_vertex('C')

    # 2. Test get_vertices method
    assert set(graph.get_vertices()) == {'A', 'B', 'C'}

    # 3. Add edges
    graph.add_edge('A', 'B', 10)
    graph.add_edge('B', 'C', 5)

    # 4. Test get_neighbors method
    assert graph.get_neighbors('A') == [('A', 'B', 10)]
    assert graph.get_neighbors('B') == [('B', 'C', 5)]
    assert graph.get_neighbors('C') == []

    # 5. Test size method
    assert graph.size() == 3

    # 6. Test graph with one vertex and edge
    single_vertex_graph = Graph()
    vertex_x = single_vertex_graph.add_vertex('X')
    single_vertex_graph.add_edge('X', 'X', 1)
    assert single_vertex_graph.get_vertices() == ['X']
    assert single_vertex_graph.get_neighbors('X') == [('X', 'X', 1)]
    assert single_vertex_graph.size() == 1

    # 7. Test adding edge with non-existent vertices
    with pytest.raises(ValueError):
        graph.add_edge('A', 'D')

    # 8. Test adding edge with non-existent vertices
    with pytest.raises(ValueError):
        graph.add_edge('D', 'B')
