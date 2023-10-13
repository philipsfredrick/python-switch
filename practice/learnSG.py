# s = "Strings are awesome!"
# # Length should be 20
# print("Length of s = %d" % len(s))

# # First occurrence of "a" should be at index 8
# print("The first occurrence of the letter a = %d" % s.index("a"))

# # Number of a's should be 2
# print("a occurs %d times" % s.count("a"))

# # Slicing the string into bits
# print("The first five characters are '%s'" % s[:5]) # Start to 5
# print("The next five characters are '%s'" % s[5:10]) # 5 to 10
# print("The thirteenth character is '%s'" % s[12]) # Just number 12
# print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
# print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# # Convert everything to uppercase
# print("String in uppercase: %s" % s.upper())

# # Convert everything to lowercase
# print("String in lowercase: %s" % s.lower())

# # Check how a string starts
# if s.startswith("Str"):
#     print("String starts with 'Str'. Good!")

# # Check how a string ends
# if s.endswith("ome!"):
#     print("String ends with 'ome!'. Good!")

# # Split the string into three separate strings,
# # each containing only a word
# print("Split the words of the string: %s" % s.split(" "))

# name = "John"
# age = 24

# if name == "John" and age == 23:
#     print("Yeah this is John")
# else:
#     print("This is not John")

# # boolean logical operators: and, or, not, xor

# primes = [2,3,4,5]
# for x in primes:
#     print(x)
# for x in range(5):
#     print(x)
# for x in range(3,8,2):
#     print(x)

# count = 0
# while count < 5:
#     print("This is count %s" %count)
#     count += 1

# cant = 0
# while True:
#     print("This is can't %s" %cant)
#     cant += 1
#     if cant >= 5:
#         break

# for x in range(10):
#     if x % 2 == 0:
#         continue
#     print(x)

# numbers = [
#     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#     743, 527
# ]

# for number in numbers:
#     print(number)
#     if number == 237:
#         break

# def list_benefits():
#     return ["More organized code", 
#             "More readable code", "Easier code reuse",
#             "Allowing programmers to share and connect code together"]
# def build_sentence(benefit):
#     return benefit + " is a benefit of functions!"
# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))

# name_the_benefits_of_functions()

# def list_benefits():
#     return ["More organized code", "More readable code", 
#             "Easier code reuse", 
#             "Allowing programmers to share and connect code together"]
# def build_sentence(benefit):
#     return benefit + " is a benefit of functions!"
# def list_function_benefits():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))
# list_function_benefits()

# # for loop example S.G
# str = "Python"
# for x in str:
#     if x in "aeiou":
#         continue
#     print(x, end=" ")
# else:
#     print("Complete")

# for x in str:
#     if x in "aeiou":
#         break
#     print(x)
# else:
#     print("Complete")
# sum of digits algorithm
# num = 12345
# sum = 0
# while num > 0:
#     sum += num % 10
#     num = num // 10
# print(sum)

# product of digits.
# num = 12345
# product = 1
# while num > 0:
#     product *= num % 10
#     num = num // 10
# print(product)

# 
# l = [123,754,21]
# for num in l:
#     sum = 0
#     for i in str(num):
#         # convert i to str for iteration
#         sum += int(i)
#         # convert back to int to add or sum.
#     print(sum)

# positional arguments
# default kewords. Default values for trailing arguments

# def add(a = 20, b):
#     return a + b
# print(add(10))
# print(add(a = 34, b = 24))

# def data(**k):
#     print(k)

# print(data())
# print(data(a=1, b=2,c=3,d=4))

# Classes and Objectts in Python: 
class MyClass:
    my_variable = "blah"
    
    def function(self):
        print("Print this is my own self function")

myObject = MyClass()
xObject = MyClass()
myObject.function()
xObject.my_variable = "yackcity"
print(myObject.my_variable)
print(xObject.my_variable)


class NumberHolder:

    def __init__(self, number):
        self.number = number