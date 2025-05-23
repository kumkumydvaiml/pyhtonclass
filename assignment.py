# Que-1 WAP to check whether a number is negative,positive or zero? 
# n=int(input("Enter number :"))
# if n>0:
#     print("Positive")
# elif n<0:
#     print("Negative")
# else:
#     print("Zero")



# Que-2 WAP to check whether a number is divisible by 5 and 11 or not?
# n=int(input("Enter number :"))
# if n%5==0 and n%11==0:
#     print("Divisible of 5 and 11")
# else:
#     print("Not divisible of 5 and 11")



# Que-3 WAP to check whether a year is leap year or not?
# year=int(input("Enter year :"))
# if year%4==0:
#     print("Leap year.")
# else:
#     print("Not a leap year.")



# Que-4  WAP to find maximum between three numbers ?
# n1=int(input("Enter number1 :"))
# n2=int(input("Enter number2 :"))
# n3=int(input("Enter number3 :"))
 
# if n1>n2 and n1>n3:
#     print("Greatest number is",n1)
# elif n2>n1 and n2>n3:
#     print("Greatest number is",n2)
# else:
#     print("Greatest number is",n3)




# Que-5  WAP to find maximum between two numbers ?
# n1=int(input("Enter number1 :"))
# n2=int(input("Enter number2 :"))

# if n1>n2:
#     print("Greatest number is",n1)
# else:
#     print("Greatest number is",n2)




# Que-6  WAP to check even or odd ?

# n=int(input("Enter number :"))
# if n%2==0:
#     print("No is even.")
# else:
#     print("No is odd")



# Que-7  WAP to input all sides of a triangle and check wheather triangle is valid or not ?

# side1=int(input("Enter side1 of triangle :"))
# side2=int(input("Enter side2 of triangle :"))
# side3=int(input("Enter side3 of triangle :"))

# sum=side1+side2+side3

# if sum==180:
#     print("It's a triangle")
# else:
#     print("Not a triangle")



#  Que-8  WAP to input marks of five subjects Physics,Chemistry,Biology,Mathematics and Computer.Calculate percentage ang grade according to following :
# Percentage>=90% : Grade A
# Percentage>=80% : Grade B
# Percentage>=70% : Grade C
# Percentage>=60% : Grade D
# Percentage>=40% : Grade E
# Percentage<40% : Grade F


# m1=int(input("Enter your physics marks :"))
# m2=int(input("Enter your mathematics marks :"))
# m3=int(input("Enter your chemistry marks :"))
# m4=int(input("Enter your biology marks :"))
# m5=int(input("Enter your computer marks :"))

# marks=m1+m2+m3+m4+m5
# print(marks)
# percentage=marks/500*100

# print("Your percentage is ",percentage)

# if percentage>=90:
#     print("You got Grade A.")
# elif percentage>=80:
#     print("You got Grade B ")
# elif percentage>=70:
#     print("You got Grade C ")
# elif percentage>=60:
#     print("You got Grade D ")
# elif percentage>=40:
#     print("You got Grade E ")
# elif percentage<40:
#     print("You got Grade F ")



# Que-9  WAP to input any alphabet and check whether it is vowel or consonant?
# li=['a','e','i','o','u']
# ch=input("Enter any alphabet to check vowel or consonant :")

# if ch in li:
#     print("It's a vowel.")
# else:
#     print("It's a consonant.")




# Que-10  WAP to check whether a character is alphabet or not?
# ch=input("Enter character :")
# if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
#     print("It is a character.")
# else:
#     print("Not a character.")



# Que-11 WAP to check whether a character is lowercase or uppercase alphabet?

# ch=input("Enter any character :")
# if ch>='a' and ch<='z':
#     print("Character is lowercase .")
# elif ch>='A' and ch<='Z':
#     print("Character is uppercase.")
# else:
#     print("Invalid")



# Que-12 WAP to input week number and print week day ?

# dic={
#      1:'Monday',
#      2:'Tuesday',
#      3:'Wednesday',
#      4:'Thursday',
#      5:'Friday',
#      6:'Saturday',
#      7:'Sunday'
#      }
# day=int(input("Enter days in number :"))
# if day==1:
#     print("Monday")
# elif day==2:
#     print("Tuesday")
# elif day==3:
#     print("Wednesday")
# elif day==4:
#     print("Thursday")
# elif day==5:
#     print("Friday")
# elif day==6:
#     print("Saturday")
# elif day==7:
#     print("Sunday")
# else:
#     print("Invalid")




