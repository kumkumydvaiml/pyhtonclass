

n=int(input("Enter number :"))
g=0
while n>0:
    digit=n%10
    if(digit>g):
        g=digit
    n=n//10
print(g)                        
