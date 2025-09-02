class New:
    x=10
    y=20
obj=New
print(id(New))
print(id(obj))

class New:
    pass
obj=New
print(id(New))
print(id(obj))

class New:
    "for demo purpose"
obj=New