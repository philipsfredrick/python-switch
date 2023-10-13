# from abc import *
# class Demo1(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass
#     def m3(self):
#         print("Implemented method")
# cy = Demo1()

from abc import ABC,abstractmethod
# Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")
    @abstractmethod
    def interest(self):
        "Abstract Method"
        pass
class Access(Bank):       #sub class/ child class of abstract class.
    def interest(self):
        "Implementation of abstract method"
        print("In access bank #5000 interest")

s = Access()
s.bank_info()
s.interest()
