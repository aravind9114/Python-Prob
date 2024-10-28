class Calc:
    sum=0
    def add(self,x,y):
        sum=x+y
        print(sum)
class A(Calc):
    sum=0
    def add(self,x,y,z=0):
        sum=x+y+z
        print(sum)
c=A()
c.add(2,3)