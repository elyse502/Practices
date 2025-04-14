class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list.
        self.adjacency_list = {}

    def add_node(self, node):
        # Add a new node to the graph.
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        pass

    def display(self):
        pass
    