# n=(input("Enter number :"))
# n1=len(n)
# n=int(n)
# sum=0
# ans=n
# while n>0:
#  digit=n%10
#  sum=sum+digit**n1
#  n=n//10
# if(sum==ans):
#  print("Armstrom")
# else:
#  print("not armstrom")


#  s1,s2="python","language"
#  s=','.join([s1,s2])
#  print(s)


# li=eval(input("Enter 5 name :"))
# s="_".join("li")
# print(s)

# s="python"
# x=s.count('')
# print(x)

s="python_language"
print(s.split())

s="this is python class"
print(s.split())  #space se spllit karta hai

s="python_language_this_is_python_class"
print(s.split("_")) 

s="python_language_this_is_python_class"
print(s.split("_",1)) 

# flavours of pyhton

# syntax string spilit()
# string.split('where','how')
# s="python","language"
# print((s.split()))

s="python"
x=s.replace("t","a")
print(x)

#space false hota hai
