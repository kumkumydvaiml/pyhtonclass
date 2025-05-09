s=input("Enter a :")
if(s=='a'):
    s=input("Enter b,c or d :")
    if(s=='b'):
        s=input("Enter q or d :")
        if(s=='q'):
            print("Reached")
        elif(s=='d'):
            s=input("Enter p or q :")
            if(s=='p'):
                print("Reached")
            elif(s=='q'):
                print("Reached")
            else:
                print("Invalid")

    elif(s=='c'):
        s=input("Enter f or o :")
        if(s=='f'):
            print("reached")
        elif(s=='o'):
            print("reached")
        else:
            print("invalid")
    elif(s=='d'):
        s=input("Enter i or e :")
        if(s=='i'):
            print("Reached")
        elif(s=='e'):
            s=input("Enter z :")
            if(s=='z'):
                print("Reached")
            else:
                print("Invalid")
        else:
            print("Invalid")
else:
    print("Invalid")    