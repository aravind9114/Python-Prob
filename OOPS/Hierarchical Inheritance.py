class A:
    def display(self):
        print("Function of A")
class B(A):
    def display1(self):
        print("Function of B")  
class C(A):
    def display3(self):
        print("Function of C")   
c=B()
c.display()
c.display1()
d=C()
d.display()
d.display3()