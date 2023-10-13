class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def __str__(self):
        return "This is Student object with name %s and roll no %d" % (self.name,self.rollno)
        # return "This is Student object with name {} and roll no {}".format(self.name,self.rollno)

    
s1 = Student("Non",10)
s2 = Student("Lol",12)
print(s1)
print(s2)