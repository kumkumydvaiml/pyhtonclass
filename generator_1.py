# def natural_no(n):
#     for i in range(1,n+1):
#         return i
# x=int(input("Enter number :"))
# res=natural_no(x)
# print(res)

# # yield
# def natural_no(n):
#     for i in range(1,n+1):
#         yield i
# x=int(input("Enter number :"))
# res=natural_no(x)
# print(res)
# print(next(res))
# print("hello")
# print(next(res))
# print("Welcome")
# print("hii")
# print(next(res))
# for i in res:
#     print(i)

# yield
def natural_no(n):
    for i in range(1,n+1):
       yield i
x=int(input("Enter number :"))
res=natural_no(x)
for i in res:
    if i%2==0:
        print(i)



