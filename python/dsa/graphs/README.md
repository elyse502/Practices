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

## Graphs: Adjacency Matrix
The **adjacency matrix** is a representation of the **graph** in computer science.

An example of an **adjacency matrix** is:


Since the above **graph** is **undirected**, the **matrix** is `symmetric`, meaning that one half is a mirror of the other half of the **matrix**.



 **N.B:** In the **directed graph**, the **matrix** may not be **symmetric**. Here is an example of a **directed graph**:

 
 
 As you can see, the above **matrix** is **not symmetric** unlike in the **undirected graph** case.

