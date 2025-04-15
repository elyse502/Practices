#!/usr/bin/python3

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word
    
    def delete(self, word):
        node = self.root
        stack = []  # Stack to track the path
        for char in word:
            if char not in node.children:
                return  # Word doesn't exist
            # Push the node and char to the stack
            stack.append((node, char))
            node = node.children[char]

        if not node.is_word:
            return  # Word doesn't exist
        
        # Unmark the last node's `is_word` flag
        node.is_word = False

        # Now clean up the nodes from the stack (if needed)
        while stack:
            parent, char = stack.pop()

            # Check if the current node has any children or is marked as another word
            if not node.children and not node.is_word:
                # If no childred and it's not the end of another word, remove the child node
                del parent.children[char]
            else:
                # Stop the cleanup as soon as we find a node that can't be deleted
                break

            # Move back to the parent node for the next iteration
            node = parent

# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("cherry")

print(">> Search for 'apple':", trie.search("apple"))
print(">> Search for 'banana':", trie.search("banana"))
print(">> Search for 'cherry':", trie.search("cherry"))

trie.delete("apple")
print("\n>> Search for 'apple' after deletion:", trie.search("apple"))
trie.delete("banana")
print(">> Search for 'banana' after deletion:", trie.search("banana"))
trie.delete("cherry")
print(">> Search for 'cherry' after deletion:", trie.search("cherry"))
