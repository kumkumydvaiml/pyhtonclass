#27/aug/2025
with open('n1.txt','a+') as f:
    print(f.name)
    print(f.mode)
    print(f.closed)
print(f.closed)


# with open('n1.txt','a+') as f:
#     print(f.tell())


# with open('n1.txt','w') as f:
#     print(f.tell())
    

# with open('n6.txt','x') as f:
#     print(f.tell())

# with open('n1.txt','r') as f:
#     print(f.tell())


# with open('n1.txt','r') as f:
#     print(f.tell())
#     data=f.read(5)
#     print(data)
#     print(f.tell()) # cursor current postion find with the help of tell()

# seek() method use to change position of curser
#syntax=seek()


with open('n1.txt','rb') as f: #b stands for binary
    print(f.tell())
    data=f.read(5)
    print(f.tell())
    f.seek(0)
    print(f.tell())
    data=f.read(10)
    print(f.tell())
    f.seek(5,0)
    print(f.tell())
    f.seek(2,1)
    print(f.tell())
    f.seek(-5,1)
    print(f.tell())
    f.seek(-5,2)
    print(f.tell())




