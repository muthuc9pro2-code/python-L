# for loop

names = ["saravanan", "muthu", "kumar", "suresh", "rajesh"]

for name in names:
     name.capitalize()
print(names)

# array is list in python
# id names = in list then the index(0) = "Saravanan"
# if names = "saravanan" then index(0) = "s"

for i in range(len(names)):
    names[i] = names[i].capitalize()
print(names)

# while loop

correct_pin = "1234"
pin = ""

while pin != correct_pin:
     pin = input("Enter your pin: ")

print("access granted")

# break

# break in for
for i in range(10):
    if i == 7:
        break
    print(i)

#  break in while 
correct_pin = "1234"

while True:
     pin = input("enter your pin: ")
     if pin == correct_pin:
         print("access granted")
         break
     print("incorrect pin, please try again")

# continue

for i in range(10):
    if i < 8:
        continue
    print(i)

# continue is used to skip the current iteration of the loop and move to the next iteration. In the above code, it will skip all numbers less than 8 and only print 8 and 9.

num = [-10, -5, 0, 5, 10, -7, -3, 9 , -9]

for n in num:
    if n >= 0:
        continue
    print(n)

# placeHolder

for i in range(5):
    pass # pass is used as a placeholder when you want to write a loop or function but you dont want to implement it now . It allows the code to run without any errors, but it doesn't do anything. In the above code, ypu  can just implement the loop later when you have the logic ready.

# small logics 

# timecounter

count = 5

while count > 0:
    print(f"countdown: {count}")
    count -= 1
print("Time's up!")

count = 0

while count < 5:
    print(f"countdown: {count}")
    count += 1
print("Countup complete!")


# add to cart 

cart = []

while True:
    item = input("Add Item (type 'done' after all items you want is added): ")
    if item.lower() == 'done':
        break
    cart.append(item)
print("your cart : ", cart)