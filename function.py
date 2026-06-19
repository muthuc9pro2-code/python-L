def hello():
    print("hello world")
hello()

# diff of arugument and parameter 

def greet(name):
    print(f"hello {name}")
greet("muthu")

# in above code the name is parameter and "muthu" is argument

def add(a, b):
    print(a+b)
add(5, 10)

# return

def add(a, b):
    return a+b

result = add(5, 9)
print(result)

# return is used to get the output of a function and store it in a variable,class,object etc. for later use. In the above code, the add function returns the sum of a and b, which is then stored in the variable result and printed.

