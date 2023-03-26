class employee:
    salary = 100
    location = "Delhi"
    


    @classmethod
    def changeSalary(cls, sal):
        cls.salary=sal

e = employee()
print(e.salary)
e.changeSalary(455) 
print(e.salary)