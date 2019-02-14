class student:

    college = "RCCIIT"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def get_school(cls):
        return cls.college

    @staticmethod
    def get_info():
        print("I did it very well..")

s1 = student(62, 84, 29)
s2 = student(58, 29, 73)

print(s1.avg())
print(s2.avg())

print(s1.college)
print(s1.m1)

print(student.get_school())
student.get_info()
