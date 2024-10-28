class A:
    def display(self):
        print("Funstion of A")
class B:
    def display1(self):
        print("Function of B")
class C(A,B):
    def display3(self):
        print("Function of C")        
c=C()
c.display()
c.display1()
c.display3()
