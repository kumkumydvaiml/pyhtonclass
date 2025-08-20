# s='kumkum'
# s1=''
# for i in range(len(s)-1,-1,-1):
#     s1+=s[i]
# print(s1)

# n=input("Enter :")
# result=''
# for ch in n:
#     if ch>='A' or ch<='Z':
#         result+=chr(ord(ch)+32)
# print(result)

# n=input("Enter :")
# n1=''
# for ch in n:
#     if n>='a' or n<='z':
#         n1+=chr(ord(ch)-32)
# print(n1)


# s=input("Enter :")
# s1=''
# for ch in s:
#     if ch!=' ':
#         s1+=ch
# print(s1)

# s=input("Enter :")
# s1=''
# for ch in s:
#     if ch not in 'aeiouAEIOU':
#         s1+=ch
# print(s1) 

# s=input("Enter :")
# s1=''
# for ch in s:
#     if ch>='a' or ch<='z':
#         s1+=chr(ord(ch)-32)
        
# print(s1)

# li=[1,2,3,4]
# count=0
# for _ in li:
#     count+=1
# print(count)

# li=[1,2,3,4]
# sum=0
# for i in li:
#     sum+=i
# print(sum)

# li=[1,2,3,4,70,20]
# max=li[0]
# for i in li:
#     if i>max:
#         max=i
# print(max)

# li=[1,2,1,3,1,1]
# target=1
# count=0
# for i in li:
#     if i==target:
#         count+=1
# print(f'count of {target} is {count}')

# remove duplicate from list
# li=[1,2,4,1,3,1]
# li1=[]
# for i in li:
#     if i not in li1:
#         li1.append(i)
# print(li1)


s='kumkum'
fre={}
for i in s:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
print(fre)











