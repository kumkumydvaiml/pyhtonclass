#list comprehancion
n=int(input("Enter :"))
result=[i for i in range(1,n+1)]
print(result)

l=[1,2,3,4,5]
x=[i**2 for i in l]
print(x)


l=[1,2,3,4,5]
x=[i**2 for i in l if i%2==0]
print(x)