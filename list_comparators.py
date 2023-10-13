##print([1,2,3] < [2,2,3])
##print([1,2,3] < [1,2,3])
##print([1,2,3] <= [1,2,3])
##print([1,2,3] < [1,2,4])
##print([1,2,3] < [0,2,3])
##print([1,2,3] == [1,2,3])


##x = ["abc", "def", "ghi"]
##y = ["abc", "def", "ghi"]
##z = ["ABC", "DEF", "GHI"]
##a = ["abc", "def", "ghi", "jkl"]
##print(x == y)
##print(x == z)
##print(z == a)

## mebership operators in, not in

##a = [80,90]
##b = [10,20,30,a]
####a.extend(b)
####b.reverse()
##print(b)
##
##temp = []
##for i in b:
##    if type(i) == list:
##        for x in i:
##            temp.append(i)
##    else:
##        temp.append(i)
##print(temp)

## filter function
##items_cost = [999, 888, 1100, 1200, 1300, 777]
##gt_thousand = filter(lambda x:x> 1000, items_cost)
##x = list(gt_thousand)
##print("Eligible for discount: ", x)
##
#### map function
##without_gst_cost = [100,200,300,400]
##with_gst_cost = map(lambda x: x+10, without_gst_cost)
##x = list(with_gst_cost)
##print("Without GST items costs:", without_gst_cost)
##print("With GST items costs:", x)
##
#### reduce function
##from functools import reduce
##each_items_costs = [111,222,333,444]
##total_cost = reduce(lambda x,y:x+y, each_items_costs)
##print(total_cost)

## list comprehension
##x = [1,2,3,4]
##y = [i*2 for i in x]
##print(y)

s = range(1,20,3)
for i in s:
    print(i)
m = [x for x in s if x%2==0]
print(m)
