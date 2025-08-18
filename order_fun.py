#map
# l=[1,2,3,4,5]
# def squr(n):
#     return n**2
# result=map(squr,l)
# print(result)
# print(tuple(result))
# print(list(result))


# li1=[6,7,8,9,10]
# li2=[1,2,3,4,5]
# li3=[1,2,3,4]
# li4=[1,2,3]
# def add(x,y,z,p):
#     return x+y+z+p
# result=map(add,li1,li2,li3,li4)
# print(list(result))


# li1=[6,7,8,9,10]
# li2=[1,2,3,4,5]
# li3=[1,2,3,4,5]

# def add(x,y,z):
#     return x+y+z
# result=map(add,li1,li2,li3)
# print(list(result))


#filter()


# l=[1,2,3,4,5]
# def even_no(n):
#     if n%2==0:
#         return n
# result=list(filter(even_no,l))
# print(result)


# l=[1,2,3,4,5]
# def odd_no(n):
#     if n%2!=0:
#         return n
# result=list(filter(even_no,l))
# print(result)


l=[1,2,3,4,5]
def even_no(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'
result=list(map(even_no,l))
print(result)