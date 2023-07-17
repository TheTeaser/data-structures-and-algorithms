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

#CC36:

def test_breadth_first():
    # Create a graph
    graph = Graph()

    # Add vertices
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_c = graph.add_vertex('C')
    vertex_d = graph.add_vertex('D')
    vertex_e = graph.add_vertex('E')

    # Add edges
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'E')

    # 1. Test breadth-first traversal from vertex A
    traversal_order = graph.breadth_first('A')
    assert traversal_order == ['A', 'B', 'C', 'D', 'E']

    # 2. Test breadth-first traversal from vertex B
    traversal_order = graph.breadth_first('B')
    assert traversal_order == ['B', 'C', 'D', 'E']

    # 3. Test breadth-first traversal from vertex E
    traversal_order = graph.breadth_first('E')
    assert traversal_order == ['E']

