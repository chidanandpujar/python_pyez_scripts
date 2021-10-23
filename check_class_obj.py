class printvar:
    def __init__(self,x,y):
       self.x=x
       self.y=y

    def printxy(self):
        print(self.x)
        print(self.y)

class addvar:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def addxy(self):
        print(self.x+self.y)


class multvar:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def multxy(self):
        print(self.x * self.y)


class subtvar:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def subxy(self):
        print(self.x - self.y)


class myclass:
    """ This is class test"""
    class_var = 10
    def test_function(self):
        print("Hello")

print(myclass.class_var)
print(myclass.__doc__)

x = printvar(1,2)
x.printxy()

y = addvar(1,2)
y.addxy()

z= multvar(1,2)
z.multxy()

m= subtvar(10,2)
m.subxy()

