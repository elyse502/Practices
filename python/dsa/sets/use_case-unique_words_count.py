#!/usr/bin/python3

def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

# Example usage
text_input = ("Python is a high-level programming language. "
              "Python's simplicity and flexibility make it a popular programming language. "
              "Learning Python is essential for mastering web development, data science, and automation tasks.")
print(">> Original text:", text_input)
print()
print(">> Splitting the text into words:", text_input.split())
print()
print(">> Creating a set of unique words:", set(text_input.split()))
print()
print(">> The number of unique words in the text is:", len(set(text_input.split())))
print("\n", "_" * 50, "\n\n")

# Using the function to count unique words
print(">> Using a function to count unique words:")
unique_words_count = count_unique_words(text_input)
print("\t- The number of unique words in the text is:", unique_words_count)
