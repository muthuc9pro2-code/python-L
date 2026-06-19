"""
function can be classified as pure and impure function 

PURE FUNCTION :
              if a fucntion does not change any global scope shit (0 side effect) , the changes inside the funciton does not change
              anything outside the fucntion 

IMPURE FUNCTION :
               if a fucntion does change any global scope shit (have side effect)  ,  the changes inside the funciton does change
               something outside the fucntion  
"""

# example for pure function :

total = 0  # --> global variable

def add(num):   
    global total   # in python we should use global iniside the function to modify or change the value , just printing dont need  
    total += num   # --> this function uses global variable inside the funciton 
    print(total)

def check():       # this fucntion doesnt uses any global variable its just printing the global variable 
    print(total)

add(2)
check()


# the output will be 2 for both cause the def add() just change the value of total globally 
# now the add() is a impure function

amount = 0 

def adding(num):
    amount = 15
    amount += num
    print(amount)

def checking():
    print(amount)

adding(3)
checking()

# here no use of global variable inside adding() so it doesnt change anything globally so,
# adding() is a pure function 

