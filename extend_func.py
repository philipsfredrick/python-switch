##extend() method
##
##result = 0
##def mySum(txns):
##    result = 0
##    for x in txns:
##        result += x
##    return result
##
##august_txns = [100,200,500,600,400,500,900]
##sept_txns = [111,222,333,600,790,100,200]
##print("August month transactions are:",august_txns)
##print("September month transactions are:", sept_txns)
##sept_txns.extend(august_txns)
##print(sept_txns)
####print(sum(sept_txns))
##print("August and Sept total transactions amount:", mySum(sept_txns))

## has ValueError if item not present
##n = [1,2,3]
##n.remove(1)
##print(n)

## has IndexError if index out of range
n = [1,2,3,4,5]
print(n.pop())
print(n.pop(10))
