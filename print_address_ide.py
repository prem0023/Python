def  new(x):
    print(id(x))
    x = 10
    print(id(x))
    print("x", x)


a = 5
print(id(a))
new(a)
