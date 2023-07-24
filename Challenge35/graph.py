class Graph:
    def __init__(self):
        """
        Initialize an empty graph.
        """
        self.vertices = {}

    def add_vertex(self, value):
        """
        Add a vertex to the graph.
        """
        self.vertices[value] = []
        return value

    def add_edge(self, vertex1, vertex2, weight=None):
        """
        Add a new edge between two vertices in the graph.
        """
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise ValueError("Both vertices should already be in the graph")
        edge = (vertex1, vertex2, weight)
        self.vertices[vertex1].append(edge)

    def get_vertices(self):
        """
        Get all vertices in the graph.
        """
        return list(self.vertices.keys())

    def get_neighbors(self, vertex):
        """
        Get the neighbors of a given vertex in the graph.
        """
        if vertex in self.vertices:
            return self.vertices[vertex]
        return []

    def size(self):
        """
        Get the total number of vertices in the graph.
        """
        return len(self.vertices)

    #CC36:

    def breadth_first(self, node):
        """
        Traverses the graph based on the breadth-first algorithm starting from the given node.
        """
        all_vertices = []
        visiting_queue = [node]
        visited_vertices = set()
        visited_vertices.add(node)

        while visiting_queue:
            current_node = visiting_queue.pop(0)
            all_vertices.append(current_node)

            for neighbor in self.get_neighbors(current_node):
                neighbor_node = neighbor[1]
                if neighbor_node not in visited_vertices:
                    visited_vertices.add(neighbor_node)
                    visiting_queue.append(neighbor_node)

        return all_vertices
    
    # CC38:

    def depth_first(self, node):
        """
        Traverses the graph based on the depth-first algorithm starting from the given node.
        """
        if node not in self.vertices:
            return []

        all_vertices = []
        visited_nodes = set()

        def traverse(current_node):
            visited_nodes.add(current_node)
            all_vertices.append(current_node)

            for neighbor in self.get_neighbors(current_node):
                neighbor_node = neighbor[1]
                if neighbor_node not in visited_nodes:
                    traverse(neighbor_node)

        traverse(node)
        return all_vertices


    # CC37:

def has_direct_flight(graph, src, dest):
    """
    Check if there is a direct flight from the departure city to the destination city.
    """
    return any(dest == neighbor[1] for neighbor in graph.get_neighbors(src))

def calculate_trip_cost(graph, cities):
    """
    Calculate the total cost of a trip based on the route and the airline route map.
    """
    total_cost = 0
    for i in range(len(cities) - 1):
        src = cities[i]
        dest = cities[i + 1]
        if not has_direct_flight(graph, src, dest):
            return None
        for neighbor in graph.get_neighbors(src):
            if neighbor[1] == dest:
                total_cost += neighbor[2]
                break
    return total_cost

def business_trip(graph, city_names):
    """
    Determine if the trip is possible with direct flights and calculate the total trip cost.
    """
    return calculate_trip_cost(graph, city_names)

    

        