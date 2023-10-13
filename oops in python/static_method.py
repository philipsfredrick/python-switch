# class Demo:
#     @staticmethod
#     def m3():
#         Demo.z = 20
# Demo.m3()
# # obje = Demo()
# # obje.m3()
# print(Demo.__dict__)

class Demo:
    @staticmethod
    def sum(x,y):
        print(x+y)
    @staticmethod
    def multiply(x,y):
        print(x*y)
Demo.sum(2,3)
Demo.multiply(2,4)