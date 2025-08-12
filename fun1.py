# # def add(x,y):
# #     # print(x+y)
# #     return(x,y)
# # p=int(input("Enter first value :"))
# # q=int(input("Enter second value :"))
# # result=add(p,q)
# # print(result)
# # print(result)
# # print(result)


# def add(x,y):
#     return(x+y)
# p=int(input("Enter first value :"))
# q=int(input("Enter second value :"))
# result=add(p,q)
# x=add(p,q)
# if x%2==0:
#     print(f' given no{x} is even')
# else:
#     print('odd')

# # koi bhi fuction terminate hota hai return se

# def add(x,y):
#     # print(x+y)
#     return(x,y)
#     print("HEllo")
# p=int(input("Enter first value :"))
# q=int(input("Enter second value :"))
# result=add(p,q)

#positonal argu
def fun_name(x,y,z):
    return x+y+z
result=fun_name(10,20,30)
print(result)

def fun_name(x,y,z):
    return x+y+z
# result=fun_name(10,20,30,40)
# print(result)
#jitne parameter define honge utne hi argumnet dene hai otherwiese error

#default argument
def fun_name(x=0,y=0,z=0):
    return x+y+z
result=fun_name()
print(result)
result=fun_name(10)
print(result)
result=fun_name(10,20)
print(result)
result=fun_name(10,20,30)
print(result)

#variable length positional 
def add(*x):
    print(x)
    print(type(x))
result=add(10,20,30,1,2,3,4)
