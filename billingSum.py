amount=1300
tax=amount/18
total=amount+tax
print("Total bill is:", total)

if total > 1000:
    discount=total/10
    total -= discount

print("Final total after discount:", total)