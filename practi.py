# # # n=1
# # # while n<=100:
# # #     print(n)
# # #     n+=1

# # # n=100
# # # while n>=1:
# # #     print(n)
# # #     n-=1

# # # num=int(input("Enter a number :"))
# # # n=1
# # # while n<=10:
# # #     print(num*n)
# # #     n+=1

# # # li=[1,4,9,16,25,36,49,64,81,100]
# # # idx=0
# # # while idx<len(li):
# # #     print(li[idx])
# # #     idx+=1

# # # li=(1,4,9,16,25,36,49,64,81,100)
# # # x=36
# # # idx=0
# # # while idx<len(li):
# # #     if (li[idx]==x):
# # #         print("found",idx)
# # #     else:
# # #         print("finding")
# # #     idx+=1


# # # for i in range(100 ,0,-1):
# # #     print(i)


# # # n=int(input("Enter a number :"))
# # # for i in range(1,11):
# # #     print(n*i)

# # # sum=0
# # # for i in range(1,11):
# # #     sum=i+sum
# # # print("Total sum = ",sum)

# # # n=int(input("Enter a number :"))
# # # for i in range(1,n+1):
# # #     print(i,end=" ")

# # # n=int(input("Enter a number :"))
# # # for i in range(1,n+1):
# # #     print(i**2,end=" ")

# # # n=int(input("Enter a number :"))
# # # for i in range(1,n+1):
# # #     if i%2==0:
# # #         print(i)

# # # sum=0
# # # n=int(input("Enter a number :"))
# # # for i in range(1,n+1):
# # #     sum+=i
# # # print("Sum = ",sum)

# # # str="kumkum"
# # # for i in range(len(str)-1,-1,-1):
# # #      print(str[i])


# # # vowels='aeiou'
# # # word='education'
# # # count=0
# # # for char in word:
# # #     if char in vowels:
# # #         count+=1
# # # print(f"Total vowels in {word} is {count}")

# # # first=0
# # # second=1
# # # n=int(input("Enter a number :"))
# # # print(first,second,end=" ")
# # # for i in range(1,n-1):
# # #     next=first+second
# # #     first=second
# # #     second=next
# # #     print(next,end=" ")

# # # fact=1
# # # n=int(input("Enter a number :"))
# # # for i in range(1,n+1):
# # #     fact*=i
# # # print(fact)

# # # n=int(input("Enter a number :"))
# # # for i in range(2,n):
# # #     if n%i==0:
# # #         print("Not a prime")
# # #         break
# # # else:
# # #     print("prime")


# # # n=int(input("Enter a number :"))
# # # is_prime=True
# # # for i in range(2,int(n**0.5)+1):
# # #     if n%i==0:
# # #         is_prime=False
# # #         break
# # # if is_prime and n>1:
# # #     print(n,"is a prime member")
# # # else:
# # #     print(n,"is not a prime member")

# # # n=10
# # # while n<=15:
# # #     print(n,end=" ")
# # #     n+=1


# # # n=1
# # # while n<=5:
# # #     print(n**3)
# # #     n+=1

# # # n=1
# # # while n<=10:
# # #     if n%2!=0:
# # #         print(n)
# # #     n+=1

# # # n=1
# # # mul=1
# # # while n<=5:
# # #     mul*=n
# # #     n+=1
# # # print(mul)

# # # is_prime=True
# # # n=int(input("Enter a number :"))
# # # for i in range(2,int(n**0.5)+1):
# # #     if n%i==0:
# # #         is_prime=False
# # #         break
# # # if is_prime and n>1:
# # #     print(n,"is prime member")
# # # else:
# # #     print(n, "is not a prime member")


# # # sum=0
# # # n=input("Enter a number :")
# # # n1=int(len(n))
# # # n=int(n)
# # # ans=n
# # # while n>0:
# # #     digit=n%10
# # #     sum=sum+digit**n1
# # #     n//=10
# # # if ans==sum:
# # #     print("Armstrong")
# # # else:
# # #     print("Not an armstrong")


