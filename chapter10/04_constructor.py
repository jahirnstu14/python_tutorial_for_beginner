class Emplyee:
    company = "google"



    def __init__(self, name,salary, subnit):
        self.name = name
        self.salary=salary
        self.subnit=subnit
        print("emplyee is created")
    
    def getDetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the name of the employee is {self.salary}")
        print(f"the name of the employee is {self.subnit}")



harry = Emplyee("harry", 100, "youtube")
harry.getDetails()

