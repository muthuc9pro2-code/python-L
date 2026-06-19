# method is nothing but functions inside class 
# There are three types of method : objMethod(instance), clsMethod(class), staticMethod(static)

class example:
    def instance_method(self):
        print("objMethod")

    @classmethod
    def class_method(cls):
        print("clsMethod")

    @staticmethod
    def static_method():
        print("staticMethod")

obj = example()
obj.instance_method()

example.class_method()

example.static_method()

# static and class method looks same right lets see the difference

class difference:
    
    company = "zoho"

    @classmethod
    def change_companyName(cls, name):
        cls.company = name

    @staticmethod
    def try_change_companyName(name):
        difference.company = name

difference.change_companyName("apex")
print(difference.company)

difference.try_change_companyName("neo")
print(difference.company)

# the difference is just nothing, to change the value u should hardcode inside class lvl when compare to class method (cause it just uses cls)


