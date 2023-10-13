class Demo:
    @classmethod
    def m2(cls):
        Demo.b = 30
obj = Demo()
obj.m2()
print(Demo.__dict__, end=", ")

