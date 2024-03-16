"""a=123
tuple_a = (5, "Six", a, 8.2)
#Accessing
print(tuple_a[1])
#inserting
tuple_a=tuple_a"""
"""
creating the dictionary with atleast 4 key value pairs
accessing the values using keys
accessing the whole dictionary through loops 
try to change the value
try to remove a key value pair from dictionary
"""
My_dic={"name":"kesava","age":20,"dept":"IT","city":"Kakinada"}
print(My_dic)
print(My_dic["name"])
print(My_dic["age"])
for eachKey in My_dic:
    print(My_dic[eachKey])
My_dic["age"]=23
del My_dic["dept"]
print(My_dic)
#memory allocation