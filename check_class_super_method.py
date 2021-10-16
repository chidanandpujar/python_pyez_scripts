class TestMethods:
    def test1(self):
        print("test1 is completed")
    def test2(self):
        print("test2 is completed")
    def test3(self):
        print("test3 is failed")

class results(TestMethods):
    def result(self):
        super().test1()
        super().test2()
        super().test3()
        print("Tests Completed Successfully")


testexec1=results()
testexec1.result()
