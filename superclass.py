class Person:
    country = "India"
    def __init__(self):
        print("initialiing person..\n")

    def teaching (self):
        print("i am teaching...")

class Employee(Person):
    company= "honda" 
    def __init__(self):
        super().__init__()
        print("initialiing employee..\n") 
        
    def getSalary(self):
        print(f"salary is {self.salary}")

    def teaching (self):
        super().teaching()
        print("i am an employee so i am teaching very good...")     

class Programmer(Employee):
    company="fiver"
    def getSalary(self):
        print(f"no salary to programmer")

    def teaching (self):
        super().teaching()
        print("i am an programmer so i am teaching very good ++++...") 


# p= Person()
# p.teaching()

e=Employee()
e.teaching()

# pr= Programmer()
# pr.teaching()