class A:

    def __init__(self):
        print(" In A init")

    def feature1(self):
        print(" In feature 1 working")

    def feature2(self):
        print(" In feature 2 working")


class B:

    def __init__(self):

        print(" In B init")
                                            #we can also write "super().__init__()"

    def feature3(self):
        print(" In feature 3 working")

    def feature4(self):
        print(" In feature 4 working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print(" In C init")

b = C()
