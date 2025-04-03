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

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass


# Example usage:
queue = Queue()
print(">> Is the queue empty?", queue.is_empty())
