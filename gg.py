# li=[3,5,2,9]
# for i in range(len(0,li)):
        
    


n=int(input("Enter number :"))
first = 0
second = 1
for i in range(n):
   if i==0:
      print(first,end=" ")
      continue
   if i==1:
      print(second,end=" ")
      continue
   next=first+second
   first=second
   second=next
   print(next,end=" ")

