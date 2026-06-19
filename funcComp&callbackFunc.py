"""
FUNCTION COMPOSITION : 
                * A composition function is when the output of one function becomes the input of another - like f(g(x))
"""

def add(x):
    return x + 2 

def multi(x):
    return x * 2 

def comp(x):
    return add(multi(x)) # Here we calling multiple function where the multi function called first comp's argument becomes multi's 
                         # argument and executes and its output becomes input arugument for add 

print(comp(10))


"""
CALLBACK FUNCTION : 
            * A callback function is a function that you pass as an argument to another function ,
            so that it can be called (executed) later, usually after some action is completed.
"""

# EXAMPLE FOR CALLBACK: 

def function(callback):
    print("Hello world")
    callback()

def call():
    print("Iam muthu kumar")


function(call)