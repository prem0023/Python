def person(name, **detail):
    print(name)

    for a,b in detail.items():
        print(a,b)

person('prem', age=20, city='kolkata', mob=8949455)
