class laptop:

    city = "bokaro"

    def __init__(self):
        self.name = "Prem"
        self.age = 20

    def update(self):
        self.age = 20

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False



a = laptop()
b = laptop()

a.name = "Riya"
a.age = 18

a.update()

print("Name", a.name)
print("age", a.age)
print("City", a.city)
print("Name", b.name)
print("age", b.age)
print("City", b.city)

if a.compare(b):
    print("They are same")
else:
    print("They are not same")
