def add(a, b):
    return a + b

# *args is used to pass a variable number of arguments to a function.

def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

# **kwargs is used to pass key and value type of variable length arguments to a function.

def create_profile(**kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return(profile)

def sample_function(**kwargs):
    print("kwargs working")
    for key,value in kwargs.items():
        print(f"{key}: {value}")

    