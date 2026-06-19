# poly means 'many' morphism means 'form'

class dad(): #parent
    def house(self):
        print("red")

class son(dad): #child

    def house(self):
        print("yellow")

obj = son()
obj.house()

# polymorphism is nothing but just overriding the method like we did in inheritance