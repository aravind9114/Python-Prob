#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class Circle:
    def __init__(self,radius=0):
        radius=int(input("enter radius:"))
        self.radius=radius
    
    def Area(self):
        area=3.14*self.radius*self.radius
        print("AREA OF CIRCLE={} sq units".format(area))
    def Permeter(self):
        perimeter=2*3.14*self.radius
        print("PERIMETER OF CIRCLE={} units".format(perimeter))
    
c=Circle()
c.Area()
c.Permeter()
