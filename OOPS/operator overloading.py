class B:
    def __init__(self,b):
        self.b=b
    def __add__(self,i):
        return self.b + i.b
    def __gt__(self, o):
        if(self.b>o.b):
            return True
        else:
            return False
    def __lt__(self, other):
        if(self.b<other.b):
            return "ob1 is lessthan ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self, other):
        if(self.b == other.b):
            return "Both are equal"
        else:
            return "Not equal"
    def __ne__(self, other):
        if(self.b == other.b):
            return "equal"
        else:
            return "not equal"
    
c1=B(44)
c2=B(10)
print(c1+c2)
print(c1.__add__(c2))
print(c1.__gt__(c2))
print(c1>c2)
print(c1<c2)
print(c1.__lt__(c2))
print(c1==c2)
print(c1.__eq__(c2))
print(c1.__ne__(c2))