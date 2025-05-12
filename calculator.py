
n1=int(input("Enter number1 :"))
n2=int(input("Enter number2 :"))
o=input("Enter operator :")
if(o=='+'):
    print(n1+n2)
elif(o=='-'):
    print(n1-n2)
elif(o=='/'):
    print(n1/n2)
elif(o=='*'):
    print(n1*n2)
elif(o=='%'):
    print(n1%n2)
else:
    print("Invalid")