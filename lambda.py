# lambda function (anonymous function)
# lambda argument: expression
# 1. Use for small solutions/functionality we use lambda funtion
# to perform lambda task lambda funtion is more readable and faster then normal function
# mostly used with high order funtion like map() filter() and reduce()

prime=lambda x: x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))
print(prime(6))

# cube=lambda x:x*x*x
# print(cube(2))

# square=lambda x:x*x
# print(square(4))

greater=lambda x,y:x if x>y else y
print(greater(15,8))





