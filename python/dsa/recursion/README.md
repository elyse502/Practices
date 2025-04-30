# Recursion
**Recursion** in the context of programming refers to a technique where a **function calls itself** in order to solve a problem.

This is often done in order to reduce the number of operations required to solve a problem.

**Open Box instance:**

![Screenshot 2025-04-30 080143](https://github.com/user-attachments/assets/0305f446-33e7-4407-ab17-8f29d1a2c685)

**Pseudo Code of Open Box function:**
```python
function open_box(current_box):
    if current_box does not contain Key:
        # When the current box does not contain a key and the function calls itself with a new box or the sub box, this is called a recursive case.
        return open_box(current_box.sub_box)  # Recursive Case.
    else:
        # When the current box contains a key, this is called the base case.
        return Key  # Base Case.
```

* the `Base Case` is very important in **recursion**, because if there is no `Base Case` the function will keep calling itself. And this will cause a **StackOverflowError**.

<br /><br />

## Examples
### Fibonacci Sequence

The **Fibonacci Sequence** is a sequence of numbers in which each number is the sum of the two preceding ones.

The first two numbers in the sequence are 0 and 1.

The next number in the sequence is the sum of the two preceding ones.

For example, the first 10 numbers in the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

The Fibonacci sequence can be defined recursively as follows:

$$f(n) = \begin{cases} 0, & \text{if } n = 0 \\ 1, & \text{if } n = 1 \\ f(n - 1) + f(n - 2), & \text{otherwise} \end{cases}$$

where $f(n)$ is the $n$th number in the sequence.

For example, $f(3) = f(2) + f(1) = 1 + 1 = 2$, $f(4) = f(3) + f(2) = 2 + 1 = 3$, and $f(5) = f(4) + f(3) = 3 + 2 = 5$.

The first 10 numbers in the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

<br /><br />

### Factorial

The **factorial** of a number is the product of all positive integers less than or equal to that number. So the **factorial** of a non-negative integer $n$, is the product of all positive integers less than or equal to $n$.

**Example**:
* The factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

**Example with recursion:**

`factorial(3)` = 3 * 2 * 1 = 6

`factorial(3)` = 3 * `factorial(2)`

`factorial(2)` = 2 * `factorial(1)`

![Screenshot 2025-04-30 085040](https://github.com/user-attachments/assets/3729bcdf-af0a-4d3b-9c02-00eeb33c00df)
![Screenshot 2025-04-30 085142](https://github.com/user-attachments/assets/003c0360-f14b-4ef0-9c77-cdd074d91395)

The factorial can be defined recursively as follows:

$$f(n) = \begin{cases} 1, & \text{if } n = 0 \\ n * f(n - 1), & \text{otherwise} \end{cases}$$

where $f(n)$ is the factorial of $n$.

For example, $f(5) = 5 * f(4) = 5 * 4 * f(3) = 5 * 4 * 3 * f(2) = 5 * 4 * 3 * 2 * f(1) = 5 * 4 * 3 * 2 * 1 = 120$.

The factorial of 0 is 1.

<br /><hr /><br />

# Call Stack
In the context of programming, a **call stack** is a stack data structure that **keeps track of the sequence of function calls** and their corresponding execution contexts during the execution of a program.

So when a function is called, it's pushed onto the `call stack`, and the function at the top of the `stack` is executed. And if this function calls another function, then this function is pushed onto the `stack` and the control transfers to the newly called function.

**Example**:

![Screenshot 2025-04-30 083300](https://github.com/user-attachments/assets/f9dd4435-80ba-478c-9988-a5d12f97a976)

**Example with recursion:**

![Screenshot 2025-04-30 083517](https://github.com/user-attachments/assets/aacf9f69-d0c1-4194-9b70-190d1b8e295b)

<br /><hr /><br />

# Recursion: Big O
In **recursion**, the `time complexity` depends on the **number of recursive calls** and the `space complexity` depends on the **depth of the call stack**.

**Example**:
```python
function factorial(n):
    if n equals 0:
        return 1
    else:
        return n * factorial(n - 1)
```
* **The time complexity** is `O(n)`, where `n` is the number of recursive calls.
* **The space complexity** is `O(n)`, where `n` is the depth of the call stack.

<br /><hr /><br />

# Stack Overflow
**Stack overflow** occurs when the `call stack` of a program **exceeds its available memory space**. And this can happen due to several reasons, such as:

1. Missing or incorrect `base case` in **recursion**, which leads to infinite recursion.
For example:

```python
function infiniteRecursion(n):
    return infiniteRecursion(n + 1)
```

The above function is a **recursive function** and it has no `base case`, so it will keep calling itself infinitely, and the `call stack` will keep adding instances of this function until it runs out of space. And this is what's called **stack overflow**.

2. Excessive `recursion depth`, and this happens when the **recursive function** has a `base case` but it has a very inefficient `time complexity`, and with a large input it can cause a `call stack` to run out of memory and a **stack overflow** will happen.
For example:

```python
function fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

The above **fibonacci function** as we saw has a `O(2^n)` or `exponential time complexity`, which leads to exessive recursion depth for large inputs, and this can cause a **stack overflow**. And we can solve that issue with the `memoization` or `dynamic programming` techniques to make the `time complexity` `linear` or `O(n)`.

**N.B:** To avoid _**stack overflow**_, you have to always define a proper `base case` and pay attention about the depth of the **recursion** in your code.




