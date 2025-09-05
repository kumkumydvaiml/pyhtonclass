class Student:
    def __init__(self,name,age,roll):
        self.n=name
        self.a=age
        self.r=roll
    def add_new(self,contact):
        self.c=contact
    def show_detail(self):
        print(self.n,self.a,self.r,self.c,self.e)
obj=Student('Neeraj',37,10)
obj.add_new(12345)
obj.e='Neeraj@gmail.com'#declaration
obj.show_detail()

# cd .assigment

class Student:
    def __init__(self,name):
        self.n=name
    def show(self):
        print(self.n)
obj=Student("Neeraj")
obj.show()
print(obj.n)