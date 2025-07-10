# n=1
# while n<=100:
#     print(n)
#     n+=1

# n=100
# while n>=1:
#     print(n)
#     n-=1

# num=int(input("Enter a number :"))
# n=1
# while n<=10:
#     print(num*n)
#     n+=1

# li=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(li):
#     print(li[idx])
#     idx+=1

# li=(1,4,9,16,25,36,49,64,81,100)
# x=36
# idx=0
# while idx<len(li):
#     if (li[idx]==x):
#         print("found",idx)
#     else:
#         print("finding")
#     idx+=1


# for i in range(100 ,0,-1):
#     print(i)


# n=int(input("Enter a number :"))
# for i in range(1,11):
#     print(n*i)

# sum=0
# for i in range(1,11):
#     sum=i+sum
# print("Total sum = ",sum)

# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     print(i,end=" ")

# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     print(i**2,end=" ")

# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i)

# sum=0
# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     sum+=i
# print("Sum = ",sum)

# str="kumkum"
# for i in range(len(str)-1,-1,-1):
#      print(str[i])


# vowels='aeiou'
# word='education'
# count=0
# for char in word:
#     if char in vowels:
#         count+=1
# print(f"Total vowels in {word} is {count}")

# first=0
# second=1
# n=int(input("Enter a number :"))
# print(first,second,end=" ")
# for i in range(1,n-1):
#     next=first+second
#     first=second
#     second=next
#     print(next,end=" ")

# fact=1
# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# n=int(input("Enter a number :"))
# for i in range(2,n):
#     if n%i==0:
#         print("Not a prime")
#         break
# else:
#     print("prime")


# n=int(input("Enter a number :"))
# is_prime=True
# for i in range(2,int(n**0.5)+1):
#     if n%i==0:
#         is_prime=False
#         break
# if is_prime and n>1:
#     print(n,"is a prime member")
# else:
#     print(n,"is not a prime member")

# n=10
# while n<=15:
#     print(n,end=" ")
#     n+=1


# n=1
# while n<=5:
#     print(n**3)
#     n+=1

# n=1
# while n<=10:
#     if n%2!=0:
#         print(n)
#     n+=1

# n=1
# mul=1
# while n<=5:
#     mul*=n
#     n+=1
# print(mul)

# is_prime=True
# n=int(input("Enter a number :"))
# for i in range(2,int(n**0.5)+1):
#     if n%i==0:
#         is_prime=False
#         break
# if is_prime and n>1:
#     print(n,"is prime member")
# else:
#     print(n, "is not a prime member")


# sum=0
# n=input("Enter a number :")
# n1=int(len(n))
# n=int(n)
# ans=n
# while n>0:
#     digit=n%10
#     sum=sum+digit**n1
#     n//=10
# if ans==sum:
#     print("Armstrong")
# else:
#     print("Not an armstrong")


# word='Education'
# count=0
# for char in word:
#     if char in word:
#         count+=1
# print(f"{count} Letter in {word} ")

# count=0
# n=int(input("Enter digits :"))
# while n>0:
#     digit=n%10
#     count+=1
#     n//=10
# print(f"Total digits are {count}")

# a=10
# b=20
# c=a+b
# a=c-a
# b=c-b
# print("a = ",a)
# print("b = ",b)


# 1. Write a program to find maximum between two numbers.

# n1=int(input("Enter number 1 :"))
# n2=int(input("Enter number 2 :"))
# if n1>n2:
#     print("Greatest number is",n1)
# else:
#     print("Greatest number is",n2)


# 2. Write a program to find maximum between three numbers.
# n1=int(input("Enter number 1 :"))
# n2=int(input("Enter number 2 :"))
# n3=int(input("Enter number 3 :"))
# if n1>n2 and n1>n3:
#     print("Greatest number is",n1)
# elif n2>n1 and n2>n3:
#     print("Greatest number is",n2)
# else:
#     print("Greatest number is",n3)

# 3. Write a program to check whether a number is negative,
# positive or zero.
# n=int(input("Enter a number :"))
# if n>0:
#     print("Number is positive")
# elif n<0:
#     print("Number is negative")
# else:
#     print("Number is zero")

