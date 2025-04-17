# Linear Search
**Linear Search** is a search algorithm that sequentially checks each element of a list until a given target value is found. **Linear Search** is a very straightforward method for finding an **element** within a **list**.

![Screenshot 2025-04-17 065128](https://github.com/user-attachments/assets/74255510-3fc3-4e99-9cd7-ce9a7cb72e38)

How the **algorithm** works:
* It basically starts from the beginning of a **list** and compares the **target element** with the **current element**, and if a **match** is found, it returns the `index` of the element. Otherwise, if the end of the **list** is reached without finding the **match**, it returns a `specific value` like `-1` (that means that the **element** was not found). 
* The **time complexity** of the **linear search** is `O(n)`, where `n` is the size of the **list**, because in the **worst case**, we will have to iterate through all the **items** in the **list**, if the **item** that we are searching for is the **last item**, or if it does not exist in the **list**.
* **Linear Search** is suitable for **small data sets** or **unordered lists**, and it's also easy to implement. But for **large data sets** it's not very efficient because as you see, the **time complexity** is **linear** (`O(n)`). There are more efficient **searching algorithms** like **binary search**, which has **time complexity** of `O(log n)`, which is more efficient than **linear search** for **large data sets**. However, the **data set** needs to be sorted, otherwise it's not possible to use **binary search**.

<br /><hr /><br />

# Binary Search
**Binary Search** is a `divide` and `conquer` **algorithm** that repeatedly divides a **sorted data set** in `half` to locate the **target element**. So by that it narrows down the `search space` at each step.
* **Binary Search** is a `divide and conquer algorithm` that is used to find an `element` in a **sorted list**.
* In **binary search** we use two **pointers** called `low` and `high`, and they are used to define the `current search space` within the **array**.
    * Initially `low` is set to the first `index` of the **array** and `high` is set to the last `index` of the **array**, because initially we will search the entire **array** and then we will divide it step by step later.
    * In each **iteration**, the `mid point` or `mid` of the `current search space` is calculated using this formula: `mid = (low + high) // 2` (where `//` is integer division, by ignoring the decimal part), and that will get us the `index` of the **mid element**. And then we will compare the **middle element** with the **target element**.
    * If the **target element** is less than (`<`) the **mid element**, it means that the **target** must be in the `left half` of the `current search space`. So in that case the `high pointer` is updated to `mid - 1`.
    * If the **target element** is greater than (`>`) the **mid element**, it means that the **target** must be in the `right half` of the `current search space`. So in that case the `low pointer` is updated to `mid + 1`.
    * Otherwise, if the **target element** is equal to the **mid element**, it means that the **target** is found and we can return the `index` of the **target element**.
* As we saw in each `iteration` we reduce the `search space` by **half**, and as we learned in the **big O notation**, this means that the **time complexity** is `O(log n)`, where `n` is the number of the `items` in the **array**.
* **Binary Search** is efficient when working with **large data sets**, but they have to be **sorted**.