# # # word='Education'
# # # count=0
# # # for char in word:
# # #     if char in word:
# # #         count+=1
# # # print(f"{count} Letter in {word} ")

# # # count=0
# # # n=int(input("Enter digits :"))
# # # while n>0:
# # #     digit=n%10
# # #     count+=1
# # #     n//=10
# # # print(f"Total digits are {count}")

# # # a=10
# # # b=20
# # # c=a+b
# # # a=c-a
# # # b=c-b
# # # print("a = ",a)
# # # print("b = ",b)


# # # 1. Write a program to find maximum between two numbers.

# # # n1=int(input("Enter number 1 :"))
# # # n2=int(input("Enter number 2 :"))
# # # if n1>n2:
# # #     print("Greatest number is",n1)
# # # else:
# # #     print("Greatest number is",n2)


# # # 2. Write a program to find maximum between three numbers.
# # # n1=int(input("Enter number 1 :"))
# # # n2=int(input("Enter number 2 :"))
# # # n3=int(input("Enter number 3 :"))
# # # if n1>n2 and n1>n3:
# # #     print("Greatest number is",n1)
# # # elif n2>n1 and n2>n3:
# # #     print("Greatest number is",n2)
# # # else:
# # #     print("Greatest number is",n3)

# # # 3. Write a program to check whether a number is negative,
# # # positive or zero.
# # # n=int(input("Enter a number :"))
# # # if n>0:
# # #     print("Number is positive")
# # # elif n<0:
# # #     print("Number is negative")
# # # else:
# # #     print("Number is zero")

# # # 4. Write a program to check whether a number is divisible by 5
# # # and 11 or not.
# # # n=int(input("Enter a number :"))
# # # if n%5==0 and n%11==0:
# # #     print("No. is divisible of 5 and 11")
# # # else:
# # #     print("Not divisible of 5 and 11")

# # # 5. Write a program to check whether a number is even or odd.
# # # n=int(input("Enter a number :"))
# # # if n%2==0:
# # #     print("Even number")
# # # else:
# # #     print("Odd number")

# # # 6. Write a program to check whether a year is leap year or not.
# # # year=int(input("Enter the year :"))
# # # if (year%4==0) or (year%400==0 and year%100!=0):
# # #     print("Year is a leap year")
# # # else:
# # #     print("Year is not a leap year")

# # # 7. Write a program to check whether a character is alphabet or
# # # not.
# # # ch=input("Enter any alphabet :")
# # # if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
# # #     print("It's a character/alphabet")
# # # else:
# # #     print("It's not a character/alphabet")


# # # 8. Write a program to input any alphabet and check whether it is
# # # vowel or consonant.
# # # ch=input("Enter any character :")
# # # li='aeiouAEIOU'

# # # if ch in li:
# # #     print("It's an Vowel")
# # # else:
# # #     print("It's a consonant")

# # # 9. Write a program to input any character and check whether it is
# # # alphabet, digit or special character.
# # # n=input("Enter a any digit or special character or a;phabet what you want : ")
# # # if n>='0' and n<='9':
# # #     print("Its a digit")
# # # elif (n>='A' and n<='Z') or (n>='a' and n<='z'):
# # #     print("Its an alphabet")
# # # else:
# # #     print("Its a special character")


# # # 10. Write a program to check whether a character is uppercase or
# # # lowercase alphabet .
# # # 11. Write a program to input week number and print week day .
# # # 12. Write a program to input month number and print number of
# # # days in that month.
# # # 13. Write a program to count total number of notes in given
# # # amount .
# # # 14. Write a program to input angles of a triangle and check whether
# # # triangle is valid or not.
# # # 15. Write a program to input all sides of a triangle and check
# # # whether triangle is valid or not.
# # # 16. Write a program to check whether the triangle is equilateral,
# # # isosceles or scalene triangle.
# # # 17. Write a program to calculate profit or loss.
# # # 18. Write a program to input marks of five subjects Physics,
# # # Chemistry, Biology, Mathematics and Computer. Calculate
# # # percentage and grade according to following:
# # # Percentage &gt;= 90% : Grade A
# # # Percentage &gt;= 80% : Grade B
# # # Percentage &gt;= 70% : Grade C
# # # Percentage &gt;= 60% : Grade D
# # # Percentage &gt;= 40% : Grade E
# # # Percentage &lt; 40% : Grade F

