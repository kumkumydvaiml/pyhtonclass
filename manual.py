# String

# to reverse the string
# s='kumkum'
# s1=''
# for i in range(len(s)-1,-1,-1):
#     s1+=s[i]
# print(s1)


# remove duplicate character
# n='kumkum'
# n1=''
# for i in n:
#     if i not in n1:
#         n1+=i
# print(n1)


# character frequency
# s='kumkum'
# fre={}
# for i in s:
#     if i in fre:
#         fre[i]+=1
#     else:
#         fre[i]=1
# print(fre)



#To convert uppercase to lowercase
# n=input("Enter :")
# result=''
# for ch in n:
#     if ch>='A' or ch<='Z':
#         result+=chr(ord(ch)+32)
# print(result)


#To convert uppercase to lowercase
# n=input("Enter :")
# n1=''
# for ch in n:
#     if n>='a' or n<='z':
#         n1+=chr(ord(ch)-32)
# print(n1)


#to remove spaces
# s=input("Enter :")
# s1=''
# for ch in s:
#     if ch!=' ':
#         s1+=ch
# print(s1)

#to remove vowels
# s=input("Enter :")
# s1=''
# for ch in s:
#     if ch not in 'aeiouAEIOU':
#         s1+=ch
# print(s1) 

#
# s=input("Enter :")
# s1=''
# for ch in s:
#     if ch>='a' or ch<='z':
#         s1+=chr(ord(ch)-32)
# print(s1)


# List

# reverse list
# li=[1,2,3,4,5]
# li1=[]
# for i in range(len(li)-1,-1,-1):
#     li1.append(li[i])
# print(li1)

#count elements in list
# li=[1,2,3,4]
# count=0
# for _ in li:
#     count+=1
# print(count)

# sum of list elements
# li=[1,2,3,4]
# sum=0
# for i in li:
#     sum+=i
# print(sum)

# find max element in list
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

# combine two list
# l1=[1,2,3,4]
# l2=[6,7,8]
# result=[]
# for i in l1:
#     result.append(i)
# for i in l2:
#     result.append(i)
# print(result)


# common elements
# l1=[5,3,2,1]
# l2=[4,2,9,3,1,1]
# result=[]
# for i in l1:
#     if i in l2:    
#         result.append(i)
# print(result)


# find even and odd elemnet
# l0=[1,2,4,9,3,5]
# l1=[1,4,7]
# even=[]
# odd=[]
# for i in l0:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f'even are {even}')
# print(f'odd are {odd}')


# sort list in ascending
# l=[2,1,8,2,0,7,5]
# n=len(l)
# for i in range(n):
#     for j in range(i+1,n):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)


# combine two list
# l1=eval(input("Enter a list1 :"))
# l2=eval(input("Enter a list2 :"))
# l3=[]
# for i in l1:
#     l3.append(i)
# for j in l2:
#     l3.append(j)
# print(l3)


# l1=eval(input("Enter list1 :"))
# l2=eval(input("Enter list2 :"))

# if l1==l2:
#     print('yes {l1} and {l2} are equal')
# else:
#     print('No {l1} and {l2} are not equal')


# to convet list to string
# l=eval(input("Enter list :"))
# s=''
# for i in l:# input kisme lena hai 
#     s+=i
# print(s)


# to conver string  to list
# n=eval(input("Enter :"))
# l=[]
# for i in n:
#     l.append(i)
# print(l)


# Tuple

# total element in tuple
# t=eval(input("enter any tuple :"))
# count=0
# for _ in t:
#     count+=1
# print(f' total element in {t} are {count}')


# t=eval(input("enter any tuple :"))
# tar=eval(input("Enter target :"))
# count=0
# for i in t:
#     if i==tar:
#         count+=1
# print(f'total {tar} in {t} are {count}')


# find max element in tuple
# t=eval(input("enter any tuple :"))
# max=t[0]
# for i in t:
#     if i>t[0]:
#         max=i
# print(f'maximum element in {t} is {max}')


# find minimum element in tuple
# t=eval(input("enter any tuple :"))
# min=t[0]
# for i in t:
#     if i<t[0]:
#         min=i
# print(f'minimum element in {t} is {min}')


# sum of tuple element
# t=eval(input("Enter any tuple :"))
# sum=0
# for i in t:
#     sum+=i
# print(f'Sum of {t} is {sum}')


# find index of element
# t=eval(input("Enter any tuple :"))
# idx=int(input("Enter which element index do you find :"))
# found=()
# for i in t:
#     if idx==i:
#         found=t[i]
# print(found)


# reverse the tuple
# t=eval(input("Enter any tuple :"))
# rev=()
# for i in range(len(t)-1,-1,-1):
#     rev+=(t[i],)
# print(rev)



# convert tuple to list
# t=eval(input("Enter any tuple :"))
# li=[]
# for i in t:
#     li.append(i)
# print(li)


# convert list to tuple
# li=eval(input("Enter any list :"))
# t=()
# for i in li:
#     t+=(i,)
# print(t)



# Dictionary

# count elemnent in dict
# d=eval(input("Enter dictionary :"))
# count=0
# for i in d:
#     count+=1
# print(count)


# to find key in dict
# dic=eval(input("Enter dictionary :"))
# key=[]
# for i in dic:  python tutor par chalana hai
#     key.append(i)
# print(key)

# merge two dict
# d1=eval(input("Enter dictionary 2 :"))
# d2=eval(input("Enter dictionary 1 :"))
# result={}
# for i in d1:
#     result[i]=d1[i]
# for j in d2:
#     result[j]=d2[j]
# print(result)

def dic(d1,d2):
    merge={}
    for i in d1:
        merge[i]=d1[i]
    for j in d2:
        merge[j]=d2[j]
    return merge


# Example 8: Write a program to add 5 in each elements in given list. [10,20,30,40,50]
# l1=eval(input("Enter a list :"))
# l2=[]
# for i in l1:
#     i=i+5
#     l2.append(i)
# print(l2)


# t1=eval(input("Enter a tuple :"))
# t2=()
# for i in t1:
#     i=i+5  # append kaam nahi karta kya tuple me
#     t2=t1[i]
# print(t2) error


# s=(input("Enter string :"))
# li=[]
# for i in s:
#     li.append(i)
# print(li)

# Example 7: Write a program to find how many vowels and consonants are present in strings.

# vowel='aeiou'
# consonant='qwrtyplkjhgfdszxcvbnm'
# n=input("Enter any :")
# for i in n:
#     if n in vowel:
#         count+=1 









































