## variable length argument algorithm(print 1-10)
##def sqlength(*y):
##   for i in y:
##       if(i >= 1 and i <= 10):
##           print(i*i,end=" ")
##sqlength(1,2,3,4,5,6,7,8,9,10,11)

## guess game. List between 5 - 50, if input equal list item congrats, else game over.
## user only has 3 tries.
## second part- if game over prompt for restart.


## dictionary like **variable length keyword
##def print_kwargs(**kwargs):
##    print(kwargs)
##print_kwargs(id=1, name="Jack", qualification="MBA")
##
##def m1(**x):
##    for k,v in x.items():
##        print(k,"=",v)
##m1(a=10, b=20, c=30, d=40, e=50)
##m1(id=100, name="Nonso", gender="male", role="student", subject="maths")
##

##a =1
##def m():
##    a = 2
##    print(a)
##    print(globals()["a"])
##m()

##def factorial(n):
##    if n == 0:
##        result = 1
##    else:
##        result = n * factorial(n-1)
##    return result
##x = factorial(4)
##print("Factorial of 4 is: ", x)

add = lambda a,b: a+b
x = add(4,5)
print(x)
