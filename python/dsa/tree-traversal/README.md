# Tree Traversal
**Tree traversal** refers to the process of visiting each `node` in a `tree data structure`, covering all the `nodes` in a `specific order`.

## Types of Tree Traversal Algorithms
* **Breadth First Search** (BFS): The `breadth first search algorithm` explores a `tree` level by level, starting from the `root` and moving horizontally across the `levels`.
* **Depth First Search** (DFS): The `depth first search` explores a `tree` by going as deep as possible along one `branch` before backtracking.

When it comes to **tree traversal**, `depth first search` is a very common `traversal algorithm`, and there are mainly 3 types of `depth first search` **tree traversal algorithms**:
1. **In-order traversal**: Visit the `left subtree` first, then visit the `root node`, then visit the `right subtree`.
2. **Pre-order traversal**: Visit the `root node` first, then visit the `left subtree`, then visit the `right subtree`.
3. **Post-order traversal**: Visit the `left subtree` first, then visit the `right subtree`, then visit the `root node`.

### Tree Traversal: Inorder
**Inorder traversal** is a **tree traversal algorithm** that recursively performs an `inorder traversal` on the `left subtree`, visits the `root node`, and finally performs an `inorder traversal` on the `right subtree`.

So to make it simpler, this **algorithm** visits the `nodes` in the `tree` in this order:

> left child -> root node -> right child

And that happens `recursively` for each `node` in the `tree`.

![Screenshot 2025-05-04 111451](https://github.com/user-attachments/assets/af037639-43f2-4fbe-ba1d-e16b2569dd08)

### Tree Traversal: Preorder
**Preorder traversal** is a **tree traversal algorithm** that visits the `root node` first, then `recursively` performs a `preorder traversal` on the `left subtree`, and finally on the `right subtree`.

So to make it simpler, this **algorithm** visits the `nodes` in the `tree` in this order:

> root node -> left child -> right child

And that happens `recursively` for each `node` in the `tree`.





