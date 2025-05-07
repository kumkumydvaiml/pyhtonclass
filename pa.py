pa=int(input("Enter purchase amount :"))
if(pa>=5000):
    print("You got 20% discount")
    print("After 20% discount",pa-pa*20/100)
elif(pa>3000 and pa<5000):
    print("you got 15% discount")
    print("After 15% discount",pa-pa*15/100)
elif(pa>1000 and pa<3000):
    print("You got 10% discount")
    print("After 10% discount",pa-pa*10/100)
else:
    print("No discount")
    
    
