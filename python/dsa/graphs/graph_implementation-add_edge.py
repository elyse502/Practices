class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list.
        self.adjacency_list = {}

    def add_node(self, node):
        # Add a new node to the graph.
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        # Add an undirected edge between node1 and node2.
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def display(self):
        pass
    