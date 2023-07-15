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
