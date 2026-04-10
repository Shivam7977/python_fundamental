# list in python  and list is mutable means we can change the vaule using index...
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

# 4th mydict.update(what to change write here) it is used to update the exsisting key value pair and can be used to add the new key value pair.
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
# student.update({"name":"navya pandey"})
# student.update({"state":"maharastra"})
# print(student)

# set is the collection of the unordered items , each element in the set must be unique and immutable... same element  stored only once

# nums={1,2,3,3,4,3,5,5,6,6,}
# print(nums)
# print(type(nums))

# for empty set 
# nums={} # these is for the dictionary
# print(nums)
# print(type(nums))

# nums=set() # these is how we take empty set
# print(nums)
# print(type(nums))


# methods in set....
#  1st set.add(element) we use these for adding the element in set
# nums=set() # these is how we take empty set
# nums.add("shivam")
# print(nums)


# 2nd set.remove(element)

# nums={132,123,43,6,786,90,4,432,786,98,65} 
# print(nums)
# nums.remove(132) # if we try to remove the element which is not present...
# print(nums)
# print(type(nums))


# 3rd set.clear we use these for the clearing the complete set.
# nums={132,123,43,6,786,90,4,432,786,98,65}
# print(len(nums))
# print(nums)
# nums.clear()
# print(len(nums))
# print(nums)

# 4th set.pop() we used for removing the random element form the set...
# nums={132,123,43,6,786,90,4,432,786,98,65}
# print(nums.pop())

# set.union(set2) combines both set values and returns the new , only take once the repeated element in both.
# nums_1={132,123,43,6,76,90,4,432,746,98,65}
# nums_2={4531,65,4153,6,76,5454,43,6,98,65}
# print(nums_1.union(nums_2))
# print(nums_1.difference(nums_2)) # combines common values and return new set...
# # some example....

# store the following word meaning in a pyhton dictionary...
# 

# you are given a list of subject for students . assume one classroom is required for 1 subject . how many classroom are needed by all subject
# set={"j","p","j","p","c",'c++',"j","p","ai","j"}
# n=len(set)
# print("the number of class needed by assuming one classroom is required for 1 subject is",n)

"""wap to enter to enter marks of 3 subjects from the user and store them in a dictionary start with an 
empty dictionary and add one by one use subject name as a key and marks as a value.."""

# marks={}
# subject_1=float(input("enter the marks of 1st subject="))
# subject_2=float(input("enter the marks of 2nd subject="))
# subject_3=float(input("enter the marks of 3rd subject="))

# marks.update({"sub_1":subject_1})
# marks.update({"sub_2":subject_2})
# marks.update({"sub_3":subject_3})
# print(marks)

"""Create a dictionary storing your own details — name, age, city, 
and a list of your 3 hobbies. Print each value using its key."""

# dict={}
# name=input("enter your name=")
# age=int(input("eneter your age="))
# city=input("enter name of your city=")
# hobbie=["Coding","kabbadi","Watching TV"]
# dict.update({"name":name})
# dict.update({"age":age})
# dict.update({"city":city})
# dict.update({"hobbie":hobbie})
# print(dict)

"""You are given this list [4, 2, 7, 1, 9, 3] — sort it in ascending order, then reverse it, 
then remove the last element using .pop(). Print the list after each step."""

# list=[4, 2, 7, 1, 9, 3]
# list.sort()
# # print(list)

# list=[4, 2, 7, 1, 9, 3]
# list.reverse() #revesring the actual given list
# print(list)

# list=[4, 2, 7, 1, 9, 3]
# list.sort(reverse=True) #reverse in the decending order
# print(list)

# list=[4, 2, 7, 1, 9, 3]
# print(list)
# pop_1=list.pop()
# print(pop_1)
# print(list)
# pop_2=list.pop()
# print(pop_2)
# print(list)
# pop_3=list.pop()
# print(pop_3)
# print(list)
# pop_4=list.pop()
# print(pop_4)
# print(list)
# pop_5=list.pop()
# print(pop_5)
# print(list)
# pop_6=list.pop()
# print(pop_6)
# print(list)

"""Create a tuple of 5 of your favourite foods. Print the count of any one item and 
find the index of another item using tuple methods."""

# tuple=("icecream","noodles","chawal","dal","panner")
# print(tuple.count("icecream"))
# print("the index of the item chawal",tuple.index("chawal"))


"""Take 5 subject names as input from the user and store them in a list. 
Then remove duplicate subjects using a set and print how many unique subjects are there."""

# subject=[]
# subject_1=input("enter the name of 1st subject=")
# subject_2=input("enter the name of 2nd subject=")
# subject_3=input("enter the name of 3rd subject=")
# subject_4=input("enter the name of 4th subject=")
# subject_5=input("enter the name of 5th subject=")
# subject.append(subject_1)
# subject.append(subject_2)
# subject.append(subject_3)
# subject.append(subject_4)
# subject.append(subject_5)
# print("the 5 subjects are",subject)

# set={subject_1,subject_2,subject_3,subject_4,subject_5}
# print(set)
# print("the number of unique subjects are",len(set))

