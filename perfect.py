n=int(input("Enter number :"))
ans=0
for i in range(1,n):
    if n%i==0:
        ans=ans+i
if ans==n:
    print("Perfect")
else:
    print("Not perfect")
