# class Parent:
#     def home(self):
#         print("home from parent")
#     def car(self):
#         print("car from parent")
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass
# obj=Child1()
# obj.home()
# obj.car()

# obj2=Child2()
# obj2.home()
# obj2.car()

class Parent:
    def home(self):
        print("home from parent")
    def car(self):
        print("car from parent")
class Child1(Parent):
    pass
class Child2(Parent):
    pass
class Child(Child1,Child2):
    pass
obj=Child()
obj.home()
obj.car()


