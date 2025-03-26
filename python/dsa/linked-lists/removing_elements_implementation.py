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
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return
        iterator = self.head
        while iterator.next:
            if iterator.next.value == value:
                iterator.next = iterator.next.next
                if not iterator.next:
                    self.tail = iterator
                return
            iterator = iterator.next

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

print(">> The linked list values before removing 30:")
linked_list.display()
print(">> The linked list values after removing 30:")
linked_list.remove(30)
linked_list.display()