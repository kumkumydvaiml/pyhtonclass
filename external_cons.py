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