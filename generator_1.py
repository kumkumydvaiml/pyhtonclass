def natural_no(n):
    for i in range(1,n+1):
        return i
x=int(input("Enter number :"))
res=natural_no(x)
print(res)

# yield
def natural_no(n):
    for i in range(1,n+1):
        if i%2!=0:
        # if i%2==0:
            yield i
x=int(input("Enter number :"))
res=natural_no(x)
print(res)
print(next(res))
print("hello")
print(next(res))
print("Welcome")
print("hii")
print(next(res))
for i in res:
    print(i)


