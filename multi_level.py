class Grandparent:
    def home(self):
        print("home from grand_parent")
class Parent(Grandparent):
    def car(self):
        print("car from parent")
class Child(Parent):
    pass
obj=Child()
obj.home()
obj.car()