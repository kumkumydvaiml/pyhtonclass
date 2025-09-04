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


class Marks:
    def __init__(self,english,social):
        self.e=english
        self.s=social
        print(self.e)
        print(self.s)
obj=Marks(89,97)


class Marks:
    def __init__(self,english,social):
        self.e=english
        self.s=social
        print(id(self))
        
        print(self.e)
        print(self.s)
        print(id(Marks))
obj=Marks(89,97)
print(id(obj))#



class Student:
    def __init__(self):
        print("External Constructor called")
obj=Student
obj=Student()

obj.__init__()



# multiple constructor par call karne par last wala hi call hoga
class Student:
    def __init__(self):
        print("External ")
    def __init__(self):
        print("Constructor 2")
    def __init__(self):
        print("constructor3")
obj=Student()
obj.__init__()