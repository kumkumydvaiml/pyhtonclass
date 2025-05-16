n=(input("Enter number :"))
n1=len(n)
n=int(n)
sum=0
ans=n
while n>0:
 digit=n%10
 sum=sum+digit**n1
 n=n//10
if(sum==ans):
 print("Armstrom")
else:
 print("not armstrom")