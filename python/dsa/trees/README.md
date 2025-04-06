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





