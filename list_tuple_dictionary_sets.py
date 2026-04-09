# list in python  and list is mutable means we can change the vaule using ind
# student=["shivam",99,17,"delhi"]
# print(student[0])
# student[0]="pandey"
# print(student[0])
# print(student)

# list slicing {similar to that of the string slicing}  {the last index is not included in the slicing...}
# marks=[87,64,33,95,76]
# print(marks[1:4])
# print(marks[:4])
# print(marks[0:])
# print(marks[0:len(marks)])
# print(len(marks))

# list methods...
# list = [2,1,3]
# list.append(4) #adds one element at end
# print(list)

# list.sort() # in the complete list is got sorted it also work for the alphabte in ascending order.
# print(list)

# list.sort(reverse=True) # here in these we got the sorted in reverse order...
# print(list)

# list.reverse() #reverse the given list..
# print(list)

# list.insert(0,0) # here these insert method used for the insertion of the element at the specific index ... first is index and the second one is value..
# print(list)


# list.remove(2) # here these remove method is used for the removal of the value from the list it removes the value occuring first 
# print(list)

# list.pop(2) # here in these it remove the value at the specific index we will write their... 
# print(list)

# list[0]=3  # here in list we can change the value using the indexing... 
# print(list)

# tuples in python....{it is immutable we cannot assign value in tuple.}

# tuple=(341,143,31,143,34,65,65,76,78,87,65,43,4567)
# hello=tuple[0]
# print(hello)

# empty tuple
# tuple=()
# print(tuple)
# print(type(tuple))

# single tuple
# tuple=(1,) #without the commo in last it will take it is integer
# print(tuple)
# print(type(tuple))

# slicing in tuples , slicing in tuple take same the last index is not included...

# tup=(231,3,314,243,453,5534,765,865,54413)
# print(tup[0:2])

# tuple method 
# 1st tup.index(element) the element we write in these method return the index of that element...

# tup=(231,3,314,243,453,5534,765,865,54413)
# index=tup.index(3)
# print(index)

# 2nd tup.count(element) here we write any element it will return the count of the element...
# tup=(231,3,314,243,453,5534,765,865,54413)
# count=tup.count(3)
# print(count)

# wap to ask the user to enter the name of their three fav movie..
# name1=input("enter the name of the 1st fav movie=")
# name2=input("enter the name of the 2nd fav movie=")
# name3=input("enter the name of the 3rd fav movie=")
# list=[name1,name2,name3]
# print(list)
# print(type(list))

# now 2nd method of appending...
# list=[]
# name1=input("enter the name of the 1st fav movie=")
# list.append(name1)
# name2=input("enter the name of the 2nd fav movie=")
# list.append(name2)
# name3=input("enter the name of the 3rd fav movie=")
# list.append(name3)
# print(list)
# print(type(list))

# # check the given list is palindrome or not... taking list as a input
# name1=input("enter the name of the 1st fav movie=")
# name2=input("enter the name of the 2nd fav movie=")
# name3=input("enter the name of the 3rd fav movie=")
# list=[name1,name2,name3]

# copy_list=list.copy()
# copy_list.reverse()
# if(copy_list==list):
#     print("yes it palindrome")
# else:
#     print("not it is not palindrome")
    
# # wap to count the number of student's with the "A" grade in the following tuple
# list=["A","A","B","C","D","F","A","D"]
# count_A=list.count("A")
# print(count_A)

# store the list in the sorted manner. means sort the list.
# list=["A","A","B","C","D","F","A","D"]
# list.sort()
# print(list)

# Dictionary ansd sets

# dictionaries are used to store data value in key:value pairs ,, they are unordered , mutable i.e changeable , we can also add the new key value pair..
# dict={
#     "name":"shivam",
#     "cgpa":"9.14",
#     "marks":[72,525,55,78]
# }
# print(dict)
# print(dict["name"])
# print(dict["cgpa"])
# print(dict["marks"])
# print(dict)
# dict["name"]="pandey"
# print(dict)

# we can also create a null/empty dictionary.
# null_dict={}
# print(null_dict)
# print(type(null_dict))


# we can also create a nested dictinary i.e dictionary ke andar dictionary...
# student={
#     "name":"shivam rajesh pandey",
#     "subject":{
#         "maths":68,
#         "ML":70,
#         "AI":55,
#     },
#     "college_name":"VIT",
#     "year":"3rd"
# }
# # print(student)
# # print(student["subject"])# how to get the value of the specific key value pair.
# student["subject"]="maths"#how to change the value of key pair..
# print(student)

# now learning some dictionary methods 
# 1st mydict.keys() these help to get all the  key from the dictionary. these return only the outer key not the nested one...
# student={
#     "name":"shivam rajesh pandey",
#     "subject":{
#         "maths":68,
#         "ML":70,
#         "AI":55,
#     },
#     "college_name":"VIT",
#     "year":"3rd"
# }
# print(student.keys())

# 2nd mydict.values() these help to get all the value form the dictionary it return the netsed part as the value...

# student={
#     "name":"shivam rajesh pandey",
#     "subject":{
#         "maths":68,
#         "ML":70,
#         "AI":55,
#     },
#     "college_name":"VIT",
#     "year":"3rd"
# }
# print(student.values())

# 3rd mydict.items()  return all the key value pair as the tuple...

# student={
#     "name":"shivam rajesh pandey",
#     "subject":{
#         "maths":68,
#         "ML":70,
#         "AI":55,
#     },
#     "college_name":"VIT",
#     "year":"3rd"
# }
# print(student.items())

# 4th mydict.get(key)  return the value of the key we will be giving in these method

# student={
#     "name":"shivam rajesh pandey",
#     "subject":{
#         "maths":68,
#         "ML":70,
#         "AI":55,
#     },
#     "college_name":"VIT",
#     "year":"3rd"
# }
# print(student["name"])  # both student["name"] and student.get["name"] work same but the second one has the ability to manage the error like if the key is not their in the dictionary then the first one give error but the second one will give none
# print(student.get("name")) #if key is not their it will give us none...

# 4th mydict.update(what to chnage write here) it is used to update the exsisting key value pair and can be used to add the new key value pair.
student={
    "name":"shivam rajesh pandey",
    "subject":{
        "maths":68,
        "ML":70,
        "AI":55,
    },
    "college_name":"VIT",
    "year":"3rd"
}
student.update({"name":"navya pandey"})
student.update({"state":"maharastra"})
print(student)