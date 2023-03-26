class employee:
    company = "google"
    def showDetails(self):
        print("this is an employer")

class programmer(employee):
    language = "python"
    def getLanguage(self):
        print(f"the language is {self.language}")
    def showDetails(self):
        print("this is an programmer   ")

e = employee()
e.showDetails()
p = programmer()
p.getLanguage()
p.showDetails
