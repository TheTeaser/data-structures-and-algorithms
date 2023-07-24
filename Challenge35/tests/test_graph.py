from Challenge35.graph import Graph, business_trip
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

# CC37:
alaska_airlines_route_map = Graph()
alaska_airlines_route_map.add_vertex('Metroville')
alaska_airlines_route_map.add_vertex('Pandora')
alaska_airlines_route_map.add_vertex('Arendelle')
alaska_airlines_route_map.add_vertex('New Monstropolis')
alaska_airlines_route_map.add_vertex('Naboo')
alaska_airlines_route_map.add_vertex('Narnia')

alaska_airlines_route_map.add_edge('Metroville', 'Pandora', 82)
alaska_airlines_route_map.add_edge('Metroville', 'Arendelle', 99)
alaska_airlines_route_map.add_edge('Metroville', 'New Monstropolis', 105)
alaska_airlines_route_map.add_edge('Metroville', 'Naboo', 26)
alaska_airlines_route_map.add_edge('Metroville', 'Narnia', 37)

alaska_airlines_route_map.add_edge('Pandora', 'Metroville', 82)
alaska_airlines_route_map.add_edge('Pandora', 'Arendelle', 150)

alaska_airlines_route_map.add_edge('Arendelle', 'Pandora', 150)
alaska_airlines_route_map.add_edge('Arendelle', 'New Monstropolis', 42)
alaska_airlines_route_map.add_edge('Arendelle', 'Metroville', 99)

alaska_airlines_route_map.add_edge('New Monstropolis', 'Metroville', 105)
alaska_airlines_route_map.add_edge('New Monstropolis', 'Arendelle', 99)
alaska_airlines_route_map.add_edge('New Monstropolis', 'Naboo', 73)

alaska_airlines_route_map.add_edge('Naboo', 'Metroville', 26)
alaska_airlines_route_map.add_edge('Naboo', 'New Monstropolis', 73)
alaska_airlines_route_map.add_edge('Naboo', 'Narnia', 250)

alaska_airlines_route_map.add_edge('Narnia', 'Metroville', 37)
alaska_airlines_route_map.add_edge('Narnia', 'Naboo', 250)


# Test cases using pytest
def test_possible_trip():
    assert business_trip(alaska_airlines_route_map, ['Metroville', 'Pandora']) == 82
    assert business_trip(alaska_airlines_route_map, ['Arendelle', 'New Monstropolis', 'Naboo']) == 115

def test_impossible_trip():
    assert business_trip(alaska_airlines_route_map, ['Naboo', 'Pandora']) is None
    assert business_trip(alaska_airlines_route_map, ['Narnia', 'Arendelle', 'Naboo']) is None

def test_empty_trip():
    assert business_trip(alaska_airlines_route_map, []) == 0



# CC38:

def test_depth_first():
    graph = Graph()

    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_c = graph.add_vertex('C')
    vertex_d = graph.add_vertex('D')
    vertex_e = graph.add_vertex('E')

    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'E')

    # 1. Test depth-first traversal from vertex A
    traversal_order = graph.depth_first('A')
    assert traversal_order == ['A', 'B', 'C', 'E', 'D']

    # 2. Test depth-first traversal from vertex B
    traversal_order = graph.depth_first('B')
    assert traversal_order in (['B', 'D', 'C', 'E'], ['B', 'C', 'E', 'D'])

    # 3. Test depth-first traversal from non-existent vertex F
    traversal_order = graph.depth_first('F')
    assert traversal_order == []

