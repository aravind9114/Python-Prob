class A:
    def display(self):
        print("Function of A")
class B(A):
    def display1(self):
        print("Function of B")  
class C(B):
    def display3(self):
        print("Multilevel Inheritance")      

d=C()
d.display()
d.display1()
d.display3()