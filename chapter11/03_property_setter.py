class employee:
    location = "Delhi"
    salary = 5600
    salarybonus = 500

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus
    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

       

e = employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus)
