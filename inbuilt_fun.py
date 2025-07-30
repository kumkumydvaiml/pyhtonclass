# to find the length of string
# count=0
# s1='kumkum'
# for _ in s1:
#     count+=1
# print(count)

# to count the char
s1='kumkum'
# target='k'
# count=0
# for _ in s1:
#     if _==target:
#         count+=1    
# print(count)
s=''
for i in range(len(s1)-1,-1,-1):
    s+=s1[i]
print(s)