"""Take a student's name and marks of 4 subjects as input. 
Store them in a dictionary with subject names as keys. 
Then print the total marks and check if the student passed (passing marks = 40 per subject).
Print "Pass" or "Fail" accordingly."""

# # dict={}
# # name=input("enter your name=")
# # subject_1=int(input("enter the marks of 1st subject outoff 100="))
# # subject_2=int(input("enter the marks of 2nd subject outoff 100="))
# # subject_3=int(input("enter the marks of 3rd subject outoff 100="))
# # subject_4=int(input("enter the marks of 4th subject outoff 100="))
# # dict.update({"name":name})
# # dict.update({"subject_1":subject_1})
# # dict.update({"subject_2":subject_2})
# # dict.update({"subject_3":subject_3})
# # dict.update({"subject_4":subject_4})
# # print(dict)
# # total_marks=subject_1+subject_2+subject_3+subject_1
# # percent=(total_marks/400)*100
# # if(percent>=40):
# #     print("the student is pass")
# # else:
# #     print("the student is fail.")    
    
# """Create a dictionary of 5 items in a shop with item name as key and price as value. 
# Take an item name as input from the user and print its price using .get().
# If item is not found, print "Item not available"."""    

# dict_shop={
#     "apple":190,
#     "banana":60,
#     "dal":250,
#     "chawal":90,
#     "atta":80,
# }
# item=input("enter the product you want=").lower()
# if(item=="apple"):
#     print("the price of the apple is ",dict_shop.get("apple"))
# elif(item=="banana"):
#     print("the price of the banana is ",dict_shop.get("banana"))
# elif(item=="dal"):
#     print("the price of the dal is ",dict_shop.get("dal"))   
# elif(item=="chawal"):
#     print("the price of the chawal is ",dict_shop.get("chawal")) 
# elif(item=="atta"):
#     print("the price of the atta is ",dict_shop.get("atta"))   
# else:
#     print("Item not available")         
    
    
    
"""Take a list of numbers as input (ask user for 5 numbers one by one using .append()).
Then create a dictionary from it where the number is the key and the value is either "even" or "odd". 
Print the final dictionary."""

# list=[]
# num_1=float(input("enter the 1st number="))
# num_2=float(input("enter the 2nd number="))
# num_3=float(input("enter the 3rd number="))
# num_4=float(input("enter the 4th number="))
# num_5=float(input("enter the 5th number="))
# list.append(num_1)
# list.append(num_2)
# list.append(num_3)
# list.append(num_4)
# list.append(num_5)
# print(list)

# dict={
#     num_1:"even" if num_1%2==0 else "odd",
#     num_2:"even" if num_2%2==0 else "odd",
#     num_3:"even" if num_3%2==0 else "odd",
#     num_4:"even" if num_4%2==0 else "odd",
#     num_5:"even" if num_5%2==0 else "odd"
# }
# print(dict)

"""Take names of students as input and store them in a list. 
Then take their corresponding marks and store them in another list. 
Build a dictionary pairing each student with their marks. 
Finally print the name of the student with the highest mark — 
without using any built-in max() function, use list indexing and if-elif logic only."""

list_name=[]
name_1=(input("enter you name_1="))
name_2=(input("enter you name_2="))
name_3=(input("enter you name_3="))
name_4=(input("enter you name_4="))
list_name.append(name_1)
list_name.append(name_2)
list_name.append(name_3)
list_name.append(name_4)
print(list_name)

list_marks=[]
marks_1=(input("enter you marks_1="))
marks_2=(input("enter you marks_2="))
marks_3=(input("enter you marks_3="))
marks_4=(input("enter you marks_4="))
list_marks.append(marks_1)
list_marks.append(marks_2)
list_marks.append(marks_3)
list_marks.append(marks_4)
print(list_marks)

# if(marks_1>marks_2)and(marks_1>marks_3)and(marks_1>marks_4):
#     print("highest mark is",marks_1,"and the student name is",name_1)
# elif(marks_2>marks_1)and(marks_2>marks_3)and(marks_2>marks_4):
#     print("highest mark is",marks_2,"and the student name is",name_2)
# elif(marks_3>marks_1)and(marks_3>marks_2)and(marks_3>marks_4):
#     print("highest mark is",marks_3,"and the student name is",name_3)    
# else:
#     print("highest mark is",marks_4,"and the student name is",name_4)  
   

dict={
    name_1:marks_1,
    name_2:marks_2,
    name_3:marks_3,
    name_4:marks_4,  
}
print(dict)


if(marks_1>marks_2)and(marks_1>marks_3)and(marks_1>marks_4):
    print("highest mark is",marks_1,"and the student name is",name_1)
elif(marks_2>marks_1)and(marks_2>marks_3)and(marks_2>marks_4):
    print("highest mark is",marks_2,"and the student name is",name_2)
elif(marks_3>marks_1)and(marks_3>marks_2)and(marks_3>marks_4):
    print("highest mark is",marks_3,"and the student name is",name_3)    
else:
    print("highest mark is",marks_4,"and the student name is",name_4)  
   

