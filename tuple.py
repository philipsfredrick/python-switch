## tuple
##name = ("Nonso")
##print(name)
##print(type(name))
##
##name1 = ("Nonso",)
##print(name1)
##print(type(name1))
##
##a = (11)
##print(a)
##print(type(a))
##
##a = (11,)
##print(a)
##print(type(a))
##
##details = ("Janet", "Lekki")
##print(type(details))
##
##
##odd = (tuple(range(1,16,2)))
##print(odd)
##print(type(odd))

##def signup():
##    username = input("Enter username: ")
##    password = input("Enter password: ")
##    detail= (username,password)
##    print(detail)
##    return detail
##print(signup())
##def login(username, password):
##    user = input("Enter your username: ")
##    passw = input("Enter your password: ")
##    saved = signup()
##    

##t = (10,20,30,40,50,60)
##print(t[2:5])
##print(t[2:100])
##print(t[::2])
##
##for i in t:
##    print(i)
##
##t2 = t *2
##print(t2)
##
####t[1] = 70
#### tuple methods: len(), count(), index(), sorted(), min(), max()
##t2 = min(t)
##print(t2)
##
##t1 = sorted(t,reverse=True)
##print(t1)

## tuple packing and unpacking
a,b,c,d = 10,20,30,40
x = a,b,c,d
print(x)

a,b,c,d = x
print("a=",a,"b=",b,"c=",c,"d=5",d)

userDetails = ("Nonso", "Male", 17)
name,gender,age = userDetails
##name,gender,age,contact = userDetails

print(name)
print(gender)
print(age)
##print(contact)

##studentDetails = ("Nonso", "Male", 17, "Maths", '2345')
##name,gender,age = studentDetails

studentDetails = ("Nonso", "Male", 17, "Maths", '2345')
name,gender, *anything = studentDetails
print(studentDetails)
print(anything)
