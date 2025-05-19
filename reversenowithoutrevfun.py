
# list=[4,2,5,1,6,9]
# a=0
# print(len(list))
# for i in list:
#  digit=list%10
#  a=a+digit
#  list=list//10
# if(list==a):
#  print(list)




li = [1,9,7,3,6,2,3,4,2]

i=0
j=len(li)-1

while i<j:
  temp=li[i]
  li[i]=li[j]
  li[j]=temp
  i=i+1
  j=j-1

print(li)