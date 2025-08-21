# movies=[]
# mov1=input("Enter your favorite movie name :")
# mov2=input("Enter your favorite movie name :")
# mov3=input("Enter your favorite movie name :")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

#grade=("C","D","A","A","B","B","A",)
# print(grade.count("A"))
# grade=["C","D","A","A","B","B","A",]
# grade.sort()
# print(grade)

# x,y,z='kuki','mohni','babita'
# print(x)
# print(z)
# print(y)

# a=b=c='kuki'
# print(a)
# print(b)
# print(c)



n=[1,2,3,4,5]
print(' choose any one \n 1= +\n 2= -\n 3= % \n 4= *\n 5= off\n')
while True:
    n0=(1,2,3,4)
    n=int(input("Enter any one :"))
    if n==1:
        n1=int(input("Enter number 1 :"))
        n2=int(input("Enter number 2 :"))
        n3=n1+n2
        print(f'sum of {n1} and {n2} is = {n3}')
    elif n==2:
        n1=int(input("Enter number 1 :"))
        n2=int(input("Enter number 2 :"))
        n3=n1-n2
        print(f'subtraction of {n1} and {n2} is = {n3}')
    elif n==3:
        n1=int(input("Enter number 1 :"))
        n2=int(input("Enter number 2 :"))
        n3=n1%n2
        print(f'divide of {n1} and {n2} is = {n3}')
    elif n==4:
        n1=int(input("Enter number 1 :"))
        n2=int(input("Enter number 2 :"))
        n3=n1*n2
        print(f'multiplication of {n1} and {n2} is = {n3}')
    else:
        break



