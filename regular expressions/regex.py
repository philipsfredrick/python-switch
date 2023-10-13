import re

# count = 0
# pattern = re.compile("ab")
# matcher = pattern.finditer("abaababa")
# for match in matcher:
#     count += 1
#     print(match.start(),"...",match.end(),"...",match.group())
#     print("The number of occurences:", count)

# count = 0
# matcher = re.finditer("ab", "abaababa")
# for match in matcher:
#     count += 1
#     print(match.start(),"...",match.end(),"...",match.group())
#     print("The number of occurences:",count)

# matcher = re.finditer("[^a-zA-Z0-9]", "a7b@k9z")
# for match in matcher:
#     print(match.start(),"...",match.group())

# print()
# matcher = re.finditer("[0-9]", "a7b@k9z")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()
# matcher = re.finditer("[abc]", "a7b@k9z")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()
# matcher = re.finditer("[a-z]", "a7b@k9z")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()
# matcher = re.finditer("[a-zA-Z0-9]", "a7b@k9z")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()
# matcher = re.finditer("[^abc]", "a7b@k9z")
# for match in matcher:
#     print(match.start(),"...",match.group())

# predefined character classes: \s,\S,\d,\D, \w, \W, .
# matcher = re.finditer("\s", "a7b @k9z")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()

# matcher = re.finditer("\S", "a7b @k9z")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()

# matcher = re.finditer("\d", "a7b @k9z")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()

# matcher = re.finditer("\D", "a7b @k9z")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()

# matcher = re.finditer("\w", "a7b @k9z")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()

# matcher = re.finditer("\W", "a7b @k9z")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()

# matcher = re.finditer(".", "a7b @k9z")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()

# Quantifiers in Python - {m,n} -> minimum and maximum
# matcher = re.finditer("a", "abaabaaab")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()

# matcher = re.finditer("a+", "abaabaaab")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()

# matcher = re.finditer("a*", "abaabaaab")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()

# matcher = re.finditer("a?", "abaabaaab")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()

# matcher = re.finditer("a{3}", "abaabaaab")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()

# matcher = re.finditer("a{2,4}", "abaabaaab")
# for match in matcher:
#     print(match.start(),"...",match.group())
# print()

# matcher = re.finditer("[a-zA-Z0-9]+.[a-zA-Z0-9]{3}@[a-zA-Z0-9]+.[a-zA-Z0-9]{3}", "segun.ade@gmail.com")
# for match in matcher:
#     print(match.start(),"...",match.end(),match.group())
# print()

# matcher = re.finditer("[^a-zA-Z][\d+]{0,10}", "08169261156")
# for match in matcher:
#     print(match.start(),"...",match.end(),match.group())
# print()

# class activity solution
# matcher = re.finditer("\w+\.\w+@\w+\.\w{3}", "segun.ade@gmail.com")
# for match in matcher:
#     print(match.start(),"...",match.end(),match.group())
# print()

# matcher = re.finditer("\d{11}", "08169261156")
# for match in matcher:
#     print(match.start(),"...",match.end(),match.group())
# print()

# s = input("Enter pattern to check: ")
# m = re.search(s, "abaaaba")
# if m != None:
#     print("Match is available")
#     print("First occurence of match with start index:",m.start(),"and end index:",m.end())
# else:
#     print("Match is not available")

# findall method finds all occurences. Returns a list
# l = re.findall("[0-9]", "a7b9c5kz")
# print(l)

# # in a target string, matched pattern will be replaced with provided replacement.
# s = re.sub("[a-z]","#", "a7b9c5kz")
# print(s)

# t = re.subn("[a-z]","#", "a7b9c5kz")
# print(t)
# print("The Result String:", t[0])
# print("The number of replacements:", t[1])

# m = re.split(",","KGF,BB1,BB2")
# print(m)
# for t in m:
#     print(t)

s = input("Enter Mail id: ")
m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
if m!=None:
    print("Valid Mail Id")
else:
    print("Invalid Mail id")