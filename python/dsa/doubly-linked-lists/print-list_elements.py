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
        pass

    def delete(self, data):
        pass

    def print_list(self):
        current_node = self.head
        print("\n\t", end="")
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

    def display(self):
        pass


# Test the doubly linked list implementation
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)

print(">> Doubly Linked List Elements:")
dll.print_list()
print(f"\n>> The head of the doubly linked list is: {dll.head.data}")
print(f">> The tail of the doubly linked list is: {dll.tail.data}")
print(f">> The next node of the head is: {dll.head.next.data}")
print(f">> The previous node of the tail is: {dll.tail.prev.data}")
print(f">> The next node of the tail is: {dll.tail.next}")
print(f">> The previous node of the head is: {dll.head.prev}")
