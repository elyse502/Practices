# Linear Search
**Linear Search** is a search algorithm that sequentially checks each element of a list until a given target value is found. **Linear Search** is a very straightforward method for finding an **element** within a **list**.

![Screenshot 2025-04-17 065128](https://github.com/user-attachments/assets/74255510-3fc3-4e99-9cd7-ce9a7cb72e38)

How the **algorithm** works:
* It basically starts from the beginning of a **list** and compares the **target element** with the **current element**, and if a **match** is found, it returns the `index` of the element. Otherwise, if the end of the **list** is reached without finding the **match**, it returns a `specific value` like `-1` (that means that the **element** was not found). 
* The **time complexity** of the **linear search** is `O(n)`, where `n` is the size of the **list**, because in the **worst case**, we will have to iterate through all the **items** in the **list**, if the **item** that we are searching for is the **last item**, or if it does not exist in the **list**.
* **Linear Search** is suitable for **small data sets** or **unordered lists**, and it's also easy to implement. But for **large data sets** it's not very efficient because as you see, the **time complexity** is **linear** (`O(n)`). There are more efficient **searching algorithms** like **binary search**, which has **time complexity** of `O(log n)`, which is more efficient than **linear search** for **large data sets**. However, the **data set** needs to be sorted, otherwise it's not possible to use **binary search**.





