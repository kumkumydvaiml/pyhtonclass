s='kumkum'
s1=''
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
print(s1)

n=input("Enter :")
result=''
for ch in n:
    if ch>='A' or ch<='Z':
        result+=chr(ord(ch)+32)
print(result)

n=input("Enter :")
n1=''
for ch in n:
    if n>='a' or n<='z':
        n1+=chr(ord(ch)-32)
print(n1)



