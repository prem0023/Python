n = int(input("Enter thr size of pyramnid: "))

for i in range(n):

    for j in range((n-i-1),0,-1):
        print(" ",end = "")

    for j in range(i):
        print("*",end = "")

    for j in range(1,i,1):
        print("*", end="")



    print("\n")
