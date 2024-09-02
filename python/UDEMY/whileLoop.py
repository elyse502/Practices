# Tutorial 36-Python While Loop

# Using while loop
i = 3
while i > 0:
    print(i)
    i -= 1
print()

i = 5
while i < 10:
    print(i)
    i += 1
else:
    print("Displayed Successfully!")


# A program to display a pattern using loops
n = int(input("Please enter the number of layers... "))
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(".", end="")
        j += 1
    j = 1
    while j <= 2*i - 1:
        print("*", end="")
        j += 1
    j = 1
    while j <= n - i:
        print(".", end="")
        j += 1
    print()
    i += 1


# Another program to display a pattern using loops using blank space instead of *
n = int(input("Please enter the number of layers... "))
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end="")
        j += 1
    j = 1
    while j <= 2*i - 1:
        print("*", end="")
        j += 1
    j = 1
    while j <= n - i:
        print(" ", end="")
        j += 1
    print()
    i += 1


# A program to display a pattern using loops
n = int(input("Please enter the odd number of layers... "))
m = (n+1)/2 # mid point...
i = 1
while i <= n:
    if (i > m):
        b = n-i # Blank...
        s = 2*(i-m)+1   # Star...
    else:
        b = i-1
        s = 2*(m-i)+1
    j = 1
    while j <= b:
        print(".", end="")
        j += 1
    j = 1
    while j <= s:
        print("*", end="")
        j += 1
    j = 1
    while j <= b:
        print(".", end="")
        j += 1
    print()
    i += 1