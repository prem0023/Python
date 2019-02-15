def sort(list):

    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                a = list[j]
                list[j] = list[j+1]
                list[j+1] = a



list = [22,25,9, 10, 11,29,1, 3, 5, 7, 8,42,48,52,59,66, 15,35,36,39]

sort(list)
print(list)