# Que-13 WAP to check whether the triangle is equilateral,isosceles or scalene triangle ?
# side1=int(input("Enter first side of triangle :"))
# side2=int(input("Enter second side of triangle :"))
# side3=int(input("Enter third side of triangle :"))

# if side1==side2==side3:
#     print("Equilateral triangle.")
# elif (side1==side2 or side2==side3 or side1==side3):
#     print("Isoscale triangle.")
# else:
#     print("Scalene triangle") 



#Que-14 WAP to input any character and check whether it is alphabet,digit or special character?

# ch=input("Enter any digit or character :")
# if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
#     print("It's is character.")
# elif ch>='0' and ch<='9':
#     print("It's a digit.")
# else:
#     print("Special symbol.")


# Que-15 WAP to input month number and print number of days in that month ? 
# dic={ 1:"January",
#       2:"Febuary",
#       3:"March",
#       4:"April",
#       5:"May",
#       6:"June",
#       7:"July",
#       8:"August",
#       9:"September",
#       10:"October",
#       11:"November",
#       12:"December"
#       }

# month=int(input("Enter month in digit:"))
# if month==1:
#     print("January 30 days")
# elif month==2:
#     print("Febuary 28 or 29 days")
# elif month==3:
#     print("March 31 days")
# elif month==4:
#     print("April 30 days")
# elif month==5:
#     print("May 31 days")
# elif month==6:
#     print("June 30 days")
# elif month==7:
#     print("July 31 days")
# elif month==8:
#     print("August 31 days")
# elif month==9:
#     print("September 30 days")
# elif month==10:
#     print("October 31 days")
# elif month==11:
#     print("November 30 days")
# elif month==12:
#     print("December 31 days")
# else:
#     print("Inavlid")


# Que-16 WAP to count total number notes in given amount ?

# amount= int(input("Enter a amount :"))
# notes=[2000,1000,500,300,100,50,20,10,5,2,1]

# for note in notes:
#     if amount>=note:
#      count=amount//note
#      amount%=note
#      print(f"{note} x {count}= {note*count}")


# Que-17 WAP to input all sides of a triangle and check whether triangle is valid or not ?

# side1=int(input("Enter first side :"))
# side2=int(input("Enter second side :"))
# side3=int(input("Enter third side :"))

# if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
#     print("Triangle is valid.")
# else:
#     print("Not a triangle.")

# Que-18 WAP to calculate profit or loss ?

# cp= float(input("Enter the cost price :"))
# sp= float(input("Enter the selling price :"))

# if sp>cp:
#     profit=sp-cp
#     print("Profit.")
# elif cp>sp:
#     loss=cp-sp
#     print("Loss.")
# else:
#     print("Neither profit nor loss")


# Que-19 WAP to input basic salary of an employee and calculate its Gross salary according to following :
#   Basic Salary <= 10000 : HRA =20 DA = 80%
#   Basic Salary <= 20000 : HRA =25 DA = 90%
#   Basic Salary > 20000 : HRA =30 DA = 95%

# basic=float(input("Enter your basic salary :"))
# if basic<=10000:
#     hra= (20*basic)/100
#     da=(80*basic)/100
# elif basic<=20000:
#     hra=(25*basic)/100
#     da=(95*basic)/100
# else:
#     hra=(30+basic)/100
#     da=(95*basic)/100
# gross = basic+hra+da
# print(gross)





# Que-20 WAP to input electricity unit charges and calculate total electricity bill according to the given condition :
#   For first 50 units Rs. 0.50/unit
#   For next 100 units Rs. 0.75/unit
#   For next 100 units Rs. 1.20/unit
#   For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill


# unit=float(input("Enter electricity bill :"))
# if unit<=50:
#      amount= unit*0.50
# elif unit<=150:
#      amount=(50*0.50)+ (100*0.75)+ ((unit-150)*1.20)
# else:
#      amount=(50*0.50)+(100*0.75)+(100*1.20)+((unit-250)*1.50)
# surcharge=amount*0.20
# total=amount+surcharge
# print("Electricity bill :",amount)
# print("Surcharge")
# print("Total electricity bill :",total)
     




































    
    

