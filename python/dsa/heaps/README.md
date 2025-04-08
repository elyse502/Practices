# Heaps
**Heaps** are complete **binary tree** based **data structures** that are used to maintain the largest or the smallest **element** in a data set.

There are two types of **heaps**:
* `max heap`: the `max heap` maintains the largest **element** in a data set.
    * The `node` at the top is the maximum or the largest **element** in the `heap`, and the value of each `node` in the max `heap` is greater than or equal to the values of its children. And in `heaps` it's okay to have duplicate **elements**, unlike **`binary search trees`**.

![Screenshot 2025-04-08 190848](https://github.com/user-attachments/assets/2a8dda0c-980e-4cae-bd6e-71ba1eeac0a3)

* `min heap`: the `min heap` maintains the smallest **element** in a data set.
    * The `node` at the top is the `node` with the smallest value in the `heap`, and the children in each `node` are greater than their parent, so it's basically the opposite of the `maximum heap`.

![Screenshot 2025-04-08 192847](https://github.com/user-attachments/assets/5b8341a6-9df7-4d06-8c82-7a5207e4c80b)

The order of the `nodes` doesn't matter in the `max heap` or in the `min heap`. Unlike **`binary search trees`**, where all the `nodes` in the **left** subtree are less and all the `nodes` in the **right** subtree are greater.

**N.B**: `heaps` are not good for searching, they are only good in keeping track of the **minimum** or the **maximum** value in a data set. And heaps are **complete binary trees**, and we saw that **binary trees** are **trees** in which each `node` has maximum two children, and a **complete tree** is a **tree** in which all the levels are completely filled from left to right, so there should not be any gaps in between the `nodes` in each level.


