class A:
    def __init__(self):
        print("outer class object creation")
    class B:
        def __init__(self):
            print("inner class object creation")
        def m1(self):
            print("inner class method")
a = A()
b = a.B()
b.m1()
