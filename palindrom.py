n=int(input("Enter number :"))
rev=0
while n>0:
 ans=n
 digit=n%10
 rev=rev*10+digit
 n=n//10
if rev==ans:
 print("palilndrom")
else:
 print("Not a palindrom")





