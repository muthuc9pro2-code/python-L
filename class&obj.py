# if u write def inside a class then it is called as method, if its outside the class then its is called as function 

class student:
    def say_hello(self):
        print("pizza")

s1 = student()
s1.say_hello()

""" 
okay in class method we should always write self as a argument thats a rule cause python take s1.say_hello() as
s1.say_hello(s1) that means s1 is calling say_hello() inside class student
"""

