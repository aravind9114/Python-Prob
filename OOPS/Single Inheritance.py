class A:
    def display(self):
        print("Hello World")
class B(A):
    def display1(self):
        print("Single Inheritance")        
c=B()
c.display()
c.display1()