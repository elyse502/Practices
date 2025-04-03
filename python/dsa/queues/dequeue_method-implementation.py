#!/usr/bin/python3

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
        
    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
        self.size += 1

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.front.value
            self.front = self.front.next
            self.size -= 1
            if self.is_empty():
                self.back = None
            return removed_item
        else:
            print("Queue is empty, cannot dequeue.")

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        # Collect elements in a list
        elements = []
        current = self.front
        while current:
            elements.append(current.value)
            current = current.next

        # Print in reversed order
        print("Back ->", " <- ".join(map(str, reversed(elements))), "<- Front")


# Example usage:
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(">> Queue contents:")
queue.display()
print()

print(">> Queue size:", queue.size)
print(">> First element:", queue.front.value)
print(">> Last element:", queue.back.value)
print("\n-----------------------------------------\n")

print(">> Dequeue:", queue.dequeue())
print(">> Queue contents after dequeue:")
queue.display()
print()

print(">> Is the queue empty?", queue.is_empty())
print()

print(">> Queue size:", queue.size)
print(">> First element:", queue.front.value)
print(">> Last element:", queue.back.value)
