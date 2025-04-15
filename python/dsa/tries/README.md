# Tries
**Tries** also known as **Prefix Trees**, are `tree-like data structures` that are used for **efficient storage and retrieval of strings**.

Here is an example of a **trie data structure**:

![Screenshot 2025-04-15 065728](https://github.com/user-attachments/assets/01828fee-3876-4e16-a0ec-e9d7dd61e360)

* As you can see it mainly consists of `nodes` that represent `characters`, and those `characters` form `words`. So we can say that it stores `strings` or `words` in an efficient way, so that you can search or retrieve those `words` or `strings` efficiently.
* As you can see, each `node` represents a `character` and the **root** `node` represents an **empty string**.
* And how do we know that a `character` is representing a `last character` in a `word`?
    * This is known through a **flag** called `isWord`, and it's configured in each `node` in the **tree**. If a `character` is the `last character` in a `word`, the **flag** is going to be **true**, otherwise it's going to be **false**.
* The goal of using **tries** is efficient storage and retrieval or search for `strings` or `words`.


