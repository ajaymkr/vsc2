class Employee:
    company="bharat gas"
    salary=5600
    salaryBonus=500

    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus

e=Employee()
print(e.totalSalary)
