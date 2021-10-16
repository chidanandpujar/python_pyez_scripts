class test:
    """ test doc string"""
    class_variable="class variable"
    a=10
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def printxy(self):
        print(self.x)
        print(self.y)


if __name__ == "__main__":
    t1=test(3,4)
    t1.printxy()
    print(t1.class_variable)
    t2=test(4,5)
    t2.printxy()
    print(t2.class_variable)
    print(test.__doc__)
    print(test.a)
