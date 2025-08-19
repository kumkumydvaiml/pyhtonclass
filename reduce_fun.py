#reduce function 
#max
import functools
l=[10,5,8,20,25,30]
def max_digit(x,y):
    if x>y:
        return x
    else:
        return y
result=functools.reduce(max_digit,l,0)
print(result)

#min
import functools
l=[10,5,8,20,25,30]
def min_digit(x,y):
    if x<y:
        return x
    else:
        return y
result=functools.reduce(min_digit,l)
print(result)


#sum
import functools
l=[10,2,9,40,20]
def sum(x,y):
    return x+y
result=functools.reduce(sum,l)
print(result)

