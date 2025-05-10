# b=(input("Enter bank name :"))
# if(b=="sbi"):
#     pin=int(input("Enter pin :"))
#     balance=10000
#     if(pin==1234):
#         b=input("Enter withdrawl, deposite or balance inquiry :")
#         if(b=='withdrawl'):
#             b=int(input("Enter amount how much you want to withdrawl :"))
#             if(b>0 and b<=10000):
#                 print("You have withdrawl :",b)
#                 print("Your current balance withdrawl is: ",balance-b)
#         elif(b=='deposite'):
#             b=int(input("Enter how much you want to deposite :"))
#             if(b>0):
#              print("You  deposite :",b)
#         elif(b=='balance inquiry'):
#             print(balance)

            
            
#         else:
#            print("Invalid")
# else:
#     print("Invalid")


e=input("Enter email id :")
if(e=='student@gmail.com'):
    p=int(input("Enter password :"))
    if(p==1234):
        print("Password is correct.")
    else:
        print("Try agin!")
else:
    print(" Invalid gmail :( ")        