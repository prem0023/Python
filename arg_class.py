class student:

    def __init__(self, name, std, marks,):
        self.name = name
        self.std = std
        self.marks = marks
        self.lap = self.laptop()

    def detail(self):
        print(self.name, self.std, self.marks)
        self.lap.lappi()


    class laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "intel"
            self.ram = "8gb"

        def lappi(self):
            print(self.brand, self.cpu, self.ram)


s1 = student("prem", 12, 89)
s1.detail()

