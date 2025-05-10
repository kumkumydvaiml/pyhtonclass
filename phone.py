mob=input("Enter which mobile you want to purchase ?")
if(mob=='realme'):
    mob=input("There are 2 options you can purchase realme13 or realme13 pro choose :")
    if(mob=='realme13'):
        print("Realme price is 25000/-")
    elif(mob=='realme13pro'):
        print("Realme13 pro price is 30000/-")
    else:
        print("Invalid")

elif(mob=='iphone'):
    mob=input("There are 2 options you can purchase iphone14 or iphone15,choose which you want :")
    if(mob=='iphone14'):
        print("iphone14 price is 70000/- ")
    elif(mob=='iphone15'):
        print("iphone15 price is 80000/- ")
    else:
        print("Invalid input")

elif(mob=='oneplus'):
    mob=input("There are 2 options you can purchase oneplus node1 and node2 :")
    if(mob=='oneplus node1'):
        print("oneplus node1 price is 30000/-")
    elif(mob=='oneplus node2'):
        print("oneplus node3 price is 350000/-")
    else:
        print("Invalid")
else:
    print("Invalid Input")     

        