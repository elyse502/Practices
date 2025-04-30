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