# # # 19. Write a program to input basic salary of an employee and
# # # calculate its Gross salary according to following:
# # # Basic Salary &lt;= 10000 : HRA = 20%, DA = 80%
# # # Basic Salary &lt;= 20000 : HRA = 25%, DA = 90%
# # # Basic Salary &gt; 20000 : HRA = 30%, DA = 95%
# # # sal=float(input("Enter your basic salary :"))
# # # hra=0
# # # da=0
# # # if sal<=10000:
# # #     hra=(sal*20)/100
# # #     da=(sal*80)/100
# # # elif sal<=20000:
# # #     hra=(sal*25)/100
# # #     da=(sal*90)/100
# # # else:
# # #     hra=(sal*30)/100
# # #     da=(sal*95)/100
# # # gross=sal+hra+da
# # # print(gross)



# # n=int(input("Enter a number :"))
# # i=1
# # while i<=n:
# #     print('*'*n)
# #     i+=1


# n=int(input("Enter a number :"))
# i=1
# while i<=n:
#     print(' '*n-i + '*'*i)
# i+=1




# # # 20. Write a program to input electricity unit charges and calculate
# # # total electricity bill according to the given condition:
# # # For first 50 units Rs. 0.50/unit
# # # For next 100 units Rs. 0.75/unit
# # # For next 100 units Rs. 1.20/unit
# # # For unit above 250 Rs. 1.50/unit
# # # An additional surcharge of 20% is added to the bill


# # # a=10
# # # b=10.0
# # # if a==b:
# # #     print("True")
# # # else:
# # #     print("False")


# # # n=int(input("Enter number :"))
# # # for i in range(1,n):
# # #     for j in range(1,n):
# # #         print(j,end=" ")
# # #     print()

# # # ch=65
# # # for i in range(65,70):
# # #     for j in range(65,70):
# # #         if ch==65:
# # #             print("A",end="")
# # #     print()


# # # for i in range(6,0,-1):
# # #     for j in range(i):
# # #         print("*",end=" ")
# # #     print()

# # # for i in range(1,10):
# # #     for j in range(i+1):
# # #         print("*",end=" ")
# # #     print()


# # # word='Education'
# # # count=0
# # # for char in word:
# # #     if char in word:
# # #         count+=1
# # # print(f"{count} Letter in {word} ")

# # # count=0
# # # vowel="aeiou"
# # # word="kumkum"
# # # for char in word:
# # #     if char in vowel:
# # #         count+=1
# # # print(count,"Vowels in kumkum")


# # # li=[1,2,3,4]
# # # # for i in range(len(li)):
# # # #     print(li[i])


# # # # for i in range(4):
# # # #     print(i)

# # # # print(li[0])

# # # for i in li:
# # #     print(i+10)


# # # li=[8,3,1,6,9]
# # # large=li[0]
# # # for n in li:
# # #     if n>large:
# # #         large=n
# # # print(f"greatest number is {large}")

# # # n=9875
# # # sum=0
# # # for i in range(1,n+1):
# # #     digit=n%10
# # #     sum+=digit
# # #     n//=10
# # # print(sum)

# # # n=9875
# # # sum=0
# # # for i in range(1,n+1):
# # #     digit=n%10
# # #     sum+=digit
# # #     n//=10
# # # print(sum)




    
# # # n=9875
# # # sum=0
# # # for i in range(1,n+1):
# # #     digit=n%10
# # #     sum+=digit
# # #     n//=10
# # # print(sum)

# # # n=9875
# # # sum=0
# # # for i in range(1,n+1):
# # #     digit=n%10
# # #     sum+=digit
# # #     n//=10
# # # print(sum)

# # # s='[a,b,c,d,e,f]'
# # # print(s[::-1])

# # # print(s[1:3:-1] [2:4])

# # # a=[100,200,300,400,500,600]
# # # print(a[-4:-1])

