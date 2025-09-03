class Student:
    def __init__(self):
        print("External constructor called")
x=Student
print(id(x),id(Student))
y=Student()
# print(id(y),id(Student()))


class Student:
    def __init__(self):
        print("External constructor called")
        print(id(self))
x=Student()
print(id(x),id(Student))



class Student:
    def __init__(self,name,grade):
        self.n=name
        self.g=grade
        print("obj self id=",id(self))
    def account(self):
        print(self.n)
        print(self.g)
obj=Student("Neeraj","10th")
obj.account()