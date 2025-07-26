# Methametical opeartions of set

s1={1,2,3,4,5}
s2={2,3,6,7,8}
print(s1.difference(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))

s1.symmetric_difference_update(s2)
print(s1)
s=set()
s.add('python')
print(s)

s.update('python')
print(s)
# s.update(10,20,30,40)
# print(s)

s.update('java','php')
print(s)

s.update('p','y','t','h','o','n')
print(s)

print(s.pop())
print(s)

s.remove('j')
print(s)




