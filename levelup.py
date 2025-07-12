#print numbers from 1 to N
# n=int(input("Enter the number :"))
# for i in range(1,n+1):
#     print(i)

#print even numbers from 1 to n?
# n=int(input("Enter number :"))
# for i in range(1,n+1):
#     if i%2==0:
#         print(f"Even numbers are {i}")

# 3. print odd numbers from 1 to n?
# n=int(input("Enter the  number :"))
# for i in range(1,n+1):
#     if i%2!=0:
#         print(f"Odd number are from 1 to {n} are {i} ")

# 4. print the table of a number ?
# n=int(input("Enter the number :"))
# for i in range(1,11):
#     print(i*n)

# 5. sum of first N natural numbers ?
# sum=0
# n=int(input("Enter the number :"))
# for i in range(1,n+1):
#     sum+=i
# print(f"Sum of natural number 1 to {n} is {sum}")

#6. factorial of a number ?
# fact=1
# n=int(input("Enter the number :"))
# for i in range(1,n+1):
#     fact*=i
# print(f"Factorial of {n} is {fact}")

#7. reverse a number ?
# rev=0
# n=int(input("Enter a number :"))
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print(f"Reverse of the number is {rev}")

#8. count the digits of a number ?
# count=0
# n=int(input("Enter the number :"))
# while n>0:
#     digit=n%10
#     count+=1
#     n//=10
# print(count)

#9. sum of digits of a number ?
# sum=0
# n=int(input("Enter the number :"))
# while n>0:
#     digit=n%10
#     sum+=digit
#     n//=10
# print(sum)

#10. check if a number is palindrome ?
# n=int(input("Enter the number :"))
# ans=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# if ans==rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# 11. perfect number ?
ans=0
n=int(input("Enter the number :"))
for i in range(1,n):
    if n%i==0:
        ans+=i
if ans==n:
    print("Perfect")
else:
    print("Not perfect")
  
    
    

