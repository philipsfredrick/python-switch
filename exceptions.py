# Syntax error
# x = 123
# if x ==123
# print("Hello")


# try:
#     print("try block")
#     print(10/0)
# except:
#     print("except: Handling code")
# else:
#     print("else block")
# finally:
#     print("finally block")

try:
    x = int(input("Enter a number between positive integer: "))
    if x < 0:
        raise ValueError(x)
except ValueError as e:
    print("You provided {}. Please provide positive integer values only".format(e))