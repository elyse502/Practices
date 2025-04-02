#!/usr/bin/python3
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        pass
    def is_empty(self):
        pass

    def display(self):
        current = self.top
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def get_bottom(self):
        if not self.top:  # Stack is empty
            return None
        
        current = self.top
        while current.next:  # Move to the bottom node
            current = current.next
        return current.value  # Return the first added element


# Create a stack and add elements
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Display the stack
stack.display()
print("\n>> Top element:", stack.top.value if stack.top else "Stack is empty")
print(">> The next element:", stack.top.next.value if stack.top and stack.top.next else "No next element")
print(">> First element added:", stack.get_bottom())
