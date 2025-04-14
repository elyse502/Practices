#!/usr/bin/python3

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

    def remove_edge(self, node1, node2):
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1].remove(node2)
            self.adjacency_list[node2].remove(node1)

    def remove_node(self, node):
        if node in self.adjacency_list:
            # Remove the node from the adjacency lits of its neighbors.
            for neighbor in self.adjacency_list[node]:
                self.adjacency_list[neighbor].remove(node)
            # Remove the node itself.
            del self.adjacency_list[node]

    def display(self):
        # Display the adjacency list representation of the graph.
        for node, neighbors in self.adjacency_list.items():
            print(f">> {node}: {neighbors}")


class SocialNetwork:
    def __init__(self):
        self.graph = Graph()

    def add_user(self, user_name):
        self.graph.add_node(user_name)

    def add_friendship(self, user1, user2):
        self.graph.add_edge(user1, user2)

    def display_network(self):
        self.graph.display()


# Example usage:
social_network = SocialNetwork()

social_network.add_user("Alice")
social_network.add_user("Bob")
social_network.add_user("Charlie")
social_network.add_user("David")

social_network.add_friendship("Alice", "Bob")
social_network.add_friendship("Alice", "Charlie")
social_network.add_friendship("Bob", "Charlie")
social_network.add_friendship("Charlie", "David")

social_network.display_network()
