from inheritance import exportFile

class importFile(exportFile):
    def hi(self):
        print("how are you")

    def hello(self):
        print("hello, Im muthu kumar")

obj = importFile()
obj.hi()
obj.hello()


