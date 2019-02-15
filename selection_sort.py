def sort(list):
    for i in range(len(list)):
        min = i
        for j in range(i,len(list)):
            if list[j] < list[min]:
                min = j

        a = list[i]                                 #swapping
        list[i] = list[min]
        list[min] = a



list = [22,25,9, 10, 11,29,1, 3, 5, 7, 8,42,48,52,59,66, 15,35,36,39]

sort(list)
print(list)
