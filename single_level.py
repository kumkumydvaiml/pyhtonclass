class Parent:
    def home(self):
        print("home from parent class")
    def car(self):
        print("car from parent class")
class Child(Parent):
        pass
obj=Child()
obj.home()
obj.car()