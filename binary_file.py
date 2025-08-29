# 28/aug/25
#topic-- binary file


# import pickle
# f=open('n1.pkl','ab+')
# data={'name':'kumkum',
#       'age':20,
#       'quali':'btech'}
# pickle.dump(data,f)
# f.close()


# import pickle
# f=open('n_2.pkl','ab+')
# data=[1,2,3,4]      # append data
# pickle.dump(data,f)
# f.close()

# import pickle
# f=open('n_2.pkl','rb+')  #read data
# data=pickle.load(f)
# print(data)
# f.close()

# pickle.load(f)
# pickle.load(f)

# import pickle
# l=[]
# with open('n1.pkl','rb+') as f:
#     while True:
#         try:    
#             data=pickle.load(f)
#             l.append(data)
#         except EOFError:
#             break
# print(l)


def outer_fun(fun_name):
    def inner_fun():
        print('from inner function')
        x=fun_name()
    return inner_fun
def new():
    print('from new function')
res=outer_fun(new)
res()



