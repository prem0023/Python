def list(lst):
    lst[1] = 25
    print("lst", lst)


lst1 = [10,20,30]
print("lst1", lst1)
list(lst1)
print("lst1x", lst1)
