from abc import ABC,abstractmethod
class Senior(ABC):
    def add(self):
        x=int(input("Enter x"))
        y=int(input("Enter y"))
        print(x+y)
    def sub(self):
        x=int(input("Enter x"))
        y=int(input("Enter y :"))
        print(x-y)
    @abstractmethod
    def div(self):
        pass
class Junior(Senior):
    def multi(self):
        x=int(input("Enter x :"))
        y=int(input("Enter y :"))
        print(x*y)
    def div(self):
        x=int(input("Enter x :"))
        y=int(input("Enter y :"))
        print(x/y)
obj=Junior()
obj.multi()
