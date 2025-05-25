def square():
    for i in range(1,12):
        yield i*i
a=square()
for i in a:
 print(i,end=" ")    