from functools import partial 

"""
CLOSURE FUNCTION: 

     * closure function is nothing but if a inner function take argumrnt from the outter function then that funciton is called as 
     closure function 
     * its like higher order 2 

"""

#EXAMPLE FOR CLOSURE :

def outter(msg): 
    def inner():
        print(msg)
    return inner 

out = outter("nan thanda mass")
out()

"""
PARTIAL FUNCITON :
           *partial function is nothing but giving a fixed for a argument of a function 
           *it should be import from functools
"""

# SYNTAX FOR PARTIAL : partial(function, arugument = value) --> here the value will be fixed for that argument 

# EXAMPLE1 FOR PARTIAL:

def gst(total, tax):
    return total * (1 + tax)

gst_tax = partial(gst, tax = 0.18)

print(gst_tax(1000))

# EXAMPLE2 FOR PARTIAL:

def mail(username, domain):
    return f"{username}@{domain}"

gmail = partial(mail, domain = "gmail.com")
youmail = partial(mail, domain = "youmail.com")

print(gmail("muthu"))
print(youmail("muthu"))




