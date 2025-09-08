class Student:
    @staticmethod
    def show():
        print("Hello")
obj=Student()
obj.show()


class Student:
    @staticmethod
    def show(self):
        print(self)
obj=Student()
obj.show("neeraj")