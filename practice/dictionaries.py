# Dictionaries in python. A datatype with  key-value pairs.
phonebook = {}
phonebook["John"] = 9745673892
phonebook["Jack"] = 4545924920
phonebook["Jill"] = 34835709020
print(phonebook)

# Alternative
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)
# iterate through dictionaries
for name,number in phonebook.items():
    print("Phone number of %s is %d" %(name, number))

del phonebook["John"]
print(phonebook)

phonebook["John"] = 9684732052
print(phonebook)

phonebook.pop("John")
print(phonebook)