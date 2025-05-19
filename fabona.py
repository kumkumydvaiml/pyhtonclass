n=int(input("Enter number :"))
first=0
second=1

print(first,second)
for i in range(n-2):
    next=first+second
    first=second
    second=next
    print(next)

    
