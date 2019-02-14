n = int(input("Enter the number: "))
x = 0
b = 1
a = 0
print(1, end = " ")
for i in range(1, n):
    x = a + b
    a = b
    b = x
    print(x, end = " ")
