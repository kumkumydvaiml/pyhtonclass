# x=eval(input("Enter any value :"))
# print(x)
# print(type(x))

# x=eval('2+3-1*5')
# print(x)


x=((1,2,3,4,6),)
sum=0
for i in x:
    for j in i:
        sum+=j
print(sum)

def add(*n):
    sum=0
    for i in x:
        for j in i:
            sum+=j
print(sum)



