# f = open("abc.txt", 'w')
# print("File Name:", f.name)
# print("File Mode:", f.mode)
# print("Is FIle Readable:", f.readable())
# print("Is File Writable:", f.writable())
# print("Is File Closed:", f.closed)
# f.close()
# print("Is File Closed:", f.closed)


# f = open("wish.txt", 'w')
# f.write("Welcome\n")
# f.write("to\n")
# f.write("python world\n")
# print("Data was written successfully")
# f.close()

# f = open("wish.txt", 'a')
# f.write("Welcome\n")
# f.write("to\n")
# f.write("python world\n")
# print("Data was written successfully")
# f.close()

# writelines method for list of strings.
# f = open("wish.txt", 'a')
# list = ["Welcome", "Programming", "Interswitch", "Software"]
# f.writelines(list)
# print(f.writelines(list))
# f.close()

# # methods to read: read(), read(n), readline(), readlines()
# f = open("wish.txt", "r")
# data = f.read()
# print(data)
# f.close()

# f = open("wish.txt", "r")
# data = f.read(20)
# print(data)
# f.close()


# f = open("wish.txt", "r")
# lines = f.readlines()
# for line in lines:
#     print(line, end='')
# f.close()

# f = open("wish.txt", "r")
# print(f.tell())
# print(f.read(2))
# print(f.tell())
# print(f.read(3))
# print(f.tell())

import csv
with open("emp.csv", "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["EMP NO", "EMP NAME", "EMP SAL", "EMP ADDR"])
    n = int(input("Enter Number of EMployess:"))
    for i in range(n):
        eno = input("Enter employee No: ")
        ename = input("Enter Employee Name:")
        esal = input("Enter Employee Salary: ")
        eaddr = input("Enter Employee Address: ")
        w.writerow([eno, ename, esal, eaddr])
print("Total employee data written to csv successfully")