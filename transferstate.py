# s="kumkum yadav"
# result=""
# for ch in s:
#     if s!=" ":
#         result+=ch
# print(result)

# n=5
# i=1
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i=i+1
# # print(i)
# i=i-2
# while i>0:
#     print(' '*(n-i)+'* '*i)
#     i=i-1


# n=5
# for i in range(1,n+1):
#     print('*'*i)


# s='python'
# s1=""
# for i in s:
#     print(chr(ord(i)+1))
#     s1=''.join([s1,chr(ord(i)+1)])
#transfer statement
#pass particular block ko skip

n=int(input("Enter :"))
i=1
while i<=n:
    if i==4 or i==7:
        pass
    else:
        print(i)  #break use to terminate any loop#continue skip current iteration
    i+=1

n=int(input("Enter :"))
i=1
while i<=n:
    if i==4 or i==7:
        i+=1
        pass#continue
    else:
        print(i)  
    i=i+1

#pass- skip current block
#continue- skip current iteration
#break- terminate any loop

print(print())


x=print()
print(x)
print(x)


print()

