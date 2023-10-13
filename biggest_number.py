##x = int(input("Enter the first number: "))
##y = int(input("Enter the second number: "))
##if x > y:
##    print("Biggest number is: ", x)
##else:
##    print("Biggest number is: ", y)


while True:
    num = int(input("Enter first number(or -1 to exit): "))
    num2 = int(input("Enter second number: "))
    if num > num2:
        print(num)
        print("Exit with -1")
    elif num == -1 or num2 == -1:
        break
