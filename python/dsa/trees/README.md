# Trees
A **tree** in computer science is a data structure that represents a **hierarchical tree structure** with a set of **connected nodes**. It mainly consists of `nodes` and **edges** that connect those `nodes`.

* In **trees**, `nodes` are connected in **`parent-child`** relationships.

![Screenshot 2025-04-06 065022](https://github.com/user-attachments/assets/b7982364-f734-4e69-9bde-7151b6c52bf6)


* The `topmost` node in the **tree** is called the **root node**. And any `node` with no **children** is called a **leaf node**.

![Screenshot 2025-04-06 065639](https://github.com/user-attachments/assets/d1975be5-dac9-4722-889b-d7929366e94a)

**Trees** are very common in computer science and used in many applications such as **file systems**.

<br /><hr /><br />

## Binary Trees
**Binary trees** are **trees** in which each `node` has at most **two children**, a **left child** and a **right child**. Each `node` can have zero, one or two children.

![Screenshot 2025-04-06 071251](https://github.com/user-attachments/assets/25e732c2-8436-43f2-9e5d-f0e720922d3f)

### Properties of Binary Trees
* The **height** of the **tree** is the length of the longest path from the **root** to a **leaf** node, and the **depth** of any `node` in the **tree** is the level at which the `nodes` resides.

![Screenshot 2025-04-06 071537](https://github.com/user-attachments/assets/c0e016fc-f1b9-4774-b12b-ed0dc85f0041)

### There are two types of **binary trees**:
* **Balanced trees**: a **balanced tree** is a **tree** in which the **height** of the **left** and **right** subtrees of any `node` differs by at most one. Let's take a look at the **height** of the **left** and **right** subtrees of the following **root node**. The **height** of the **left** subtree is one, and the **height** of the **right** subtree is zero, and as yo can see, the difference between them is one. And if we recursively keep doing that for all the `nodes` in this **tree**, we should have the same result. If the difference is more than one for any `node` or any subtrees of a `node`, then it's **`unbalanced`**.
    
![Screenshot 2025-04-06 072548](https://github.com/user-attachments/assets/2a16ec28-ed01-4bc9-921e-87ea03886c70)

* **Unbalanced trees**: let's see an example of an **unbalanced tree**.

![Screenshot 2025-04-06 073222](https://github.com/user-attachments/assets/789d8514-2bfd-44e3-9302-73ad08531565)

So this **tree** is **unbalanced** because the **left** subtree has a **height** of two and the right subtree has **height** zero. So the difference here is two which is more than one, and that means that this **tree** is **unbalanced**.

* **Binary search trees** are one of the popular use cases of **binary trees**.

## Complete Binary Trees
A **complete binary tree** is a special type of a **binary tree**, where the levels except possibly last are completely filled and all `nodes` are as **left** as possible. So that means if we are constructing a **complete binary tree**, we have to fill the `nodes` from **left** to **right** in each level, leaving no gaps in the **sequence**.

And there is an exception for the last level of the **complete binary tree**, it can be not completely filled, but the gaps should be at the **right**, so we should always fill the `nodes` from the **left** in each level.

Let's take a look at some **complete binary trees**:

![Screenshot 2025-04-08 064056](https://github.com/user-attachments/assets/8fcdbb2f-db2d-41f4-8312-57ad6523590a)

So the above two **trees** are valid **complete binary trees**.
* In the first one, all the levels are completely filled with `nodes`.
* In the second one, the levels are completely filled except for the last level. But as we saw, this is okay as long as there are no gaps on the **left** side. So since the gap there is on the **right** side, that should be fine.

Let's take a look at some examples of **incomplete binary trees**:

![Screenshot 2025-04-08 065726](https://github.com/user-attachments/assets/5dadea26-2450-4572-b8ae-b2459f3e14cc)

* So in the first one, in the last level the `nodes` are not as **left** as possible. There is a gap in the middle there, and that violates the rule of a **complete binary tree**.
* In the second one also has a gap on the **left**, and that makes it an **incomplete binary tree**.

**Binary trees** are used to implement **heaps**.

## Binary Search Trees
A **binarry search tree** is a special type of **binary tree**, in which all the `nodes` are ordered in such a way that for every `node`, all the nodes in its **left** subtree are less than its value, and all the `nodes` in its **right** subtree are greater than its value.

The following is an example of a **binary search tree**:

![Screenshot 2025-04-08 083211](https://github.com/user-attachments/assets/a5f0f40f-ef66-4937-b792-7c075cfebeec)

* The **root node** there is `10` and as you can see, all the nodes in its **left** subtree are less than its value, and all the `nodes` in its **right** subtree are greater than its value. And this applies to each `node` in the **binary search tree**. If we go through them, as you can see `5` has `3` as a **left child**, which is less than `5`, and `8` as a **right child**, which is greater than `5`. And the `15` has `12` as a **left child**, which is less than `15`, and `20` as a **right child**, which is greater than `15`.

**Binary search trees** are used for efficient search operations, because the search operation has a **time complexity** of **`O(log n)`** in **binary search trees**, because at each level of the **tree**, the search space is divided in **half**.

Let's see an example of the search operation to understand this better. 

![Screenshot 2025-04-08 090358](https://github.com/user-attachments/assets/709e8b0f-f9d5-4070-b37b-a3340406a510)

* Let's say we are searching for `node 3` in the above **binary search tree**.
    * We will start with the **root node** and check, is `3` less or greater than its value. Since `3` is less than `10`, that means we are going to search in the **left** subtree. So we will eliminate the **right** subtree and move to the **root node** of the **left** subtree, which is `5` and we will continue comparing.
    * So by continue comparing, we will check is `3` less than or greater than `5`, since it's less than `5`, that means we will search in the **left** subtree.
    * So we will move to the **root node** of the **left** subtree, which is `3`, at this point we found the `node 3` that we are looking for.
    * As you can see in each level of the **tree**, we are dividing the search space by `2`. Either we eliminate the **right** or the **left** subtree.
    * So if the **binary search tree** contains `n` `nodes`, then the number of operations we need to find an **element** in that **binary search tree** is **`log n`**.

So to conclude, **binary search trees** provide an efficient way to organize and search **data**, and they are used to implement various **searching algorithms** and **databases** for quick `search operations`.
