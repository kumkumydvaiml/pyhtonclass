
n=int(input("Enter number :"))
s=9
while n>0:
    digit=n%10
    if(digit<s):
        s=digit
    n=n//10
print("Smallest number is :",s)                        
