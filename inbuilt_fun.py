# to find the length of string
# count=0
# s1='kumkum'
# for _ in s1:
#     count+=1
# print(count)

# to count the char
s1='madam'
# target='k'
# count=0
# for _ in s1:
#     if _==target:
#         count+=1    
# print(count)
# s=''
# for i in range(len(s1)-1,-1,-1):
#     s+=s1[i]
# print(s)

s=''
for i in range(len(s1)-1,-1,-1):
    s=s+s1[i]
if s1==s:
    print('palindrome')
else:
    print('not a palindrome')
    
var= "I love python"
print(var[-2:-5:])


