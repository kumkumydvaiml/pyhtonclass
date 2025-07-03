#1st method of prime number ?
n=int(input("Enter number :"))
count=0

for i in range(1,n+1):
    if n%i==0:
        count+=1

if count==2:
    print("Prime")
else:
    print("Not a prime")



# 2nd method of prime number ?

n=int(input("Enter a number :"))
is_prime=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        is_prime=False
        break
if is_prime and n>1:
    print(n,"is a prime member")
else:
    print(n,"is not a prime member")