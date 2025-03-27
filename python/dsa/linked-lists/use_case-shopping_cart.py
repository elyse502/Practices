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
        """Add a new node to the beginning of the linked list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        # If the linked list is empty
        if not self.tail:
            self.tail = new_node

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
        iterator = self.head
        while iterator:
            print("\t- " + iterator.value + " ")
            iterator = iterator.next


class ShoppingCart:
    def __init__(self):
        self.items = LinkedList()
    
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def display_cart(self):
        print(">> Items in the shopping cart:")
        self.items.iterate()


# Test the linked list user case implementation
cart = ShoppingCart()

# Add items to the shopping cart
cart.add_item("Shirt")
cart.add_item("Pants")
cart.add_item("Shoes")
cart.add_item("Socks")
cart.add_item("Hat")

# Display the items in the shopping cart
cart.display_cart()
print("\n")

# Remove an item from the shopping cart
cart.remove_item("Pants")

# Display the items in the shopping cart
cart.display_cart()