# Linked Lists
**Linked List** is a **collection of data elements** whose order is not given by their physical placement in memory, instead **each element points to the next**. In simple words a **linked list** is a `data structure` consisting of **nodes** where each **node** points to the next **node** in the sequence.

`Nodes` in **Linked List**, each node consists of two parts, the **data** the **link** that is pointing to the next node in the **linked list**. And the **link** in the last node is pointing to `null`, and the `head node` is always pointing to the `first node` in the **linked list**, and the `tail` is always pointing to the `last node`, and the `nodes` of the **linked list** are not stored in contiguous memory locations. That means they are randomly stored in the `memory`, and they are connected using the **links** in each `node`.

## Structure of a `Singly Linked List`

![Screenshot 2025-03-26 135334](https://github.com/user-attachments/assets/f17d17ce-abe3-487d-9d3d-409683a68a86)

<br />

## Time Complexity of `Singly Linked Lists` Operations
1. Insertion at the beginning (**prepend**): `O(1)`
2. Insertion at the end (**append**): `O(1)`
3. Insertion at a specific position: `O(n)`
4. Deletion from the beginning: `O(1)`
5. Deletion from the end: `O(1)`
6. Deletion from a specific position: `O(n)`
7. Searching for a specific element: `O(n)`

<br /><hr /><br />

# When to Use Linked Lists?
* Constant time insertions or deletions.
* Unknown number of items.
* Insertion in the middle.
