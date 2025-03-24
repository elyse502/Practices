#!/usr/bin/python3

class Node:
    """Node class for linked list implementation."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """Append a new node to the linked list."""
        new_node = Node(value)
        # If the linked list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        pass

    def remove(self, value):
        pass

    def iterate(self):
        pass

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")    
            current = current.next
        print("None")


# Test the linked list implementation
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)

print(f"The head node value is: {linked_list.head.value}")
print(f"The tail node value is: {linked_list.tail.value}")
print(f"The next node value is: {linked_list.head.next.value}")
linked_list.display()