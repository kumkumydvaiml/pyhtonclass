# x=10     #global
# def new():
#     global y
#     y=20  #local
#     print(x,y)
# new()
# print(x)
# print(y)


x=10     #global
def new():
    x=20  #local
    print(x)
    print(globals()['x'])
new()
print(x)

s="kumkum"
s1=""
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
print(s1)


s="kumkum"
s1=""
for i in range(len(s)-1,-1,-1):
    s1=''.join([s1,s[i]])
print(s1)


a="kumkum"
a1=[]
for i in a:
    a1.append(ord(i))
print(a1)

s="pantuation"
s1=""
for i in s:
    if i in s1:
        s1+=i
print(s1)

a="kumkum"
a1=""
for i in a:
    if ord(i)%2==0:
        a1=a1+chr(ord(i))
print(a1)


aa=input("Enter a word :")
aa1=""
for i in range(len(aa)-1,-1,-1):
    aa1+=aa[i]
print(aa1)



