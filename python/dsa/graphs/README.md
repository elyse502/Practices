# Graphs
A **graph** is a collection of `nodes` or `vertices` and `edges` that connect pairs of `nodes`.

This is an example of a **graph**:

![Screenshot 2025-04-14 055103](https://github.com/user-attachments/assets/df3772ce-034c-4d93-a82c-20f43e9db0d5)

There are two types of **graphs**:

![Screenshot 2025-04-14 055229](https://github.com/user-attachments/assets/e7226751-255d-4ad4-b7f0-e2869be2b762)

* **Directed graphs**: In a **directed graph** the `edges` have a direction indicating a one way relationship between a `node` and another in the **graph**.
    * An example of this is a social media apllication like **Instagram**, when you follow someone and they don't follow you. So the relationship here is not **mutual**, it's a one way relationship.

![Screenshot 2025-04-14 060325](https://github.com/user-attachments/assets/f1634d81-04be-4a5a-81c2-fcdfe59978d3)

* **Undirected graphs**: In the **undirected graphs**, the `edges` have no direction. That means that the relationship is **mutual**.
    * For example, in a social media application like **facebook** the people can be represented by the `nodes` of the **graph**, and if they are friends there will be an **undirected** `edge` between them.

![Screenshot 2025-04-14 055724](https://github.com/user-attachments/assets/c37e0df5-29b4-49a5-86a4-ae6f22b0aab3)

<br /><br />

**Graphs** can also be **weighted**, meaning that each `edge` in the **graph** has a numerical value that represents the **weight** of the `edge`. And that can be anything like the `distance`, the `cost`, it depends on the **graph**. An example of that can be a maps application like **`Google Maps`**, the `nodes` can be cities and the `edges` are the roads. In that case the `weights` of the `edges` can be the distance or the travel time between two districts or cities. 

![Screenshot 2025-04-14 060951](https://github.com/user-attachments/assets/7b914bff-c98f-4211-a9a8-968e828ceece)

<br /><hr /><br />

## Graphs: `Adjacency Matrix`
The **adjacency matrix** is a representation of the **graph** in computer science.

An example of an **adjacency matrix**:

![Screenshot 2025-04-14 063015](https://github.com/user-attachments/assets/bbf38607-6ce4-4f9f-8577-73eb0e9d0f20)

Since the above **graph** is **undirected**, the **matrix** is `symmetric`, meaning that one half is a mirror of the other half of the **matrix**.

![Screenshot 2025-04-14 063312](https://github.com/user-attachments/assets/aa62926a-cd72-4f41-ba9a-8fbf2ff7664d)

**N.B:** In the **directed graph**, the **matrix** may not be **symmetric**. Here is an example of a **directed graph**:

 ![Screenshot 2025-04-14 063815](https://github.com/user-attachments/assets/e119a62b-8190-4168-b003-f89039ed7c26)
 
As you can see, the above **matrix** is **not symmetric** unlike in the **undirected graph** case.

<br /><hr /><br />

## Graphs: `Adjacency List`
The **adjacency list** is a representation of the **graph** in computer science. In the **adjacency list**, we will use a `hash map` and the **keys** in the `hash map` will be the `nodes` of the **graph**. So each **key** in the `hash map` represents a `vertex` or a `node` in the **graph**. So for each **key**, or in other words, for each **vertex**, the value will be a `list` of its neighboring **vertices**.

Let's see an example, where we have an **undirected graph**:

![Screenshot 2025-04-14 082501](https://github.com/user-attachments/assets/db28e3ab-a984-46df-b386-b50895915156)

<br /><hr /><br />

## Graphs: Time & Space Complexities
### Space Complexity
The **adjacency matrix** itself is a square matrix with the dimensions `v` multiplied by `v`, where `v` is the number of **vertices** in the **graph**. So the total the total **space complexity** of the **adjacency matrix** is `O(v^2)`. Meanwhile, in the **adjacency list** representation, we use **hash table** and the `keys` are the `vertices` of the **graph**, and the `value` for each `key` is the `neighbors` for each `vertex`. So in this case, if the number of `vertices` is represented by `v` and the number of `edges` is represented by `E`, then the total **space complexity** of the **adjacency list** is `O(v + E)`, because we store only the `vertices` and the `edges` of each `vertex`.

![Screenshot 2025-04-14 141816](https://github.com/user-attachments/assets/3764a3ac-adfe-409a-b96e-5521bad09fcb)

So as you can see, the **adjacency list** is more efficient than the **adjacency matrix** when it comes to **space consumption** and **space complexity**.

### Time Complexity
The **time complexity** of the **graph** operartions in both **adjacency matrix** and **adjacency list**:
* Adding a new `node` to the **graph**: The **time complexity** of adding a new `node` using the **adjacency matrix** is `O(v^2)`, where `v` is the current number of **vertices** in the **graph**. On the other hand, the **time complexity** of adding a new `node` using the **adjacency list** is `O(1)`.

![Screenshot 2025-04-14 142557](https://github.com/user-attachments/assets/21006364-5f00-4755-8494-09675a8510a9)

* Adding an `edge` between two `nodes`: Using the **adjacency matrix** we will have to update those entries to `one(1)`, so the **time complexity** here is **constant** (`O(1)`). On the other hand, using the **adjacency list** we will have to append those `vertices` to the list of neighbors in the corresponding `vertices`, so the **time complexity** here also is **constant** (`O(1)`).

![Screenshot 2025-04-14 143407](https://github.com/user-attachments/assets/d872c3a3-b684-499a-bb8d-5fb72d678202)


* Removing an `edge` operation: In the **adjacency matrix** we will just update the entries to `zero(0)`, so the **time complexity** here is **constant** (`O(1)`). On the other hand, using the **adjacency list** we will have to go to the list of neighbors of the corresponding `vertices` and search for the relevant `nodes` an delete them. So this search operation is `linear`. So the **time complexity** here is `O(E)`, where `E` is the number of `edges` that we have to iterate through.

![Screenshot 2025-04-14 144757](https://github.com/user-attachments/assets/2765e585-d716-4b38-8c3f-369faaacb5ee)

* Removing a `node` operation: Removing a `node` from the **adjacency list** we will have to remove the corresponding entry from the `dictionary`, and then we will have to go through all the `nodes` and delete this `node` if it exists in the list of the neighbors for each other `node`. So this search operation has `O(V+E)` **time complexity**, where `v` is the number of `vertices` and `E` is the number of `edges`, but removing the entry itself has **constant** `O(1)` **time complexity**, so the total **time complexity** will be `O(V+E)`. On the other hand removing a `node` from the **adjacency matrix**, we will have to remove the corresponding `row` and `column`. So this will need a reconstructing of the complete **matrix**, and in this case the **time complexity** will be `O(v^2)`, where `v` is the number of `vertices`.

![Screenshot 2025-04-14 145728](https://github.com/user-attachments/assets/bc0a0ee0-9e76-45ec-9520-f7ad8e21a912)

