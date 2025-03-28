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
        if not self.head:  # Case: Empty List
            return
        
        if self.head.data == data:  # Case: Deleting Head
            self.head = self.head.next
            if self.head:  
                self.head.prev = None
            else:  # If the list is now empty, reset tail
                self.tail = None
            return

        current = self.head
        while current:
            if current.data == data:
                if current.next:  # Case: Deleting a Middle Node
                    current.next.prev = current.prev
                else:  # Case: Deleting Tail
                    self.tail = current.prev
                
                if current.prev:  # Adjust previous node's next pointer
                    current.prev.next = current.next
                return
            
            current = current.next

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
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
print(">> Initial List:")
dll.display()
print("\n-----------------------------------------\n")

print(">> The list after deleting 20:")
dll.delete(20)
dll.display()
print("\n-----------------------------------------\n")

print(">> The list after deleting 10 (Head):")
dll.delete(10)
dll.display()
print("\n-----------------------------------------\n")

print(">> The list after deleting 50 (Tail):")
dll.delete(50)
dll.display()
