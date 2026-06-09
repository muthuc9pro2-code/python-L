class dad: #parent
    def house(self):
        print("muthu kumar")

class son(dad): #child
    def factory(self):
        print("kumar muthu")

s=son()
s.house()
s.factory()

# The above code is called single level inheritance casuse we only have one child

# lets see 2 example why we use inheritance

class app1():
    def V1(self):
        print("orders")

class app1_1(app1):
    def V2(self):
        print("review")

    def V1(self):
        print("no orders")

obj = app1_1()
obj.V2()
obj.V1()

# so here u can use update and overwrite the logic without erasing the previous code 

class dad(): #parent
    def house(self):
        print("red")

class son(dad): #child
    def factory(self):
        print("white")

    def house(self):
        print("yellow")

obj = son()
obj.factory()
obj.house()

# if you want to change to parent class just change the obj 

# another example for inheritance and we should always use latest child class as object to access everything

# we can also do this even if the parent class is in some other file by importing

class exportFile():
    def hello(self):
        print("hello")

# this above code is only for export to other file so check the other file regarding this above exportFile 








