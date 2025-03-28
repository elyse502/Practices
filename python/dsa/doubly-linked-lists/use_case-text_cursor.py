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
        current_node = self.head
        print("\n\t", end="")
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


class CursorDLL(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.cursor = self.head

    def move_cursor_forward(self):
        if self.cursor is None or self.cursor.next is None:
            return
        self.cursor = self.cursor.next

    def move_cursor_backward(self):
        if self.cursor is None or self.cursor.prev is None:
            return
        self.cursor = self.cursor.prev

    def print_list_with_cursor(self):
        current_node = self.head
        while current_node:
            if current_node == self.cursor:
                print("[{}]".format(current_node.data), end=" ")
            else:
                print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def append(self, data):
        """This method is overridden to update the cursor 
        when appending a new node to the list"""
        super().append(data)
        if self.cursor is None:
            self.cursor = self.tail

    def prepend(self, data):
        """This method is overridden to update the cursor 
        when prepending a new node to the list"""
        super().prepend(data)
        if self.cursor is None:
            self.cursor = self.head

# Test the doubly linked list implementation with cursor
cursor_dll = CursorDLL()
cursor_dll.append('H')
cursor_dll.append('e')
cursor_dll.append('l')
cursor_dll.append('l')
cursor_dll.append('o')

print(">> Doubly Linked List Elements with Cursor:")
cursor_dll.print_list_with_cursor()

print("\n>> Moving cursor forward:")
cursor_dll.move_cursor_forward()
cursor_dll.print_list_with_cursor()
cursor_dll.move_cursor_forward()
cursor_dll.print_list_with_cursor()
cursor_dll.move_cursor_forward()
cursor_dll.print_list_with_cursor()
cursor_dll.move_cursor_forward()
cursor_dll.print_list_with_cursor()

print("\n>> Moving cursor backward:")
cursor_dll.move_cursor_backward()
cursor_dll.print_list_with_cursor()
cursor_dll.move_cursor_backward()
cursor_dll.print_list_with_cursor()
cursor_dll.move_cursor_backward()
cursor_dll.print_list_with_cursor()
cursor_dll.move_cursor_backward()
cursor_dll.print_list_with_cursor()
