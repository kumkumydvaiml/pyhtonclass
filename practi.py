# n=1
# while n<=100:
#     print(n)
#     n+=1

# n=100
# while n>=1:
#     print(n)
#     n-=1

# num=int(input("Enter a number :"))
# n=1
# while n<=10:
#     print(num*n)
#     n+=1

# li=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(li):
#     print(li[idx])
#     idx+=1

# li=(1,4,9,16,25,36,49,64,81,100)
# x=36
# idx=0
# while idx<len(li):
#     if (li[idx]==x):
#         print("found",idx)
#     else:
#         print("finding")
#     idx+=1


# for i in range(100 ,0,-1):
#     print(i)


# n=int(input("Enter a number :"))
# for i in range(1,11):
#     print(n*i)

# sum=0
# for i in range(1,11):
#     sum=i+sum
# print("Total sum = ",sum)

# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     print(i,end=" ")

# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     print(i**2,end=" ")

# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i)

# sum=0
# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     sum+=i
# print("Sum = ",sum)

# str="kumkum"
# for i in range(len(str)-1,-1,-1):
#      print(str[i])


# vowels='aeiou'
# word='education'
# count=0
# for char in word:
#     if char in vowels:
#         count+=1
# print(f"Total vowels in {word} is {count}")

# first=0
# second=1
# n=int(input("Enter a number :"))
# print(first,second,end=" ")
# for i in range(1,n-1):
#     next=first+second
#     first=second
#     second=next
#     print(next,end=" ")

# fact=1
# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# n=int(input("Enter a number :"))
# for i in range(2,n):
#     if n%i==0:
#         print("Not a prime")
#         break
# else:
#     print("prime")


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