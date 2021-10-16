class TestMethods:
    def test1(self):
        print("test1 is completed")
    def test2(self):
        print("test2 is completed")

class results(TestMethods):
    def result(self):
        print("Tests Completed Successfully")


testexec1=results()
testexec1.test1()
testexec1.test2()
testexec1.result()
