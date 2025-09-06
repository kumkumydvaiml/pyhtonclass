class Student:
    school='SHSS'
    def __init__(self):
        Student.city='Bhopal'
    def add_new(self):
        Student.principal='python'
    def show_details(self):
        print(Student.city,
              Student.school,
              Student.principal,
              Student.code)
Student.code=101
obj=Student()
obj.add_new()
obj.show_details()



class Student:
    school='SHSS'
    def __init__(self):
        x=10
        print(x)
        Student.city='Bhopal'
    def add_new(self):
        Student.principal='python'
        b=20
        print(b)
obj=Student()
obj.add_new()





