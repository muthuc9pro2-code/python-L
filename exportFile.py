def add(a, b):
    return a + b

# *args is used to pass a variable number of arguments to a function.

def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

def create_profile(**kwargs):
    