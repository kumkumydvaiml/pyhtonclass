n=int(input("Enter 1 :"))
if(n==1):
    n=int(input("Choose 2,3 0r 4:"))
    if(n==2):
       n= int(input("Enter 3 or 4"))
       if(n==3):
           n=int(input("Enter 4:"))
           if(n==4):
               print("reached")
       elif(n==4):
           print("reached") 
       else:
           print("invalid")  


    elif(n==3):
        n=int(input("Enter 2 or 4"))
        if(n==2):
            n=int(input("Enter 4"))
            if(n==4):
                print("reached")
            else:
                print("invalid")
        elif(n==4):
            print("reached")          
        else:
            print("invalid")    

    elif(n==4):
        print("reached")
    else:
        print("invalid")

else:
    print("invalid")
