# if u write def inside a class then it is called as method, if its outside the class then its is called as function 

class student:
    def say_hello(self):
        print("pizza")

s1 = student()
s1.say_hello()

# here class is student, s1 is object, def is method

""" 
okay in class method we should always write self as a argument thats a rule cause python take s1.say_hello() as
s1.say_hello(s1) that means s1 is calling say_hello() inside class s1 is student 
"""

class master:
    def __init__(self, fname, age):
        self.name = fname
        self.age = age

    def display(self):
        print(f"name : {self.name}, age : {self.age}")

# f is nothing but `` in js it is called formatter

s1 = master("muthu", 22)
s1.display()

class Employee:
    def __init__(self, name, aadhaar):
        self.name = name
        self.aadhaar = aadhaar

    def enter_office(self):
        print(f"{self.name} enters using aadhaar {self.aadhaar}")

    def open_bank_account(self):
        print(f"Bank account opened for {self.name} with aadhaar {self.aadhaar}.")

s1 = Employee("Muthu", "1234-5678-9090")
s1.enter_office()
s1.open_bank_account()



