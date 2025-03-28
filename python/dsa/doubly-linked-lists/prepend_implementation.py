#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        pass

    def print_list(self):
        pass

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Test the doubly linked list implementation
dll = DoublyLinkedList()

# When the list is empty
dll.prepend(0)

dll.display()
print(f"\n>> The head of the doubly linked list is: {dll.head.data}")
print(f">> The tail of the doubly linked list is: {dll.tail.data}")

print("\n-------------------------------------------------\n")
# When the list is not empty
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

dll.prepend(-1)
dll.display()
print(f"\n>> The head of the doubly linked list is: {dll.head.data}")
print(f">> The tail of the doubly linked list is: {dll.tail.data}")
print(f">> The next node of the head is: {dll.head.next.data}")
print(f">> The previous node of the tail is: {dll.tail.prev.data}")
