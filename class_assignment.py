## Q1. Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y","me","s", "lly"]
# ## expected output = ["My","name","is","Kelly"]
# ##s = list1 + list2
# ##print(s)
# def conct(list1, list2):
##for i in list1:
    

## Q2 Remove all occurrences of a specific item from a list
# list3 = [5,20,15,20,25,50,20]
## expected [5,15,25,50]
##def removeItem(list3, item):
##    for i in list3:
##        if i == item:
##            list3.remove(i)
##    return list3
##print(removeItem(list3, 20))

## Create a string made of the middle three characters
## Case 1: str1 = "JhonDipPeta" -> Dip
## Case 2: str2 = "JaSonAy" -> Son

##
##print(len("JhonDipPeta"))
##str1 = "JhonDipPeta"
##def stringChars(str1):
##    endIndex = len(str1) - 1
##    midIndex = (endIndex // 2) -1
##    for i in str1:
##        return str1[midIndex:midIndex + 2

##print(stringChars(str1))

## Q4 Write a program to create a recursive function to calculate the sum
## of numbers from 0 to 10
##listx = [0,1,2,3,4,5,6,7,8,9,10]
##
##print(listx)
##def printNums(x):
##    if x < 0 or x > 10:
##        return 1
##    else:
##        return  (x + printNums(x-1))
##    return x
##print(printNums(10))

## Find the largest item from a given list using list comprehension
# x = [4,6,8,24,12,2]
# m = [i for i in x if i > i - 1]
# print(m)

## Q1. Write a program which takes 5 names in a list.
##Sort the list based on the string length

## Q2. Write a program which has a list of trainees': fullname.
## Create a dictionary where the initials is the key, and the name is the value.
## Note, you can use dictionary comprehension with this.
