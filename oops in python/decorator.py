import time
import math

# def hello_decorator(func):
#     def inner1():
#         print("This occurs before function execution")
#         func()
#         print("This exists after the function execution")
#     return inner1
    
# def func_to_be_used():
#     print("This is inside the function !!")

# func_to_be_used = hello_decorator(func_to_be_used)
# func_to_be_used()

def calculate_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time takin in: ",func.__name__,end - begin)
    return inner1

@calculate_time
def factorial1(num):
    time.sleep(2)
    print(math.factorial(num))

factorial1(10)