# i=1
# while i<=10:
#     print(i)
#     i+=1

# n=int(input("Enter a number :"))
# ans=1
# for i in range(1,n+1):
#  fact=ans*i
#  ans=fact
#  print(ans)



# sum=0
# n=1
# while n<=5:
#     sum=sum+n
#     n+=1
# print(sum)

# n=50
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         print(i,"Divisible by 3 or 5")

# sum=0
# n=int(input("Enter a number :"))
# for i in range(1,n):
#     sum+=i*i
# print(sum)

# i=1
# n=int(input("Enter a number :"))
# while i<=10:
#     print(n*i)
#     i+=1

# n=int(input("Enter a number :"))

# for i in range(2,n):
#     if n%i==0:
#         print("Not a prime")
#         break
# else:
#     print("Prime")

# rev=0
# n=int(input("Enter a number :"))
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)

# first=0
# second=1
# next
# n=int(input("Enter a number :"))
# print(first)
# print(second)
# for i in range(1,n-2):
#     next=first+second
#     first=second
#     second=next
#     print(next)

# rev=0
# n=int(input("Enter a number :"))
# ans=n
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if ans==rev:
#     print("Palindrom")
# else:
#     print("Not a palindrom")


# count=0
# n=int(input("Enter a number :"))
# while n>0:
#     digit=n%10
#     count+=1
#     n=n//10
# print("Count = ",count)
    
# sum=0
# n=int(input("Enter a number :"))
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# print(sum)



# start=int(input("Enter start of range :"))
# end=int(input("Enter end of range :"))
# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#             else:
#                 print(num,end= " ")


# base=int(input("Enter base :"))
# power=int(input("Enter power :"))

# for i in range(1,power):
#     ans=base**power
# print(ans)


# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# for i in range(6,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()






