# # # s="DataScience"
# # # print(s[1:8:2])

# # s="TCSNQT2025"
# # # print(s[:-4])
# # print(s[1:])

# # s1="python"
# # s2="language"
# # print(s1>s2)

# # """call by Value=value
# # call by reference=memory addresss

# # strig behavior is immutable koi""" 


# # a = 25 
# # b = 25
# # print(id(a)) 
# # print(id(b)) 

# li=[1,2,3,5,6,5.0,'python']
# # print(min(li))
# # print(max(li))
# # print(len(li))
# # print(id(li))
# # print(sum(li))
# # print(type(li))
# # print(list())

# # li.append(0)
# # print(li)

# # li.sort()
# # print(li)

# # print(li.count(5))

# # li.extend([1,2,3])
# # print(li)

# # li.copy()
# # print(li)

# # print(li.index('python'))

# # li.reverse()
# # print(li)

# # li.insert(1,'java')
# # print(li)

# # li.pop(1)
# # print(li)

# # li.remove(3)
# # print(li)

# # li.clear()
# # print(li)

# # del li
# # print(li)

# # x=li.copy()
# # print(x)
# # print(li)

# a='Python is a language'
# # s=a.split()
# # print(s)
# # print(a.capitalize())
# # print(a.upper())
# # print(a.lower())
# # print(a.title())
# # print(a.count('a'))
# # print(a.index('o'))
# # c=','.join([a,b])
# # print(c)


# #create
# d1=dict()

# #read
# print(d1)

# #update
# dd={1:'name',
#     2:'age',
#     3:'course',
#     4:'institute'}
# d1.update(dd)
# print(d1)

# #delete
# d1.pop(2)
# print(d1)


# d1.popitem()
# print(d1)

# print(d1.get(1))
# print(d1.items())

# print(d1.keys())

# n=int(input("Enter a number :"))
# i=1
# while i<=5:
#     print('*'*i + " "*(n-i))
#     i+=1

# n=int(input("Enter a number :"))
# i=1
# while i<=n:
#     print(" "*(n-i)+"*"*i)
#     i+=1

# n=int(input("Enter a number :"))
# i=0
# while i<=n:
#     print("*"*n + " "*i)
#     n-=1


# n=5
# i=0
# while i<n:
#     print(' '*i+'* '*(n-i))
#     i+=1

# n=int(input("Enter a number :"))
# rev=0
# n2=n
# while n>0:
#     last_digit=n%10
#     rev=rev*10+last_digit
#     n=n//10
# if n2==rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# m='madam'
# if m==m[::-1]:
#     print("palindrome")
# else:
#     print("Not palindrome")


# n=5
# i=0
# while i<=n:
#     print("5"*n+" "*i)
#     n=n-1

# n=5
# i=1
# for i in range(1,6):
#     print('5'*n+' '*i)
#     n=n-1

# ch='kumkum'
# count=0

# for char in ch:
#     if char=='m':
#         count+=1
# print(count)


# n=5
# i=0
# while i<n:
#     print(' '*i+'* '*(n-i))
#     i+=1


# n=int(input("Enter a number :"))
# ans=n
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit**n
#     n=n//10
# if sum==ans:
#     print("Armstrong")
# else:
#     print("Not an Armstrong")

# m='kuki'
# count=0
# for ch in m:
#     count+=1
# print(count)

# li=[1,2,3,5,6,9]
# count=0
# for _ in li:
#     count+=1
# print(count)

# li=[1,2,3,9]
# sum=0
# for i in li:
#     sum+=i
# print(sum)

# li=[9,8,3,4,10,90]
# max=li[0]
# for i in li:
#     if i>li[0]:
#         max=i
# print(max)

# li=[1,3,4,2,7,0]
# min=li[0]
# for i in li:
#     if i<li[0]:
#         min=i
# print(min)


# li=[1,3,4,3,5,3,5,3]
# count=0
# target=5
# for _ in li:
#     if target==_:
#         count+=1
# print(count)


# li1=['kumkum']
# li2=['mata']
# # li2=[3,4,5,6]
# print(li1+li2)


