def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even+=1
        else:
            odd+=1
    return even, odd

lst = [25, 62, 8, 6, 9, 3, 4, 5, 7]

even, odd = count(lst)
print(even)
print(odd)

print("Even: {} and Odd: {}".format(even,odd))
