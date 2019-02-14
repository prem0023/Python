class marks:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        s = marks(r1, r2)
        return s

    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1 > s2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)      # return self.m1, self.m2

a = marks(98, 86)
b = marks(79, 89)

s = a + b
print(s.m2)

print(a)                                            # print(a.__str__())

if a > b:
    print("a wins")
else:
    print("b wins")
