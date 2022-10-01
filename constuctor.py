class Employee:
    def __init__(self ,a,b,c):
        self.name=a
        self.salary=b
        self.submit=c
        print("emploee is created")
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The name of the employee is {self.submit}")


harry=Employee("Harry" , 100, "youtube")
harry.getDetails()

