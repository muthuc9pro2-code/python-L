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

class childEx1(example):
    def child(self):
        print("example by using child")
        print("public :", self.public)
        print("protected :", self._protected)
        try:
            print("private :", self.__private)
        except AttributeError:
            print("private : cannot access")

obj2 = childEx1()
obj2.child()

# we cannot use private here cause its private shit but we can use private variable by using name mangling 

class childEx2(example):
    def child(self):
        print("example by using child")
        print("public :", self.public)
        print("protected :", self._protected)
        try:
            print("private :", self._example__private)
        except AttributeError:
            print("private : cannot access")

obj2 = childEx2()
obj2.child()

# Attribute is a variable that belongs to an object. It stores data/value for that object. You access it using dot notation

class independendCode:
    def access_form_other_class(self,obj):
        print("example by indepentedCode")
        print("public :", obj.public)
        print("private :", obj._example__private)
        try:
            print("protected :", obj._protected)
        except AttributeError:
            print("private : cannot access")

obj4 = independendCode()
obj4.access_form_other_class(obj1)

# __example using the parent name with underscore infront is called name mangling

# lets see in method, its just same as attribute's
 
class damal:
    def public(self):
        print("public")

    def _protected(self):
        print("protected")

    def __private(self):
        print("private")

    def inisdeClass(self):
        print("insideClass")
        self.public()
        self._protected()
        self.__private()

obj1 = damal()
obj1.inisdeClass()

class damalChild(damal):
    def call(self):
        print("child class")
        self.inisdeClass()
    
    def callIndividual(self):
        print("child class")
        self.public()
        self._protected()
        try:
            self.__private()
        except AttributeError:
            print("private : cannot access")
        

obj2 = damalChild()
obj2.call()
obj2.callIndividual()

# this is an example by using child class
# if i call individually private shit it throws error but if i call the insideClass its just print everything including the private variable

class dubuku:
    def calling(self, obj):
        print("independent class")
        obj.public()
        obj._protected()
        try:
            obj.__private()
        except AttributeError:
            print("private : cannot access")

obj3 = dubuku()
obj3.calling(obj1)

    