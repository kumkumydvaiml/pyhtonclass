# n=int(input("Enter a number :"))
# if n>0:
#     print("Positive.")
# elif n<0:
#     print("Negative.")
# else:
#     print("Zero.")


# marks=int(input("Enter a number :"))
# if marks>=80 and marks<90:
#     print("A grade")
# elif marks>=60 and marks<80:
#     print("B grade")
# elif marks>=60 and marks<40:
#     print("C grade")
# elif marks>0 and marks<40:
#     print("D grade")
# else:
#     print("Invalid")

# n=int(input("Enter a number :"))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")


# n1=int(input("Enter number 1 :"))
# n2=int(input("Enter a number 2 :"))
# n3=int(input("Enter a number 3 :"))
# if n1>n2 and n1>n3:
#     print("number 1 is largest")
# elif n2>n1 and n2>n3:
#     print("number 2 is largest")
# else:
#     print("number 3 is largest")


# year=int(input("Enter the year :"))
# if (year%4==0) or (year%400==0 and year%100!=0):
#     print("Leap year")
# else:
#     print("Not a leap year")


# age=int(input("Enter your age :"))
# if age>=18:
#     print("You can vote")
# else:
#     print("Not eligible for vote")


# ch=['a','e','i','o','u','A','E','I','O','U']
# ch1=input("Enter any character :")
# if ch1 in ch:
#     print("Its a vowel ")
# else:
#     print("Consonant")


# pwd=int(input("Enter your password :"))
# if pwd==1234:
#     print("Welcome")
# else:
#     print("Try again")

amt=int(input("Enter amount :"))
if (amt>0 or amt<1000):
    print("Discount is provide you 5% a/c to your amount",amt*5/100)
elif (amt>=1000 or amt<5000):
    print("Discount is provide you 10% a/c to your amount",amt*10/100)
elif (amt>=5000 or amt<10000):
    print("Discount is provide you 15% a/c to your amount",amt*15/100)
elif (amt>=10000 or amt<30000):
    print("Discount is provide you 20% a/c to your amount",amt*20/100)
else:
    print("Inavlid amount")
    
    
    








