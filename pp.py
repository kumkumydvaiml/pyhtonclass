# li=["papaya","grapes","Apple"]
# print(type(li))
# print(li)
# p=input("Choose any item :")


# li=["papaya","grapes","Apple"]
# print(type(li))
# print(li)
# p=input("Choose any item :")

# li=["papaya","grapes","Apple"]
# print(type(li))
# print(li)
# p=input("Choose any item :")


# li=["papaya","grapes","Apple"]
# print(type(li))
# print(li)
# p=input("Choose any item :")


# i=1
# while i<=20:
#     if i%2==0:
#         print("even numbers are",i)
#     i+=1


# s=input("Enter any name :")
# s1=''
# count=0
# for i in s:
#     count+=1
# print(f'total letter in {s} are {count}')

# k=input("Enter any sentence :")
# k1=''
# for i in k:
#     if i!=' ':
#         k1+=i
# print(k1)

# z=input("Enter any sentence :")
# z1=''
# count=0
# for i in range(len(z)-1,-1,-1):
#     if i==' ':
#         count+=1
# print(count)


# s='i am kumkum'
# s1=''
# for i in s:
#     if i!=" ":
#         s1+=i
# print(s1)


# s='kumkum'
# old='k'
# new='p'
# s1=""
# for i in s:
#     if i==old:
#         s1+=new
#     else:
#         s1+=i
# print(s1)

# s=input("Enter any name :")
# vowels='aeiouAEIOU'
# s1=''
# for i in s:
#     if i not in vowels:
#         s1+=i
# print(s1)
    

# a=10
# b=20
# c=a+b
# b=c-b
# a=c-a
# print(a)
# print(b)

# h=int(input("Enter height :"))
# b=int(input("Enter base :"))
# tri=0.5*h*b
# print(tri)


# n=int(input("Enter :"))
# i=1
# while i<=n:
#     print(i)
#     i+=1

# n=input("enter :")
# i=1
# while n<=10:
#     print(n)
#     i+=1

# s="python language"
# x=s.split("l")
# print(x)


# s=set()
# print(type(s))
# b=dict()
# print(type(b))

# print(x:=10)  # walrus operator

# n=int(input("Enter a number :"))
# count=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(count,end=" ")
#         count+=1
#     print()


# n=int(input("Enter a number :"))
# first,second=0,1
# print(first)
# print(second)
# for i in range(1,n-1):
#     next=first+second
#     first=second
#     second=next
#     print(next)


# n=int(input("Enter a number :"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if n==sum:
#     print("Perfect")
# else:
#     print("Not perfect")


# n=int(input("Enter a number :"))
# count=0
# for i in range(2,n+1):
#     if n%i==0:
#         count+=1
# if count==1:
#     print("prime")
# else:
#     print("Not a Prime")

# s=input("Enter any word :")
# s1=""
# for i in range(len(s)-1,-1,-1):
#     s1+=s[i]
# print(s1)


# w=input("Enter any sentence :")
# w1=""
# for i in w:
#     if i!=" ":
#         w1+=i
# print(w1)


# s=input("Enter any word :")
# s1=""
# for i in s:
#     if i>='A' or i<='Z':
#         s1=chr(ord(i)+32)
#     print(s1,end="")


# s=input("Enter any sentence :")
# count=1
# for i in s:
#     if i==" ":
#         count+=1
# print(count)


# s=input("Enter any word :")
# s=s.lower()
# s1=""
# old,new="k","c"
# for i in s:
#     if i==old:
#         s1+=new
#     else:
#         s1+=i
# print(s1)

# s=input("Enter any word :")
# s=s.lower()
# s1=""
# vowels="aeiou"
# for i in s:
#     if i not in vowels:
#         s1+=i
#     else:
#         pass
# print(s1)

# s=input("Enter any word :")
# s1=""
# for i in s:
#     if i not in s1:
#         s1+=i
# print(s1)


# li=[1,2,3,9]
# count=0
# for i in li:
#     count+=1
# print(count)

# li=[1,2,3,9]
# sum=0
# for i in li:
#     sum+=i
# print(sum)

# li=[1,2,3,9]
# max=li[0]
# for i in li:
#     if i>max:
#         max=i
# print(max)

# li=[1,2,3,9]
# li1=[]
# for i in range(len(li)-1,-1,-1):
#     li1.append(li[i])
# print(li1)


# li=[1,2,3,9,1,9,0]
# li1=[]
# for i in li:
#     if i not in li1:
#         li1.append(i)
# print(li1)

# li=[1,2,3,9]
# tup=()
# for i in li:
#     tup+=(i,)
# print(tup)


# tup=(1,2,3,9)

# tup1=()
# for i in range(len(tup)-1,-1,-1):
#     tup1+=(tup[i],)
# print(tup1)

# n=int(input("Enter a number :"))
# ans=n
# sum=0
# for i in range(1,n+1):
#     digit=n%10
#     sum+=digit
#     n//=10
# if ans%sum==0:
#     print("Harshad")
# else:
#     print("Not harshad")



# s=eval(input("Enter string 1 :"))
# s1=eval(input("Enter string 2 :"))
# s=sorted(s)
# s1=sorted(s1)
# if len(s)==len(s1):
#     if s==s1:
#         print("Anagram")
#     else:
#         print("Not an Anagram")  
# else:
#     print("Not Anagram")


# n=int(input("Enter a number :"))
# ans=n
# sum=0
# pow=n*n
# for i in range(1,n+1):
#     pow=pow%10
#     sum+=pow
#     n//=10
# if ans==sum:
#     print("Neon")
# else:
#     print("Not a Neon")/


# n=int(input("Enter a digit :"))
# ans=n
# sum=0
# while n>0:
#     digit=n%10
#     fact=1
#     for i in range(1,digit+1):
#         fact*=i
#     sum+=fact
#     n//=10
# if ans==sum:
#     print("Peterson")
# else:
#     print("Not a peterson")




# n=int(input("Enter a digit :"))
# ans=n
# sum,mul=0,1
# while n>0:
#     digit=n%10
#     sum+=digit
#     mul*=digit
#     n//=10
# if sum==mul:
#     print("Spy")
# else:
#     print("Not a spy")


# li=[1,2,4,9,10,0]
# n=len(li)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if li[j]>li[j+1]:
#             li[j],li[j+1]=li[j+1],li[j]
# print(li)


# n=int(input("Enter a number :"))
# count=0
# for i in range(2,n+1):
#     if n%i==0:
#         count+=1
# if count==1:
#     print("Prime")
# else:
#     print("Not a prime")


# li=[0,1,0,2,0,3,4]
# li1=[]
# li2=[]
# result=[]
# for i in li:
#     if i!=0:
#         li1.append(i)
#     else:
#         li2.append(i)
# for j in li1:
#     result.append(j)
# for e in li2:
#     result.append(e)
# print(result)



# li=[2,3,5,8,6,1]
# li1=[]
# li2=[]
# result=[]
# for i in li:
#     if i%2==0:
#         li1.append(i)
#     else:
#         li2.append(i)
# for j in li1:
#     result.append(j)
# for e in li2:
#     result.append(e)
# print(result)




d1={1:'age',
    2:'name'}
d2={3:'education'}
d1.update(d2)
print(d1)


