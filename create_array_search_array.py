from array import *

arr = array('i',[])
n = int(input("Enter the size of array: "))
for i in range(n):
    x = int(input("Enter the next number: "))
    arr.append(x)
print(arr)
print(arr[1])


a = int(input("Enter the number to search"))
k = 0
for e in arr:
    if e == a:
        print(k)
        break
    k +=1

print(arr.index(a))
