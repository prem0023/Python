a = 1
i = int(input("Enter the size of pyramind: "))

while a<=i:
    for j in range(a):
        print("#", end="")
        j = j+ 1

    a = a + 1
    print()
