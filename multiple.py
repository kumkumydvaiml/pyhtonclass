class Parent1:
    def home(self):
        print("From parent")
class Parent2:
    def home(self):
        print("from parent2")
class Child(Parent1,Parent2):
    pass

obj=Child()
obj.home()



class Parent1:
    def home(self):
        print("From parent")
class Parent2:
    def home(self):
        print("from parent2")
class Child(Parent2,Parent1):
    pass

obj=Child()
obj.home()
