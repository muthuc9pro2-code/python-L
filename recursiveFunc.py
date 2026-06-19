"""

RECURSIVE FUNCTION :

                * A recursive function is a function that calls itself in order to solve a smaller version of the same problem
"""

# EXAMPLE 1 FOR RECURSIVE FUNCTION :


def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)


print(factorial(5))

# EXAMPLE 2


def damal(n):
    if n == 0:
        print("boom")
        return 
    print(n)
    damal(n - 1)

damal(5)



