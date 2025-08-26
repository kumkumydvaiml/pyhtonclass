# f=open('n2.py','w+')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)


# f=open('n3.py','a')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)


# f=open('n2.py','r')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)

# f=open('n1.txt','a')
# f.write(''' \n this is python class this is \n
#  python class
# this is python class''')
# f.close()
# print(f.closed)

# f=open('n1.txt','a')
# f.writelines(["Hello","hii","welcome"])
# f.close()

# f=open('n1.txt')
# print(f.mode)

f=open('n1.txt')
# data=f.read()
# print(data)
# f.close()

# data=f.read(10)
# print(data)

# data=f.read(10)
# print(data)

data=f.readline()
print(data)

data=f.readlines()  # interview question
print(data)


with open('n1.txt') as f:
    data=f.read()
    print(data)
print(f.closed)