# li3=['i am kumkum yadav']
# li4=['laila']
# # print(li3+li4)
# print(li3*3)


# tup1=(1,2,3,4)
# tup2=(3,56,6)
# print(tup1+tup2)
# print(type(tup1))

# set1={1,2,3,4}
# set2={2,3,4}
# print(set1+set2)   #error throw unsupported operand

# dic1={7:'m'}
# dic2={1:'age',
#       2:'name'}
# print(dic1+dic2) error throw unsupported operand


# li=[1,2,3,1,2,3,1,5,1]
# tar=3
# count=0
# for _ in li:
#     if _==tar:
#         count+=1
# print(count)

# li='python'
# li1=[]
# for i in range(len(li)-1,-1,-1):
#     li1+=li[i]
# print(li1)

# li='pythonnn'
# li1=[]

# for i in li:
#     if i not in li1:
#         li1+=i
# print(li1)


# def sub(a,b):
#     return a-b
# n1=int(input("Enter number 1 :"))
# n2=int(input("Enter number 2 :"))

# ans=sub(n1,n2)
# print(ans)



# def cal_mul(a,b):
#     return a*b
# n1=int(input("Enter number 1:"))
# n2=int(input("Enter number 2:"))

# sum=cal_mul(n1,n2)
# print(sum)


# def count_li(n):
#     return count
# n=eval(input("Enter a list :"))
# count=0
# for i in n:
#     count+=1
# print(count)


# n=5
# i=1
# while i<=n:
#     print(i,end=" ")
#     i+=1


# n=5
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)


# n=10
# i=1
# while i<=n:
#     if i%2==0:
#         print(f'{i}',end=' ')
#     i+=1

# n=10
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i+=1


# n=5
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)


# li=[10,20,30,40,50]
# for i in li:
#     i+=5
#     print(i)

# li=[10,20,30,40,50]
# i=0
# while i<len(li):
#     print(li[i]+5)
#     i+=1

# s='kumkum'
# li=[]
# li.append(s)
# print(li)

# l = [64, 34, 25, 12, 22, 11, 90, 5]
# max=l[0]

# for i in range(len(l)-1):
#     if i<max:
#         max=i
# print(max)



# Program to convert month name to number of days

# month = input("Enter month name: ")

# convert to lowercase for easy comparison
# month = month.lower()

# if month in ("january", "march", "may", "july", "august", "october", "december"):
#     print("31 days")
# elif month in ("april", "june", "september", "november"):
#     print("30 days")
# elif month == "february":
#     print("28 or 29 days")
# else:
#     print("Invalid month name")


# n=float(input("Enter a number :"))
# squ=n**0.5
# print(squ)


# year=int(input("Enter a year :"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("Leap year")
#         else:
#             print("Not leap")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")

# x=int(input("Enter x :"))
# y=int(input("Enter y :"))
# x,y=y,x
# print(x)
# print(y)

# x=int(input("Enter x :"))
# y=int(input("Enter y :"))
# x=x*y
# y=x/y
# x=x/y
# print(x)
# print(y)


# x=int(input("Enter x :"))
# y=int(input("Enter y :"))
# temp=x
# x=y
# y=temp
# print(x)
# print(y)


# t=(1,2,3)
# t1=()
# for i in range(len(t)-1,-1,-1):
#     t1+=(t[i],)
# print(t1)

# li=[1,2,3]
# t=()
# for i in li:
#     t+=(i,)
# print(t)

# t=(1,2,3)
# li=[]
# for i in t:
#     li.append(t)
# print(li)


# d={1:'a',
#    2:'b',
#    3:'c'}
# keys=[]
# for key in d:
#     keys.append(key)
# print(keys)
    

# s1={1,2,4,5,4}
# s2={59,8}
# s0=set()
# for i in s1:
#     s0.add(i)
# for i in s2:
#     s0.add(i)
# print(s0)


# s1={1,2,4,5,4}
# li=[]
# for i in s1:
#     li.append(i)
# print(li)


