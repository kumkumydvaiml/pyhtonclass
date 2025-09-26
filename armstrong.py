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

# s="python_language"
# print(s.split())

# s="this is python class"
# print(s.split())  #space se spllit karta hai

# s="python_language_this_is_python_class"
# print(s.split("_")) 

# s="python_language_this_is_python_class"
# print(s.split("_",1)) 

# flavours of pyhton

# syntax string spilit()
# string.split('where','how')
# s="python","language"
# print((s.split()))

# s="python"
# x=s.replace("t","a")
# print(x)

#space false hota hai


# r,s="python","language"
# v=",".join([r,s])
# print(v)
# s="i am kumkum"
# v=s.split("a")
# print(v)

# s=r.isalnum()
# s=r.capitalize()
# s=r.casefold()
# s=r.count("p")
# s=r.encode() doubt
# s=r.endswith("n")
# s=r.find("e")
# s=r.index("u")
# s=r.isalpha()
# s=r.isascii()
# s=r.isdigit()
# s=r.isidentifier()
# s=r.isprintable()
# s=r.islower()
# s=r.isupper()
# s=r.replace("o","a")
# s=r.removesuffix("t")


# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     print("*"*i)


# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     print(" "*(n-i)+"*_"*i)


# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)

# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     print(" "*(2*n-i)+"* "*i)


# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     print(" "*(n-i)+"*_"*i)


# n=int(input("Enter a number :"))
# s="A"
# for _ in range(n+1):
#     print(s,end=" ")
#     s=chr(ord(s)+1)


# n=int(input("Enter a number :"))

# for i in range(1,n+1):
#     s="A"
#     for j in range(1,n+1):
#         print(s,end=" ")
#         s=chr(ord(s)+1)
#     print()


# n=int(input("Enter a number :"))
# s="A"
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(s ,end=" ")
#         s=chr(ord(s)+1)
#     print()


# n=int(input("Enter a number :"))
# s="A"
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     l=[]
#     for j  in range(1,i+1):
#         l.append(s)
#         s=chr(ord(s)+1)
#     print(" ".join(l))




n=int(input("Enter a number :"))
s="A"
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    l=[]
    for j  in range(1,i+1):
        l.append(s)
        s=chr(ord(s)+1)
    print(" ".join(l))

    
               



    

