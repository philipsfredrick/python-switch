class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        print("message from constructor")
    
    def display(self):
        print("Hello my id is: ",self.id)
        print("My name is : ",self.name)

e1 = Employee(1,"Nonso")
e1.display()
e2= Employee(2,"Okon")
e2.display()

# # emp = Employee()

# emp_obj = Employee()
# emp_obj.display()

# emp_obj1 = Employee()
# emp_obj1.display()