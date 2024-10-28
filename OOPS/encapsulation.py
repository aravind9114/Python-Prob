#####################################protected
"""""
class A:
    def __init__(self):
        self._x="PYTHON"
class B(A):
    def __init__(self):
        A.__init__(self)
        print("protected:",self._x)
        self._x="dddd"
        print(self._x)
c=B()
d=A()
print("of B",c._x)
print("of A",d._x)"""
######################################private
class A:
    def __init__(self):
        self.__x="PYTHON"
        self.a="DEV"
    def accessprivate(self):
        print(self.__x)
class B(A):
    def __init__(self):
        A.__init__(self)
        #print("protected:",self.__x)
        #self.__x="dddd"
        #print(self.__x)
c=B()
d=A()
print(d.a)
d.accessprivate()
#print("of B",c.__x)
#print("of A",d.__x)
