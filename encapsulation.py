# class Parent:
#     principal='python'
#     def new(self):
#         print('hello')
# class Child(Parent):
#     def child(self):
#         print(Parent.principal)
#         Parent.new(self)
# obj=Child()
# obj.child()
# print(Parent.principal)


class Parent:
    _principal='python'
    def _new(self):
        print('hello')
class Child(Parent):
    def child(self):
        print(Parent._principal)
        Parent._new(self)
obj=Child()
obj.child()
print(Parent._principal)

