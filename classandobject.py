class Employee:
    company="Google"
    def getSalary (self ,signature):
        print(f"Salary for the employee {self.company} is {self.salary} \n {signature}")

harry=Employee()
harry.salary=100

harry.getSalary("Thanks")


