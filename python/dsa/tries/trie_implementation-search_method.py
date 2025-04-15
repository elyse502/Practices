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

# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("cherry")

print(">> Search for 'apple':", trie.search("apple"))
print(">> Search for 'orange':", trie.search("orange"))
print(">> Search for 'banana':", trie.search("banana"))
print(">> Search for 'grape':", trie.search("grape"))
print(">> Search for 'cherry':", trie.search("cherry"))

print("\n>> Search for 'app' prefix of 'apple' inserted but not itself:", trie.search("app"))
trie.insert("app")
print(">> Search for 'app' after inserting it:", trie.search("app"))
