# r=6
# for i in range(1,r):
#     for j in range(1,r):
#         print("*",end=" ")
#     print()    
 

# r=6
# for i in range(1,r):
#  for j in range(1,r):
#   print("*",end=" ")
#  print()


# r=5
# for r in range(1,r+1):
#  for c in range(1,r+1):
#   if c>=6-r:
#    print("*",end=" ")
#   else:
#    print(" ",end=" ")
#  print()


# rows=5
# for r in range(1,rows+1):
#  for c in range(1,rows+1):
#    if c>=6-r:
    
#     print("*",end=" ")
#    else:
#     print(" ",end=" ")
#  print()


# r=5
# for i in range(1,r+1):
#  for j in range(1,i+1):
#   print("*",end=" ")
#  print() 


# n=int(input("Enter number :"))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev+digit
#     n=n//10
# print(rev)


# n=input("Enter the number :")
# n1=len(n)
# n=int(n)
# sum=0
# ans=n
# while n>0:
#     digit=n%10
#     sum=sum+digit**n1
#     n=n//10
# if(ans==sum):
#  print("No is an armstrong.")
# else:
#  print("No is not a armstrong.")    


n=input("Enter the number :")
len=len(n)
n=int(n)
sum=0
ans=n
while n>0:
    digit=n%10
    sum=sum+digit**len
    n=n//10
if ans==sum:
    print("No is an armstrong.")
else:
    print("No is not a armstrong.")