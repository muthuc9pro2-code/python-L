amount = 250 
age = 65
student='yes'
if age >= 60 or student == 'yes':
    discount = amount * 0.10
    amount -= discount    
else: 
    amount = amount
print("Final amount to be paid:", amount)