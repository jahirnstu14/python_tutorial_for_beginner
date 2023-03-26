class Calculator:
    def __init__(self, num):
        self.number=num

    def square(self):
        print(f"the value of {self.number} squre is {self.number **2}")
    def squareRoot(self):
        print(f"the value of {self.number} squre is {self.number **0.5}")
    def cube(self):
        print(f"the value of {self.number} squre is {self.number **3}")

a= Calculator(9)   
a.square()
a.squareRoot()
a.cube()