# 4. Write a program to check whether a number is divisible by 5
# and 11 or not.
# n=int(input("Enter a number :"))
# if n%5==0 and n%11==0:
#     print("No. is divisible of 5 and 11")
# else:
#     print("Not divisible of 5 and 11")

# 5. Write a program to check whether a number is even or odd.
# n=int(input("Enter a number :"))
# if n%2==0:
#     print("Even number")
# else:
#     print("Odd number")

# 6. Write a program to check whether a year is leap year or not.
# year=int(input("Enter the year :"))
# if (year%4==0) or (year%400==0 and year%100!=0):
#     print("Year is a leap year")
# else:
#     print("Year is not a leap year")

# 7. Write a program to check whether a character is alphabet or
# not.
# ch=input("Enter any alphabet :")
# if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
#     print("It's a character/alphabet")
# else:
#     print("It's not a character/alphabet")


# 8. Write a program to input any alphabet and check whether it is
# vowel or consonant.
# ch=input("Enter any character :")
# li='aeiouAEIOU'

# if ch in li:
#     print("It's an Vowel")
# else:
#     print("It's a consonant")

# 9. Write a program to input any character and check whether it is
# alphabet, digit or special character.
# n=input("Enter a any digit or special character or a;phabet what you want : ")
# if n>='0' and n<='9':
#     print("Its a digit")
# elif (n>='A' and n<='Z') or (n>='a' and n<='z'):
#     print("Its an alphabet")
# else:
#     print("Its a special character")


# 10. Write a program to check whether a character is uppercase or
# lowercase alphabet .
# 11. Write a program to input week number and print week day .
# 12. Write a program to input month number and print number of
# days in that month.
# 13. Write a program to count total number of notes in given
# amount .
# 14. Write a program to input angles of a triangle and check whether
# triangle is valid or not.
# 15. Write a program to input all sides of a triangle and check
# whether triangle is valid or not.
# 16. Write a program to check whether the triangle is equilateral,
# isosceles or scalene triangle.
# 17. Write a program to calculate profit or loss.
# 18. Write a program to input marks of five subjects Physics,
# Chemistry, Biology, Mathematics and Computer. Calculate
# percentage and grade according to following:
# Percentage &gt;= 90% : Grade A
# Percentage &gt;= 80% : Grade B
# Percentage &gt;= 70% : Grade C
# Percentage &gt;= 60% : Grade D
# Percentage &gt;= 40% : Grade E
# Percentage &lt; 40% : Grade F

# 19. Write a program to input basic salary of an employee and
# calculate its Gross salary according to following:
# Basic Salary &lt;= 10000 : HRA = 20%, DA = 80%
# Basic Salary &lt;= 20000 : HRA = 25%, DA = 90%
# Basic Salary &gt; 20000 : HRA = 30%, DA = 95%
# sal=float(input("Enter your basic salary :"))
# hra=0
# da=0
# if sal<=10000:
#     hra=(sal*20)/100
#     da=(sal*80)/100
# elif sal<=20000:
#     hra=(sal*25)/100
#     da=(sal*90)/100
# else:
#     hra=(sal*30)/100
#     da=(sal*95)/100
# gross=sal+hra+da
# print(gross)






# 20. Write a program to input electricity unit charges and calculate
# total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill


# a=10
# b=10.0
# if a==b:
#     print("True")
# else:
#     print("False")


# n=int(input("Enter number :"))
# for i in range(1,n):
#     for j in range(1,n):
#         print(j,end=" ")
#     print()

# ch=65
# for i in range(65,70):
#     for j in range(65,70):
#         if ch==65:
#             print("A",end="")
#     print()


# for i in range(6,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(1,10):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# word='Education'
# count=0
# for char in word:
#     if char in word:
#         count+=1
# print(f"{count} Letter in {word} ")

# count=0
# vowel="aeiou"
# word="kumkum"
# for char in word:
#     if char in vowel:
#         count+=1
# print(count,"Vowels in kumkum")


    
    



















