# Tree Traversal
**Tree traversal** refers to the process of visiting each `node` in a `tree data structure`, covering all the `nodes` in a `specific order`.

## Types of Tree Traversal Algorithms
* **Breadth First Search** (BFS): The `breadth first search algorithm` explores a `tree` level by level, starting from the `root` and moving horizontally across the `levels`.
* **Depth First Search** (DFS): The `depth first search` explores a `tree` by going as deep as possible along one `branch` before backtracking.

When it comes to **tree traversal**, `depth first search` is a very common `traversal algorithm`, and there are mainly 3 types of `depth first search` **tree traversal algorithms**:
1. **In-order traversal**: Visit the `left subtree` first, then visit the `root node`, then visit the `right subtree`.
2. **Pre-order traversal**: Visit the `root node` first, then visit the `left subtree`, then visit the `right subtree`.
3. **Post-order traversal**: Visit the `left subtree` first, then visit the `right subtree`, then visit the `root node`.

### Tree Traversal: `Inorder`
**Inorder traversal** is a **tree traversal algorithm** that recursively performs an `inorder traversal` on the `left subtree`, visits the `root node`, and finally performs an `inorder traversal` on the `right subtree`.

So to make it simpler, this **algorithm** visits the `nodes` in the `tree` in this order:

> left child -> root node -> right child

And that happens `recursively` for each `node` in the `tree`.

![Screenshot 2025-05-04 111451](https://github.com/user-attachments/assets/af037639-43f2-4fbe-ba1d-e16b2569dd08)

### Tree Traversal: `Preorder`
**Preorder traversal** is a **tree traversal algorithm** that visits the `root node` first, then `recursively` performs a `preorder traversal` on the `left subtree`, and finally on the `right subtree`.

So to make it simpler, this **algorithm** visits the `nodes` in the `tree` in this order:

> root node -> left child -> right child

And that happens `recursively` for each `node` in the `tree`.

![Screenshot 2025-05-04 122731](https://github.com/user-attachments/assets/ea79ecfd-cd68-4991-94a7-9eb53e8105ca)

### Tree Traversal: `Postorder`
**Postorder traversal** is a **tree traversal algorithm** that `recursively` performs a `postorder traversal` on the `left subtree`, then on the `right subtree`, and finally visits the `root node`.

So to make it simpler, this **algorithm** visits the `nodes` in the `tree` in this order:

> left child -> right child -> root node

And that happens `recursively` for each `node` in the `tree`.

![Screenshot 2025-05-04 130948](https://github.com/user-attachments/assets/e22c9252-1e4a-4d14-a7c0-05b5603c717d)

## Tree Traversal (inorder, preorder, postorder) Big O Notation
* **Time Complexity**: `O(n)` - as every `node` in the `tree` is visited once.
* **Space Complexity**: `O(h)` - where `h` is the **height** of the `tree`. This is because we use `recursion` for implementing those `algorithms`, and the `base case` for the `recursion` is when we try to visit a `null node`(a node that does not exist), and this case happens when we try to visit the children of a `leaf node`. So the maximum number of the `recursive` calls that will be in the `call stack`, or the `recursion stack` will be from the `topmost node` in the `tree` until a `leaf node` in the `tree`. And that is defined by the **height** of the `tree`.

