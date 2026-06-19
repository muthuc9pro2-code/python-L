mark = 75
if mark >= 90:
    print("grade is A")
elif mark >= 80:
    print("grade is B")
elif mark >= 70:
    print("grade is C")
elif mark >= 60:
    print("grade is D")  
else:
    print("grade is bF")  

# elif is nothing but else if

age = 17
has_license = 'no'

if age >= 18:
    if has_license == 'yes':
        print("you can drive")
    else:
        print("you cannot drive without a license")
else:
    print("you are too young to drive")

# if there is if inside if then it is called as nested if statement

# you can use logical operator like and or not to combine multiple conditions in if statement 

recharge_amount = 200
data_balance = 1.5
if recharge_amount >= 100 or data_balance >= 1:
    print("you have a good data balance")
else:
    print("you need to recharge for more data") 

order_amount = 1000
day_of_order = "monday"
gold_membership = True
if day_of_order in ["saturday", "sunday"] and (gold_membership == True or order_amount >= 500):
    print("you are eligible for 20% discount")
else:
    print("you are not eligible for discount") 

