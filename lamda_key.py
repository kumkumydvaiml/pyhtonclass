x=lambda x,y,z : x+y+z
print(x(4,5,6))

l=[1,2,3,4,5]
result=list(map(lambda x:x**2,l))
print(result)

l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
result=list(map(lambda x,y,z:x+y+z,l1,l2,l3))
print(result)