# lambda syntax- lambda(keyword) arguments : expression
from functools import reduce


# s = lambda x,y : x + y
# print(s(10,20))

# x = [1,2,3,4,5,6]

# t = lambda x : len(x)
# print(t(x))

# # In-built methods that work with lambda - map(every element), filter(selected elements), reduce(one single output)
# # Syntax method e.g map(lambda expression, collection). Return type for map is collection, can convert to any collection
# print(type(range(5)))

# l = [10,20,30,40,50,60]
# s = map(lambda x : x**2, l)
# print(type(s))
# print(s)
# print(list(s))

# l = [10,20,30,40,50,60]
# s = filter(lambda x: x > 20, l)
# print(s)
# print(list(s))

# m = [1,2,3,4,5,6,7,8,9,10]
# c = filter(lambda x: x% 2== 0, m)
# print(c)
# print(list(c))

# l = [1,2,10,15]
# s = reduce(lambda x,y: x + y, l)
# print(s)

# num = int(input("Enter Number: "))
# f = reduce(lambda x,y : x * y, range(1,num + 1))
# print(f)

# Rules for defining a reccursive function. A function that calls itself is a recursive function
# 1. The body of a recursive function is a select statement i.e if/elif/else.
# 2. The if condition handles the stopping condition or base call or false condition. Which when holds True, the function initiates true.
# for recursive functions, you must first identify your false condition
# 3. The else part generally deals with the work and recursive recall.
# 4. Every recursive function should have at least 1 argument, which must be changed at every recall.
# NB: If you have single variable go for recursion, if very multiple go for loop. Recursion uses more memory.
# NB: Any iterative element can be converted to a recursive call.
# def p(x):
#     if x == 11:
#         return
#     else:
#         print(x)
#         p(x + 1)
# print(p(1))


def sum(num):
    if num == 0:
        return 0
    else:
        return (num % 10 + sum(num//10))
print(sum(13764))

def product(num):
    if num == 0:
        return 1
    else:
        return (num % 10 * product(num//10))
print(product(13764))

c = filter(lambda x: sum(x) == product(x), range(1,1001))
print(list(c))