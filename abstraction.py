from abc import ABC, abstractmethod

# To make a class a abstract class we should import the above thing

# an abstract class can have both abstractMethod and normalMethod

class principle(ABC):
    @abstractmethod
    def student1(self):
        print("student1")
    
    @abstractmethod
    def student2(self):
        print("student2")

    def student3(self):
        print("student3")

class vicePrinciple(principle):

    def student1(self):
        print("muthu")

    def student3(self):
        print("jack")

obj = vicePrinciple()
obj.student1()
obj.student2()

# now the above code will send a error cause abstraction is nothing but u tell the child class to use all the abstractmethod without using that the code will not run 
# And the object should always be child class 
# the normal method in abstract class is not must to be used , u can use or not ur wish but the abstract class is must to use

class chairman(ABC):
    @abstractmethod
    def student1(self):
        print("student1")
    
    @abstractmethod
    def student2(self):
        print("student2")

    def student3(self):
        print("student3")

class headMaster(chairman):

    def student1(self):
        print("muthu")

    def student2(self):
        print("kumar")

obj = headMaster()
obj.student1()
obj.student2()


    
    
