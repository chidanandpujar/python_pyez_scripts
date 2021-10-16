class TestMethods:
    def test1(self):
        print("test1 is completed")
    def test2(self):
        print("test2 is completed")
    def test3(self):
        print("test3 is failed")

class results(TestMethods):
    def result(self):
        print("Tests Completed Successfully")
    def test3(self):
        super().test3()
        print("test3 is successful")


testexec1=results()
testexec1.test1()
testexec1.test2()
testexec1.test3()
testexec1.result()
