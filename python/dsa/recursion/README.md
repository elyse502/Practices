# Recursion
**Recursion** in the context of programming refers to a technique where a **function calls itself** in order to solve a problem.

This is often done in order to reduce the number of operations required to solve a problem.

**Open Box instance:**


**Pseudo Code of Open Box function:**
```groovy
function open_box(current_box):
    if current_box does not contain Key:
        # When the current box does not contain a key and the function calls itself with a new box or the sub box, this is called a recursive case.
        return open_box(current_box.sub_box)  # Recursive Case.
    else:
        # When the current box contains a key, this is called the base case.
        return Key  # Base Case.
```

* the `Base Case` is very important in **recursion**, because if there is no `Base Case` the function will keep calling itself. And this will cause a **StackOverflowError**.

## Examples
**Fibonacci Sequence**

The **Fibonacci Sequence** is a sequence of numbers in which each number is the sum of the two preceding ones.

The first two numbers in the sequence are 0 and 1.

The next number in the sequence is the sum of the two preceding ones.

For example, the first 10 numbers in the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

The Fibonacci sequence can be defined recursively as follows:

$$f(n) = \begin{cases} 0, & \text{if } n = 0 \\ 1, & \text{if } n = 1 \\ f(n - 1) + f(n - 2), & \text{otherwise} \end{cases}$$

where $f(n)$ is the $n$th number in the sequence.

For example, $f(3) = f(2) + f(1) = 1 + 1 = 2$, $f(4) = f(3) + f(2) = 2 + 1 = 3$, and $f(5) = f(4) + f(3) = 3 + 2 = 5$.

The first 10 numbers in the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

**Factorial**

The **factorial** of a number is the product of all positive integers less than or equal to that number.

For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

The factorial can be defined recursively as follows:

$$f(n) = \begin{cases} 1, & \text{if } n = 0 \\ n * f(n - 1), & \text{otherwise} \end{cases}$$

where $f(n)$ is the factorial of $n$.

For example, $f(5) = 5 * f(4) = 5 * 4 * f(3) = 5 * 4 * 3 * f(2) = 5 * 4 * 3 * 2 * f(1) = 5 * 4 * 3 * 2 * 1 = 120$.

The factorial of 0 is 1.








