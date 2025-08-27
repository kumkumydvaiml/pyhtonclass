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
    

with open('n6.txt','x') as f:
    print(f.tell())


    