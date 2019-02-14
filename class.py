class laptop:

    def __init__(self, cpu, ram):
        self.cpuu = cpu
        self.ramm = ram

    def  config(self):
        print("config is", self.cpuu, self.ramm)

a = 5
print(type(a))

comp1 = laptop('intel', '16gb')
comp2 = laptop('imd', '8gb')

print(type(comp1))
print(type(comp2))
comp1.config()

laptop.config(comp2)
