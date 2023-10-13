## defining a function
##def sum(a,b):
##    print("Sum of two values=", (a + b))
##sum(20,30)


##def area():
##    base = int(input("Input base of triangle: " ))
##    height = int(input("Input height of triangle: "))
##    num = (1/2) * base * height
##    print(num)
##area()

##def areaTriangle(base, height):
##    num = (1/2) * base * height
##    print(num)
##
##x = int(input("Enter your base value: "))
##y = int(input("Enter your height: "))
##
##areaTriangle(x,y)

##def areaTriangle(base, height):
##    num = (1/2) * base * height
##    return num
##
##x = int(input("Enter your base value: "))
##y = int(input("Enter your height: "))
##
##result = areaTriangle(x,y)
##print("Area of numbers is: ", result)

## multiple return values for a function in python
##def multiple(a, b):
##    c = a+b
##    d = a-b
##    return c,d
##x,y = multiple(10,5)
##print("sum of a and b: ", x, end=" ")
##print("subtraction of a and b: ", y)

## passing function as parameter to another function in python

##def display(x):
##    print("This is a display function")
##def message():
##    print("This is a message function")
##display(message())


## NB: Assign function to a variable and passing function as function combined.

##def display(x):
####    print("This is a display function")
##    x("Nonso")
##    
##def message(name):
####    print("This is a message function")
##    print("Testing for a different behaviour")
##    print("Hello ", name)
##display(message)


## keyword arguments
##def cart(item, price):
##    print(item, "cost:", price)
##cart(item="bangles", price = 20000)
##cart(item="handbag", price=100000)
##cart(price=1200, item="shirt" )

## variable-length arguments
def total_cost(x, *y):
    pass
##    sum = 0
##    for i in y:
##        sum+=i
##    print(x + sum)
##total_cost(100, 200)
##total_cost(110, 226, 311)
##total_cost(11,)
total_cost()
