# Ist Method
# n=input("Enter number :")

# print(n[::-1])


# 2nd method
# n=int(input("Enter number :"))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)



num=input("Enter number :")
print("palindrom") if num==num[::-1] else print("not a palindrom")

