from array import *

n = int(input("Enter a integer: "))
arr = array('I', [])

for a in range(n):
    arr.append(a)

newarr = array('I', (a*a for a in arr))

for b in newarr:
    print(b)
