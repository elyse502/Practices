# Hash Tables
A **hash table** is a data structure that's used to store `key value pairs`. Some examples of `key value pairs` can be a person name and their phone number, so the name is the **key** and the **value** is the phone number.

![Screenshot 2025-04-10 123112](https://github.com/user-attachments/assets/196bd12f-668e-4a3e-a95f-fc20fbb73370)

Here is an example of what a **hash table** entry can look like:

![Screenshot 2025-04-10 123227](https://github.com/user-attachments/assets/1aeb6563-7797-44db-8e49-1835f73bcd44)

![Screenshot 2025-04-10 123338](https://github.com/user-attachments/assets/bde87b63-f4c8-4ede-b365-c1ec3893b7ec)

## Collision
* When a **hash function** is invoked and return an **address** that was used previously to store another `key value pair` it's called a **`collision`**. So in that case the `key value pairs` that was stored previously at that **addres** will not be overwritten because, the **hash table** uses an array of lists. So if there is a **collision** the `key value pair` will be appended to that list and will not overwrite the previously stored `key value pair`

![Screenshot 2025-04-10 123506](https://github.com/user-attachments/assets/d4c4071f-6206-403f-9ae6-6570e4da6770)

* To retrieve an **element** from the `hash table`, we use the **key** of the **element** that we want to retrieve to retrieve it, and the **hash table** takes that **key** and pass it to the `hash function` and then the `hash function` returns the **address** at which that **item** with that specific **key** is stored, then the `hash table` retrieves the `key value pair` from that **address** and returns it.
  * If there are more than 1 **item** stored at that specific **address**, the `hash table` will call the **hash function** as well and get the **address**, and then it starts to search in the list at that **address** for a `key value pair` with that specific **key** until it finds it, and then returns it. And as you can see, that increases the **time complexity**, so a good **hash function** should avoid `collisions`!

![Screenshot 2025-04-10 123650](https://github.com/user-attachments/assets/76d364cb-6d69-484a-8cdf-0f827b086e97)

## Hash Table: Time & Space Complexities
* **Insert/Get** :
  * Average Case: **O(1)**
  * Worst Case: **O(n)**
* **Space Complexity**: **O(n)** where **n** is the number of `key/value pairs` 



