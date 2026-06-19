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

class grandDad():
    def cycle(self):
        print("silver")

class dad(grandDad): 
    def house(self):
        print("red")

class son(dad):
    def factory(self):
        print("white")

    def house(self):
        print("yellow")

obj = son()
obj.factory()
obj.house()
obj.cycle()

# this is multilevel inheritance

class dad(): #parent
    def house(self):
        print("red")

class son1(dad): #child1
    def factory(self):
        print("white")

    def house(self):
        print("yellow")

class son2(dad): #child1
    def market(self):
        print("fruits")

    def house(self):
        print("green")



obj1 = son1()
obj1.factory()
obj1.house()

obj2 = son2()
obj2.market()
obj2.house()

# okay the above code is called heirarchy inherritance ,a parent can have multiple child but each child should have seperate object 
# there is no relationship between childrens they just connected with parent class

#likewise a child can have more than one parent class by using , in () this is called multiple inherritance

class dad(): #parent
    def house(self):
        print("red")

class mom(): #parent
    def shop(self):
        print("white")

    def house(self):
        print("yellow")

class son(dad,mom): #child
    def market(self):
        print("fruits")

    def house(self):
        print("blue")

    def shop(self):
        print("green")

obj = son()
obj.house()
obj.shop()

# there is another one too called hybrid which is nothing but using all things together like multilevel, multiple, single, heirarchy inherritance combining this things is called hybrid inherritance












