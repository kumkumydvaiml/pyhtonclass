
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



# def rev(s):
#     s1=""
#     for i in range(len(s)-1,-1,-1):
#         s1+=s[i]
#     return s1
# s=input("Enter a string :")
# result=rev(s)
# if s==result:
#     print("Palindrom")
# else:
#     print("Not a palindrom")


# n=input("Enter string :")
# target='k'
# count=0
# for i in n:
#     if i in target:
#         count+=1
# print(count)



# string=input("Enter atring :")
# result=""
# for i in string:
#     if 'A'<=i <='Z':
#         result+=chr(ord(i)+32)
# print(result)



# def lower(string):
#     result = ""
#     for i in string:
#         if 'A' <= i <= 'Z':      # agar uppercase hai
#             result += chr(ord(i) + 32)   # lowercase me convert karo
#         else:
#             result += i           # otherwise same character add karo
#     return result

# string = input("Enter a string: ")
# result = lower(string)
# print(result)


# def upper(string):
#     result = ""
#     for i in string:
#         if 'a' <= i <= 'z':       # agar lowercase hai
#             result += chr(ord(i) - 32)   # uppercase me convert karo
#         else:
#             result += i           # same add karo
#     return result

# string = input("Enter any string: ")
# result = upper(string)
# print(result)


# def space(sentence):
#     result=""
#     for i in sentence:
#         if i!=" ":
#             result+=i
#     return result
# sentence=input("Enter any sentence :")
# result=space(sentence)
# print(result)


# s1='aeiouAEIOU'
# def remove_vowels(word):
#     result=""
#     for i in word:
#         if i not in s1:
#             result+=i
#     return result
# word=input("Enter any word :")
# result=remove_vowels(word)
# print(result)


# def list_length(li):
#     count=0
#     for i in li:
#         count+=1
#     return count
# li=eval(input("enter a list :"))
# result=list_length(li)
# print(result)


# def count_words(word):
#     s1=""
#     count=1
#     for i in word:
#         if i==" ":
#             count+=1
#         else:
#             s1+=i
#     return count
# word=input("Enter any sentence :")
# count=count_words(word)
# print(count)


# def convert(s1,old,new):
#     s2=''
#     for i in s1:
#         if i==old:
#             s2+=new
#         else:
#             s2+=i
#     return s2
# s1=input("Enter a string :")
# old=input("Enter old letter :")
# new=input("Enter new letter :")
# s2=convert(s1,old,new)
# print(s2)

# s='kumkum'
# s1=''
# for i in range(len(s)):
#     if i == 0 and 'a' <= s[i] <= 'z':   # पहला letter
#         s1 += chr(ord(s[i]) - 32)       # capital में convert
#     elif 'A' <= s[i] <= 'Z':            # बाकी अगर capital हो
#         s1 += chr(ord(s[i]) + 32)       # तो छोटे में convert
#     else:
#         s1 += s[i]

# print(s1)


# def unique_ch(s):
#     s1=""
#     for ch in s:
#         if ch not in s1:
#             s1+=ch
#         else:
#             s+=ch
#     return s1
# s=input("Enter a string :")
# s1=unique_ch(s)
# print(s1)


# def frequency(s):
#     freq={}
#     for ch in s:
#         if ch in freq:
#             freq[ch]+=1
#         else:
#             freq[ch]=1
#     return freq
# s=input("Enter any string :")
# freq=frequency(s)
# print(freq)


# def count_list(li):
#     count=0
#     for i in li:
#         count+=1
#     return count
# li=eval(input("Enter a list :"))
# count=count_list(li)
# print(count)


# def sum_list(li):
#     sum=0
#     for i in li:
#         sum+=i
#     return sum
# li=eval(input("Enter a list :"))
# sum=sum_list(li)
# print(sum)


# def max_li(li):
#     max=li[0]
#     for i in li:
#         if i>max:
#             max=i
#     return max
# li=eval(input("Enter a list :"))
# max=max_li(li)
# print(max)


# def min_li(li):
#     min=li[0]
#     for i in li:
#         if i<min:
#             min=i
#     return min
# li=eval(input("Enter a list :"))
# min=min_li(li)
# print(min)
# n=int(input("Enter a digit :"))
# sum=0
# arm=n
# x=len(str(n))

# while n>0:
#     digit=n%10
#     sum=sum+digit**x
#     n//=10
# if arm==sum:
#     print('Armstrong')
# else:
#     print('Not armstrong')


n=int(input("Enter a digit  :"))
sum=0
arm=n
x=len(str(n))
for digit in str(n):
    sum+=int(digit)**x
if arm==sum:
    print('Armstrong')
else:
    print('Not armstrong')

    













        