
# def rev(s):
#     s1=""
#     for i in range(len(s)-1,-1,-1):
#         s1+=s[i]
#     return s1
# s=input("Enter a string :")
# result=rev(s)
# print(result)


# def count_list(li):
#     count=0
#     for i in li:
#         count+=1
#     return count
# li=eval(input("Enter any list :"))
# result=count_list(li)
# print(result)



def rev(s):
    s1=""
    for i in range(len(s)-1,-1,-1):
        s1+=s[i]
    return s1
s=input("Enter a string :")
result=rev(s)
if s==result:
    print("Palindrom")
else:
    print("Not a palindrom")
