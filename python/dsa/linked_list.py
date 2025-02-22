#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the node
        self.next = None  # The reference to the next node (initially None)


class LinkedList:
    def __init__(self):
        self.head = None  # The head is the starting node of the list

    def append(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:
            self.head = new_node  # If the list is empty, make this the first node
            return

        # Otherwise, traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node  # Link the last node to the new node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")    
            current = current.next
        print("None")

    def delete(self, data):
        if not self.head:
            return  # The list is empty
        if self.head.data == data:
            self.head = self.head.next  # Remove the head node
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next  # Skip the node to delete


# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
ll.delete(20)
ll.display()