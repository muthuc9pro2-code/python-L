from functools import reduce

"""
LAMBDA FUNCTION :

         * lambda function is a one line function 
         * the whole code's logic will be one liner
         * lambda function will not any name for the function 
         * it will assign to a variable

uses: 

    * it is used to write a quick code, well helpfull for map, filter, reduce etc

cons:
     
    * it is not used like a normal function cause in normal function we can write multiple line logic, code reusability, can give a name 
    * you cant do a shit like normal function with lambda function 
"""    
     
# SYNTAX : lambda parameter : logic

#examples : 

add = lambda a, b : a + b
print(add(2,5))

square = lambda x : x*x
print(square(4))


"""
MAP FUNCTION : 

           * Map just says , take everything in this collection, apply a function to it, and give me the transformed items
"""

# SYNTAX FOR MAP : map(function , iterable) --> this says take this iterable, in this take each item in iterable and do this function,
#                  so each item becames the argument of the function . 

# example for map :
        
fruits = ["apple", "orange", "pineapple", "pappaya"]

result = list(
    map(lambda fruit : fruit.upper(), fruits)
    )                                           # in python map() produces some shit as output to get output as list we should use list()
print(result)

"""
FILTER FUNCTION : 
               
            * Filter just filter the collection regarding to the function given to filter()
"""

# SYNTAX FOR FILTER : filter(function, iterables) --> same as map()

# example for Filter :

nums = [1,2,3,4,5,6,7,8,9]
even = list(
    filter(lambda x : x % 2 == 0, nums) # why list() infront of filte() , its just same as map()
)
print(even)

"""
REDUCE FUNCTION : 

         * First to use reduce we must import it from functools
         * reduce will always gives a single output from a collection , it will just reduce the collection regarding the function given to
           reduce()
         * used for cummulative functionality, aggregasion 
"""

# SYNTAX FOR REDUCE : reduce(function, iterables) --> same as map but dosnt require output type like list() for map() & filter()

#example1 

nums = [2,5,6,7]

total = reduce(lambda a,b : a+b, nums) # reduce take a as 2 & b as 5 then add it , becomes 7 then a as 7 & b as 6 , goes on 
print(total)

#example2

nums = [2,9,8,5,4,2]

larg_num = reduce(lambda a,b : a if a > b else b, nums)
print(larg_num)


# EXAMPLE senario 
     # add all items worth above 1k  

items = [200, 300, 1001, 1200, 2222, 89]

expensive = list(filter(lambda a: a > 1000, items))

add= reduce(lambda a,b : a+b, expensive)
 
print(add)













    
   