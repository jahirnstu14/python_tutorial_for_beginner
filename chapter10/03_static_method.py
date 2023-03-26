class Emplyee:
    company = "google"



    def getSalary(self, signature):
        print(f"salary for this employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("good morning, sir")

harry = Emplyee
harry.salary = 10000
harry.getSalary("thanks")#emplyee.getSalary(harry)
harry.greet()#emplyee.greet()