class A:
    def display(self):
        print("Function of A")
class B:
    def display1(self):
        print("Function of B")
class C(A,B):
    def display3(self):
        print("Function of C")
class D(B):
    def display4(self):
        print("Function of D ")
c=D()
c.display1()
c.display4()
d=C()
d.display()
d.display1()
d.display3()