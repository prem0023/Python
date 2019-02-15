pos = 0

def search(list, n):
    i = 0

    while i < len(list):
        if n ==list[i]:
            global pos                  #globals()['pos']=i
            pos = i
            return True
        i = i + 1

    return False

list = [1,2,3,4,22,27,0,5,6,12,25,55,7,8,9,10]

n = int(input("Enter an integer to search in list: "))

if search(list,n):
    print("Found ", pos )
else:
    print("Not Found")
