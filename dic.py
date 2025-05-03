#in dic we can store list also and we cannot change tuple that's why we use tuple in 
# keys because we cannot change keys
# there is no indexing in dic and its mutable
# can not repeat keys ex if we make key name then we cannot make it again
# agar koi value access karni hai toh index nahi key ke name se usko access kar sakte  hai
dic={
 "name": "kumkum",
 "subjects" : ["python","java","C","sql"],
 "age" : 18,
 "marks" : 90.3,
 "is_adult" : True
}
print(dic)
print(type(dic))
print(dic["name"]) #key ke help se value access
print(dic["subjects"])
dic["name"]="cybrom"  #agar kisi key ki value update karni hai to yese kar sakte hai
print(dic)

#for create empty dictionary use null
null_dic={}
print(null_dic)
print(type(null_dic))
print(dic.values())#if i want to access all values then use values function
dic.update({"city": "bhopal"})#to update 
print(dic)
