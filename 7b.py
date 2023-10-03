class emp:
    def __init__(self):
        self.name=" "
        self.ID=0
        self.dept=" "
        self.salary=0

    def getdetails(self):
        self.name=input("enter name: ")
        self.ID=int(input("enter ID: "))
        self.dept=input("enter department: ")
        self.salary=int(input("enter salary: "))
    
    def showdetails(self):
        print("Name: ",self.name)
        print("ID: ",self.ID)
        print("dept: ",self.dept)
        print("Salary: ",self.salary)

    def upsal(self):
        a=int(input('Enter the salary increment: '))
        print("updated salary is: ", self.salary+a)
    
e=emp()
e.getdetails()
e.showdetails()
e.upsal()