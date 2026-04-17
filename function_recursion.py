# block of statement that perform a specific task.
# def function_name(paara1,para2,para3....):
    # what to do 
    # return value.
    
#function_name(arg1,arg2...) these is the command for the function call...


# small example sum of 3 number

# def sum(num1,num2,num3):
#     sum_3=num1+num2+num3
#     return sum_3

# sum(1,2,2) 
# print(sum(1,2,2))

"""we can make a function without parameter
   and if we don't want to return the value that's also okkkk"""
   
# def printhello():
#     print("hello world")

# output=printhello()
# print(output)    
    
    
#calculate the average of 3 number using function...
# def cal_average(num1=9,num2=9,num3=9): #these the value we have passed is default parameter , these default parameter is taken when we don't pass the value below 
#     sum=(num1+num2+num3)
#     average=sum/3
#     return average
# cal_average(55,55,55)
# print(cal_average(55,55,55))

# jab bhi hum defalut set karte hai tho sequence matter karta hai..
# correct way = def cal_product(a,b=1)
# incorrect way = def cal_product(a=1,b)

# practice 
# write a function to print the length of the list.(here list is a parameter)
# cities=["mi","lsg","srh","pbks","csk","rcb","rr","dc","kkr","gt"]
# nums=[5,0,1,0,5,1,1,0,3,1]
# def print_len(list_obj): here we have initialize the function and named the parameter as list_obj.
#     len_list = len(list_obj) these is the main command of finding the length of the object
#     print(len(list_obj)) printing the list of the list
# print_len(cities) calling the function
# print_len(nums)  calling the function



# WAF to print the element of a list in a single line.(list is the parameter here)
# cities=["mi","lsg","srh","pbks","csk","rcb","rr","dc","kkr","gt"]
# def print_list_object(object): # here we have inialize the fuctiona and named it as the print_list_object
#     for item in object: #here we have travers the complete object i.e complete lsit traversal
#         print(item,end=", ")# as for common end is taken as'\n' i.e next line but we change it as space.
        
# print_list_object(cities)   #here we have call the function       

# find the factorial of the number 
# def cal_fact(n):
#     fact=1
#     # i=1
#     for i in range(1,n+1):
#         fact*=i
#         # i+=1
#     print(fact)    
# cal_fact(5)    

# convert usd to indian rupee using function...
# def converter(rupee):
#     rupee_c=rupee*95
#     print(rupee_c)
#     return rupee_c
# (converter(6003*2))    

# WAF to take a number as input if it odd print odd and if the number is even print even.
# def checker(n):
#     if(n%2==0):
#         print("even")
#     else:
#         print("odd")    
# checker(5)        

#1.The Greeting Machine: WAF (Write a Function) that takes a name and time_of_day 
# (e.g., "Morning", "Night") and prints "Good [time_of_day], [name]!".

# def gretting(name,time_of_day):
#     time_of_day=time_of_day.lower()
#     if time_of_day=="morning":
#         print("good",time_of_day,"",name)
#     elif time_of_day=="evening":
#         print("good",time_of_day,"",name)
#     elif time_of_day=="afternoon":
#         print("good",time_of_day,"",name)
#     elif time_of_day=="night":
#         print("good",time_of_day,"",name)
#     else:
#         print("invalid input")
# (gretting("shivam","NIGHT"))        

"""Square Returner: WAF that takes a number and returns its square.
Call the function and print the result."""

# def Square_Returner(n):
#     square=n*n
#     return square
# print(Square_Returner(5))

"""Vowel Counter Function: Take the vowel counting logic you wrote earlier and put 
it inside a function called count_vowels(string). It should return the total count."""
def vowel_Counter(string):
    count=0
    for element in string:
        if element in "aeiou":
            count+=1
    print("the number of vowel in the string is",count)
    
vowel_Counter("shivam_rajesh_pandey_i_want_to_become_ai_engineer")    