from abc import ABC,abstractmethod
class University(ABC):
    
    @abstractmethod
    def college(self):
        pass
   
class College(University):
    def college(self):
         self.collegename=input("enter name:")
         self.location=input("enter loc:")
         print("College Name:",self.collegename)
         print("College Location:",self.location)
c=College()
c.college()