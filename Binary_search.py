
pos = 0

def search(list, n):
    i = 0
    u = len(list)-1

    while i <= u:
        mid = (i + u) // 2

        if list[mid] == n:
            global pos
            pos = mid
            return True
        else:
            if list[mid] > n:
                u = mid
            else:
                i = mid

list = [1, 3, 5, 7, 8, 9, 10, 11, 15, 22,25,29,35,36,39,42,48,52,59,66]
print(list)
n = int(input("Enter the number to search from the list: "))


if search(list,n):
    print("Found ", pos + 1)
else:
    print("Not Found")
