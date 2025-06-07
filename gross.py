# Que-19 WAP to input basic salary of an employee and calculate its Gross salary according to following :
# Basic Salary <= 10000 : HRA =20 DA = 80%
# Basic Salary <= 20000 : HRA =25 DA = 90%
# Basic Salary > 20000 : HRA =30 DA = 95%

basic=float(input("Enter your basic salary :"))
if basic<=10000:
    hra= (20*basic)/100
    da=(80*basic)/100
elif basic<=20000:
    hra=(25*basic)/100
    da=(95*basic)/100
else:
    hra=(30+basic)/100
    da=(95*basic)/100
gross = basic+hra+da
print(gross)