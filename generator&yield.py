"""
GENERATOR FUNCTION :  
            * Generator function is a special function type of function that uses the yield keyword
            to return value one by one, instead of returning everything at once 

            * it mainly used when memory is in bottleneck ,cause it prints one pause and prints 
            next one
"""

# EXAMPLE 

def nums(x):  # normal way just returning
    return  [i for i in range(x)]  # return always expect a value to return thats y [] used.if no bracket it returns multiple value

print(nums(10))


def nums1(x):
    for i in range(x):
        yield(i)
    
print(nums1(5)) # this print will not work , the yield() throws some shit as output

for i in nums1(5):
    print(i)   # print works cause u seperatly iterate a the values from nums1() which has yield()