# n1=int(input("Enter number 1 :"))
# n2=int(input("Enter number 2 :"))
# if n1>n2:
#     max=n1
# else:
#     max=n2
# while 1:
#     if max%n1==0 and max%n2==0:
#         break
# print(max)

# n1=int(input("Enter number 1 :"))
# n2=int(input("Enter number 2 :"))
# if n1>n2:
#     max=n1
# else:
#     max=n2
# while 1:
#     if max%n1==0 and max%n2==0:
#         break
# print(max)


# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# s1='listen'
# s2='kumkum'
# for i in s1:
#     pass
# if i in s2:
#     print("anagram")
# else:
#     print("not an anagram")


# n=int(input("Enter a number :"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)


# n=int(input("Enter a number :"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("Prime")
# else:
#     print("Not a prime")


# n1=int(input("Enter number 1 :"))
# n2=int(input("Enter number 2 :"))

# if n1<n2:
#     min=n1
# else:
#     min=n2
# for i in range(1,min+1):
#     if n1%i==0 and n2%i==0:
#         break
# print(i)

# n=5
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print()


# k=[]
# for i in range(10,1,-2):
#     k.append(i)
#     for j in k:
#         print(j,end=" ")
#     print()


# d1={1:'kumkum',2:"app",3:"B"}
# d2={5:'mantasa'}
# merge={}
# for key in d1:
#     merge[key]=d1[key]
# for key in d2:
#     merge[key]=d2[key]
# print(merge)


# d={1:'kumkum',2:"app",3:"B"}

# for key in d:
#     print(key)
    

# d={1:'kumkum',2:"app",3:"B"}
# for key in d:
#     print(d[key])


# d={1:'kumkum',2:"app",3:"B"}
# target='kumkum'
# for key in d:
#     if d[key]==target:

#         print("yes")
#         break
# else:
#     print("not")


# ***** 
# ****
# *** 
# ** 
# *
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*(2*i-1))


# Python program to get the Fibonacci series. (0,1,1,2,3,5,8,13,21……………..)
# n=5
# first,second=0,1
# print(first)
# print(second)
# for i in range(1,n+1):
#     next=first+second
#     first=second
#     second=next
#     print(next)



# n=int(input("Enter a number :"))
# ans=n
# x=len(str(n))
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit**x
#     n//=10
# if ans==sum:
#     print("Armstrong")
# else:
#     print("Not armstrong")


# power=5
# base=2
# ans=base**power
# print(ans)


# l=[64,89,22,5,1,5,77]
# n=len(l)
# for i in range(1,n-1):
#     for j in range(n-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)


# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j*2-1,end=' ')
#     print()


# n=5
# k=[]
# for i in range(10,1,-2):
#     k.append(i)
#     for j in k:
#         print(j,end=" ")
#     print()


# n=int(input("Enter a number :"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("Not prime")


# n=int(input("Enter a number :"))
# ans=n
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==ans:
#     print("prefect")
# else:
#     print("Not perfect")

# n=5
# for i in range(1,n+1):
#     ch='A'
#     for j in range(1,i+1):
#          print(ch,end=" ")
#          ch=chr(ord(ch)+1)
#     print()

# s='kumkum'
# l='aeiouAEIOU'
# v_count=0
# c_count=0
# for i in s:
#     if i in l:
#         v_count+=1
# print(v_count)
# for i in s:
#     if i not in l:
#         c_count+=1
# print(c_count)


# n=1412
# sum=0
# ans=n
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n//=10
# mul=1
# while n>0:
#     digit=n%10
#     mul=mul*digit
#     n//=10
# if sum==mul:
#     print("Spy ")
# else:
#     print("Not")


# n=5
# ch='A'
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
#     if ch>'Z':
#         ch='A'
#     print()


# n=5
# num=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# n=5
# for i in range(1,n+1):
#     print(" "*(n-1)+"*"*i)


# n=int(input("Enter the number of rows: ")) 
# for i in range(1,n+1): 
#     print(" "*(n-i),"*"*(2*i-1))


# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# n=int(input("Enter a number :"))
# factorial(n)

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#         return fact
# n=int(input("Enter a number :"))
# result=factorial(n)
# print(result)




