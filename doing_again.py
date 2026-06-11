# # Basic operation on string 
# # 1st concatenation (adding strings together)

# str1="shivam"
# str2=" pandey"
# print(str1+str2)

# 2nd length of string syntax === len(string)   [ismai space ke bhi length hota hai ]
# name="Apna_college is the place from where i study"
# print(len(name))

# indexing in string.... the indexing starts form 0. (we can read character and word in string but cannot replace character.)
# name="Apna_college is the place from where i study"
# print(name[2])

 # slicing in string syntax === str[starting_idx:ending_idx]  in these slicing last idx is not included..
# name="Apna_college is the place from where i study"
# print(name[1:4])# last index is not included

# 1st str.endswith("")   here in these it gives true or false check if the string is end with the given word or not...
# name="Apna_college is the place from where i study"
# print(name.endswith("dy"))

# 2nd str.capitalize()   in these  function the string made to be start from the capital letter, but it does not effect the usual string
# name="apna_college is the place from where i study"
# print(name.capitalize())


# # 3rd str.repalce(old,new) repalce all the occurrences of old...
# name="apna_college is the place from where i study"
# print(name.replace("college","ghar"))


# 4th str.find("word")  return 1st index of the first occurence of the word..
# name="apna_college is the place from where i study"
# print(name.find("e"))

# 5th str.count("") count the occurence of substring
# name="apna_college is the place from where i study"
# print(name.count("a"))


# take input as a name and print it's length...
# name=input("enter you name=")
# print(len(name))

# find the number of ouccurence of $ in the sentence  

# str="my name is $ , and i love $ and i want lots of $"
# print(str.count("$"))

# first we will be going for the if-elif-else
# traffic light code 
# input_light=input("enter the traffic light colour=")
# if input_light=="green":
#     print("you can go")
# elif input_light=="yellow":
#     print("first see , then go")
# elif input_light=="red":
#     print("don't go")
# else:
#     print("light is broken")        \
    
# # Grades of student...

# grades=float(input("enter your grades="))
# if grades>=90:
#     print("you got A+")
# elif 90>grades>=80:
#     print("you got A")
# elif 80>grades>=70:
#     print("you got B+")
# elif 70>grades>=60:
#     print("You got C")    
# else:
#     print("you got D or lower")
       
# Take the user's name and age as input, then print: Hello [name], you will be [age+10] years old after 10 years.    
# name=input("enter your name=")
# age=float(input("enter your age "))
# print("hello",name,"you will be",age+10, "years after 10 years")

# Take a string as input and print its length, the first character, the last character, and the string in reverse using slicing.
# name=input("enter your name=")
# print(len(name))
# print(name[0])
# print(name[len(name)-1])

# Take a sentence as input and print how many vowels (a, e, i, o, u) are in it. Use string methods you've learned.

# string=input("enter the sentence=").lower()
# count_a=string.count("a")
# count_e=string.count("e")
# count_i=string.count("i")
# count_o=string.count("o")
# count_u=string.count("u")
# print("the number of a in string",count_a)
# print("the number of e in string",count_e)
# print("the number of i in string",count_i)
# print("the number of o in string",count_o)
# print("the number of u in string",count_u)

# wap to ask the user to enter the name of their three fav movie..
# movie=[]
# name_1=input("enter the  name of the movie_1:")
# name_2=input("enter the  name of the movie_2:")
# name_3=input("enter the  name of the movie_3:")
# movie.append(name_1)
# movie.append(name_2)
# movie.append(name_3)
# print(movie)
# print(type(movie))

# check the given list is palindrome or not... taking list as a input
# phele jo list banaya tha wahi use kar liya...
# movie=[]
# name_1=input("enter the  name of the movie_1:")
# name_2=input("enter the  name of the movie_2:")
# name_3=input("enter the  name of the movie_3:")
# movie.append(name_1)
# movie.append(name_2)
# movie.append(name_3)
# print(movie)
# copy_movie=movie.copy()
# copy_movie.reverse()
# if copy_movie==movie:
#     print("it's palindrome")
# else:
#     print("it's not a palindrome")    
    
# wap to count the number of student's with the "A" grade in the following tuple    
# list=["A","A","B","C","D","F","A","D","A"]
# count_A=list.count("A")
# print(count_A)

"""wap to enter to enter marks of 3 subjects from the user and store them in a dictionary start with an 
empty dictionary and add one by one use subject name as a key and marks as a value.."""
# dict_marks={}
# marks_1=float(input("enter the marks of 1st sub:"))
# marks_2=float(input("enter the marks of 2nd sub:"))
# marks_3=float(input("enter the marks of 3rd sub:"))
# dict_marks.update({"sub1":marks_1})
# dict_marks.update({"sub2":marks_2})
# dict_marks.update({"sub3":marks_3})
# print(dict_marks)

"""Create a dictionary storing your own details — name, age, city, 
and a list of your 3 hobbies. Print each value using its key."""
# dict={
#     "name":"shivam",
#     "age":"21",
#     "city":"mumbai",
#     "list_hobby":{
#         "hobby1":"sports",
#         "hobby2":"watching TV",
#         "hobby3":"coding" 
#     }
    
# }
# print(dict.get("name"))
# print(dict.get("age"))
# print(dict.get("city"))
# print(dict.get("list_hobby"))
# print(dict)


# """You are given this list [4, 2, 7, 1, 9, 3] — sort it in ascending order, then reverse it, 
# then remove the last element using .pop(). Print the list after each step."""
# list=[4, 2, 7, 1, 9, 3]
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# print(list)