# accessSpecifier can be three types public, protected, and private
 
# python is not an strict language even though it has accessSpecifier we should follow the rules 

# we can access even the private variable from outside by name mangling

class example:
    def __init__(self):
        self.public = "this is public"
        self._protected = "this is protected"
        self.__private = "this is private"

    def insideClass(self):
        print("this is inside the class example")
        print("public :", self.public)
        print("private :", self.__private)
        print("protected :", self._protected)

# Create object and call method

obj1 = example()
obj1.insideClass()

class childEx(example):
    def child(self):
        print("example by using child")
        print("public :", self.public)
        print("protected :", self._protected)
        try:
            print("private :", self.__private)
        except AttributeError:
            print("private : cannot access")

obj2 = childEx()
obj2.child()

# we cannot use private here cause its private shit but we can use private variable by using name mangling 

class childEx(example):
    def child(self):
        print("example by using child")
        print("public :", self.public)
        print("protected :", self._protected)
        try:
            print("private :", self._example__private)
        except AttributeError:
            print("private : cannot access")

obj2 = childEx()
obj2.child()

# Attribute is a variable that belongs to an object. It stores data/value for that object. You access it using dot notation

class independendCode:
    def access_form_other_class(self,obj):
        print("example by indepentedCode")
        print("public :", self.public)
        print("private :", self.__private)
        try:
            print("protected :", self._example_protected)
        except AttributeError:
            print("private : cannot access")

obj4 = independendCode()
obj4.access_form_other_class(obj1)


