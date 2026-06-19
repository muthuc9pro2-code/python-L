"""

python can be written as =
    *procedural programming
    *object oriented programming 
    *functional programing


1) class object inherritance, polymorism, encapsulation, polymorphism all belongs to object oriented programming aka oops
2) we dont use anything and written a code then that is called procedural programming
3) if we written funnction in a code then that is called functional programming 

PYTHON can be written all combined if we want 

higher order function (HOF) is nothing but how we can write that function
there are many types like higher order function  

DIFFERNCE BETWEEN PARAMETER AND ARGUMENT 

parameter : 
the variable written in the function definition
eg : 
   def greet(name)
      print(name) -> name is the parameter

argument :
the actual value you pass when calling the function 
eg:
    greet("muthu") -> the muthu(value) is the argument

in HOF type function : we can give an function itself as a argument to an fucntion , -> higher order1
                       we can also return an function as a output -> higher order2      

"""

# lets see a example
     # first in normal way (normal function)

def example1(username, email) :
    if email == "gmail":
        return(f"{username}@gamil.com")
    elif email == "youmail":
        return(f"{username}@youmail.com")
    elif email == "mymail":
        return(f"{username}@mymail.com")
    else:
        return(f"{username}@pmail.com") 

print(example1("muthu","gmail"))
print(example1("muthu","youmail"))
print(example1("muthu","mymail"))
print(example1("muthu","pmail"))


# Now lets see ( we can give an function itself as a argument to an fucntion )

def gmail(username):
    print(f"{username}@gmail.com")

def youmail(username):
    print(f"{username}@youmail.com")

def mymail(username):
    print(f"{username}@mymail.com")

def pmail(username):
    print(f"{username}@pmail.com")


def example2(username, mail):
    return mail(username)

example2("muthu", gmail)
example2("muthu", youmail)
example2("muthu", mymail)
example2("muthu", pmail)


# Now see the example like (we can also return an function as a output)

def example3(mail):
    def get_name(username):
        print(f"{username}@{mail}.com")
    return get_name

gmail = example3("gmail")
youmail = example3("youmail")
mymail = example3("mymail")
pmail = example3("pmail")

gmail("muthu")
youmail("muthu")
mymail("muthu")
pmail("muthu")

# we can write a function's inside a function and that inside function can access the argument of the outer function 
# and we should give prebound function (gamil,youmail) its not a variable it literally becomes function cause it value is a fucntion 
# we can give a argument to that prabound function which will become a argument for inner function 


"""
why we need this to do , its our choice but in larger project or code this will help to reuse code, arranged format, make shorter version,
increases efficeny etc regarding ur goal  
"""











