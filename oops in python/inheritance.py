# single inheritance
class A():
    def m1(self):
        print("A class m1 method")
class B(A):
    def m2(self):
        print("Child B is derived from A class: m2 method")
obj = B()
obj.m1()
obj.m2()

# multilevel inheritance
class A():
    def m1(self):
        print("Parent A class m1 method")
class B(A):
    def m2(self):
        print("Child class B is derived from A class: m2 method")
class C(B):
    def m3(self):
        print("Child class C derived from B: m3 method")
obj = C()
obj.m1()
obj.m2()
obj.m3()

# multiple inheritance
class P1:
    def m1(self):
        print("Parent1 method")
class P2:
    def m2(self):
        print("Parent2 method")
class C(P1,P2):
    def m3(self):
        print("Child method")
obj = C()
obj.m1()
obj.m2()
obj.m3()

# super() function
class A():
    def __init__(self):
        print("super class A constructor")
class B(A):
    def m1():
        print("Child B is derived from A class: m2 method")
b = B()

class A():
    def __init__(self):
        print("super class A constructor")
class B(A):
    def __init__():
        print("Child B is derived from A class: m2 method")
        super().__init__()
b = B()
