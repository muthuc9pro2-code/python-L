"""
print("step 1 : start")
a=10
b=0
result = a/b
print("step 2 : result is", result)

# there is a difference between error and exception


print hi


# if an statement has error in compile time itself then it is called error like in the above code

# exception is an error that occur in runtime eg like a/b in the first block of code

# exception error should be handled to avoid code crash

# we can handle exception by try throw catch finally blocks


number_of_items = int(input("How many items ?"))
total_price = 200 * number_of_items
average_price = total_price / number_of_items
print("Average price:", average_price)

# if we run this above code it will just stop if user typed 0 so break the code so the print line will never execute
# To avoid this we write this block in try
"""

try:
    number_of_items = int(input("How many items ?"))
    total_price = 200 * number_of_items
    average_price = total_price / number_of_items
    print("Average price:", average_price)
except Exception:
    print("you cannot have 0 items")


print("Ooooo")

# Here we tell python to what to do when the code breaks by except block, we have to give the type of code we expect if we dono just type Exception ,the python itself take care of that

# there is another block called finally

try:
    number_of_items = int(input("How many items ?"))
    total_price = 200 * number_of_items
    average_price = total_price / number_of_items
    print("Average price:", average_price)
except FileNotFoundError:
    print("you cannot have 0 items")
finally:
    print("logout")

print("Ooooo")

# Here if we dont write the crt error type that itself throw a error and break the code but finally block executes whatever happens 

# why not if else use instead of exception u know why 