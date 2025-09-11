class Parent:
    principal='python'
    def new(self):
        print('hello')
class Child(Parent):
    def child(self):
        print(Parent.principal)
        Parent.new(self)
obj=Child()
obj.child()
print(Parent.principal)