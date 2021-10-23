class cls_methods:
    """" Demo of class methods  regular, static and class methods """
    def regular(self):
        print(" checking regular method")
        print("regular methods must and should have self as argument")
        print("regular methods can be called from instantiated objects")

    @staticmethod
    def static_method():
        print("checking static methods")
        print("static methods are decorated with @staticmethod")
        print("static methods can be called with class name")
        print("static methods can be called with instantiated object name")
        print("static methods does not take args or params")

    @classmethod
    def class_method(cls):
        print("checking class methods")
        print("class methods are decorated with @classmethod")
        print("class methods can be called from class name")
        print("class metohds can be called from instantiated object name")


cls1 = cls_methods()
cls1.regular()
cls_methods.static_method()
cls_methods.class_method()

