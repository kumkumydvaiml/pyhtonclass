n=int(input("Enter 1 :"))
if(n==1):
    n=int(input("Choose 2,3 or 4 :"))
    if(n==2):
        n=int(input("Choose 3 or 4 :"))
        if(n==3):
            n=int(input("Enter 4 :"))
            if(n==4):
                print("Reached")
            elif(n==4):
                print("Reached") 
        else:
            print("Invalid")

    elif(n==3):
        n=int(input("Choose 2 or 4 :"))
        if(n==2):
            n=int(input("Enter 4 :"))
            if(n==4):
                print("Reached")
            else:
                print("Invalid")
    elif(n==4):
            print("Reached")
    else:
            print("Invalid")           
else:
    print("Invalid")        