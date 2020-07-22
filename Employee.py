class Employee:
#Me and the boys
    def __init__(self, nameA, lastNameA):
        self.name = nameA
        self.lastName = lastNameA
        self.years = 0 #Ages working in the store
        self.salary = 200 #Not good for the newcomers.
    
    def betterSalary(self):
        self.salary = ((self.salary)*self.years + 1)/2
    
    def newYear(self):
        self.years += 1

class Admin (Employee):
#I'm the law
    def __init__(self, nameA, lastNameA):
        super().__init__(nameA, lastNameA)
        self.salary = 600
        self.leadership = 5
    
    def newYear(self):
        self.years += 1
        self.leadership += self.leadership
        if(self.leadership > 30):
            self.leadership = 30