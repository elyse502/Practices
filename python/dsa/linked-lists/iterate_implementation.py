#!/usr/bin/python3

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
        iterator = self.head
        while iterator:
            print(iterator.value, end=" -> ")
            iterator = iterator.next
        print("None\n")


# Test the linked list implementation
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)

print(">> The linked list values are:")
linked_list.iterate()