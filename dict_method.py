d={'name':'kumkum',
   'age':'21',
   'quali':'btech'}
print(d.keys())
print(d.values())
print(d.items())
print(d.get('name'))


d1={
    1:'python',
    2:'php'
}
d.update(d1)
print(d)

d.setdefault('name1','rahul')
print(d)

l=['name','age','city','contact']
d=dict.fromkeys(l)
print(d)

d['name']='neeraj'
print(d)

d.pop('age')
print(d)

d.popitem()
print(d)









