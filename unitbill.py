unit=int(input("Enter unit :"))
if(unit>0 and unit<=50):
    print("per unit is 5 rs",unit*5)
elif(unit>50 and unit<=100):
    print("per unit is 10 rs",unit*10-1000-250)
elif(unit>100 and unit<=200):
    print("per unit is 20 rs",unit*20-4000-1000-250)
elif(unit>200 and unit<=300):
    print("per unit is 30 rs",unit*30-9000-4000-1000-250)
else:
    print("Invalid")




