class Person:
    def __init__(self,name,age,loc,job,salary):
        self.name=name
        self.age=age
        self.loc=loc
        self.job=job
        self.salary=salary
    
       
    def display_personal(self):
        print("=================display personal function==================")
        print("Name={}".format(self.name))
        print("Age={}".format(self.age))
        print("Location={}".format(self.loc))
    
    def Occupation(self):
        print("===============occupation function==================")
        print("Designation={}".format(self.job))
        print("Salary={}".format(self.salary))
        
        
    
    def Full_details(self):
        print("=================full details function=======================")
        self.display_personal()
        self.Occupation()

p=Person("Aravind",25,"Kannur","Developer",20000)
p.display_personal()
p.Occupation()
p.Full_details()


        