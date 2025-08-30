# x=10     #global
# def new():
#     global y
#     y=20  #local
#     print(x,y)
# new()
# print(x)
# print(y)


x=10     #global
def new():
    x=20  #local
    print(x)
    print(globals()['x'])
new()
print(x)

