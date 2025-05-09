w=input("Enter website name :")
if(w=='flipkart'):
    w=input("Enter product or service :")
    if(w=='product'):
        w=input("Enter clothes or shoes :")
        if(w=='clothes'):
            print("Clothes price is 2000 rs")
        elif(w=='shoes'):
            print("Shoes price is 1000 rs")
    elif(w=="service"):
        print("Not available")
    else:
        print("Invalid")
else:
    print("Invalid")