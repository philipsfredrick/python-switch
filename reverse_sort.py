##n = [1,2,3,4,5,"two"]
##print(n)
##n.reverse()
##print(n)
##
##y = [1,4,5,2,3]
##n.sort
##print(n)
##
##s = ["ada", "obi", "ajax"]
##s.sort(reverse=True)
##print(s)
##
##print(sorted(s, reverse=True))

## aliasing and cloning of list
x = [10,20,30]
y = x
print(x)
print(y)
print(id(x))
print(id(y))
x[1] = 99
print(x)
print(y)
print(id(x))
print(id(y))

y = x.copy()
print(x)
print(y)
print(id(x))
print(id(y))


