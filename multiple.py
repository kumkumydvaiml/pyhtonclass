# class Parent1:
#     def home(self):
#         print("From parent")
# class Parent2:
#     def home(self):
#         print("from parent2")
# class Child(Parent1,Parent2):
#     pass

# obj=Child()
# obj.home()



# class Parent1:
#     def home(self):
#         print("From parent")
# class Parent2:
#     def home(self):
#         print("from parent2")
# class Child(Parent2,Parent1): # mro
#     pass

# obj=Child()
# obj.home()



class Parent:
    def home(self):
        print("From parent")
class Child(Parent):
    def home(self):
        print("from child")
        super().home()
obj=Child()
obj.home()


def rev(s):
    s1=""
    for i in range(len(s)-1,-1,-1):
        s1+=s[i]
    return s1
s=input("Enter a string :")
result=rev(s)
print(result)