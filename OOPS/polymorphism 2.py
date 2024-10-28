class Person:
    def details(Self):
        print("a human being regarded as an individual.")
    def features(self):
        print("Physical characteristics are defining traits or features of a person's body. \nThese are aspects of appearance that are visually apparent to others, even with no other information about the person.\nThey can include a variety of things. ")
class Aravind(Person):
    def details(self):
        print("============Details==========")
        print("NAME = ARAVIND")
        print("AGE = 25")
c=Person()
c.details()
c.features()
d=Aravind()
d.details()  
d.features()