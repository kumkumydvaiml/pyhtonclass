date=int(input("Enter date :"))
month=int(input("Enter month :"))
if(date>=10 and month<=6):
    p=input("Which place you want to choose j&k or goa :")
    if(p=='j&k'):
        print("Ticket price is 20000/- ")
        print("due to early booking we are giving you 40% discount :")
        print("After discount you got ticket price is",20000-(20000*40/100))
    elif(p=='goa'):
        print("Ticket price is 15000/- ")
        print("due to early booking we are giving you 40% discount :")
        print("After discount you got ticket price is",15000-(15000*40/100))
        
    else:
        print("Invalid")
elif(date>=20 and month<=5):
    p=input("Which place you want to choose j&k or goa ?")
    if(p=='j&k'):
     print("Ticket price is 15000/- ")
     print("due to early booking we are giving you 20% discount .")
     print("After discount you got ticket price is",15000-(15000*20/100))
    elif(p=='goa'):
       print("Ticket price is 10000/- ")
       print("due to early booking we are giving you 20% discount.")
       print("After discount you got ticket price is",10000-(10000*20/100))
    else:
        print("Invalid")
elif(date>=23 and month<=5):
    if(p=='j&k'):
     print("Ticket price is 10000/- ")
     print("No discount due to late booking ")
    elif(p=='goa'):
       print("Ticket price is 10000/- ")
       print("No discount due to late booking ")
        
else:
    print("Invalid")