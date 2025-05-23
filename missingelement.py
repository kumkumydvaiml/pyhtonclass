# li=[1,2,4,6]

# for i in range(1,len(li)):
#  if li[i]-li[i-1]>1:
#   print(li[i-1]+1)
 

 
li=[10,30,5,6]
for i in range(1,len(li)):
 if li[i]-li[i-1]>1:
  for j in range(li[i]-1):
    print(li[i-1]+1)
   
   
