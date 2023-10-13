group = [1,2,3,4]
search = int(input("Enter the element in search: "))
for element in group:
    if search == element:
        print("element found in group")
        break
else:
    print("Element not found")
cart = [10,20,500,700,50,60]
for item in cart:
    if item>=500:
        continue
    print("item: ", item)
total = 0
# loop will run at least once
while True:
   num = int(input("Enter a number(Not 0): "))
   if num ==0:
       break
   total += num
print("Total: ", total)
