""" loops are used to repeat instructions.
{their are two types of loops in python that are for loops and while loops}"""

"""whlie loop syntax
     while condition:
        work to do{until the condition is true}"""
        
# print hello world 5 times
# print("hello")
# print("hello") 
# print("hello") 
# print("hello")  
# print("hello") 
# these method can work for less times but when number of times increases these will not work 

# # now using while loop for the same question 
# i=0
# while i<=4:
#     print("hello world")
#     i+=1    
    
# print the number from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1 

# print number from 100 to 1 
# i=100
# while i>=1:
#     print(i)
#     i-=1   
    
    
# print the multiplication of the  number n.
# n=float(input("enter the number you want the multiplication="))
# i=1
# while i<=10:
#     print(i*n)
#     i+=1
    
#print the elements of the following list using a loop
# nums=[1,4,9,16,25,36,49,64,81,100] 
# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1
    
# search the number x give it's index , take x as input from the user
# nums=[1,4,9,16,25,36,49,64,81,100]
# x=int(input("enter the number you have to search= "))

# idx=0
# while idx<len(nums):
#     if(nums[idx]==x):
#         print("x  is found at index",idx)
#         break # used to terminate the loop when encountered...
#     idx+=1
# else:
#         # idx+=1
#         print("x is not found") 
    
#  continue {terminates executionin the current iteration and continues execution of the loop with next iiteration}

# print only odd number between 1 to 100

# i=1
# while i<=100:
#     if(i%2==0):
#         i+=1
#         # continue
#     print(i)
#     i+=1

# print only odd number between 1 to 100.

# i=1
# while(i<=100):
#     if(i%2!=0):
#         i+=1
#         continue
#     print(i)   
#     i+=1 

# print all the odd nums from 1 to 10 

# i=1
# while i<=100:
#         if(i%2!=0):
#                 i+=1
#                 continue
#         print(i)
#         i+=1
# print("out side the loop")        

#
# nums=(1,2,3,4,5,6,7,8,9,10)
# x=int(input("enter the number you want to find=")) 
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("found the number",x,"at the index",i)
#         break
#         i+=1        
#     else:
#         i+=1      
        
        
"""now learning for loop syntax {for element in list:
                                 #some work 
for loops are used for sequential traversal . for traversing list, string tuple etc.}"""  
# list=[1,2,3,5,55,5,5,8522,85652,5821]   
# for element in list:
#         if(element==3):
#                 print("we got the number we want")
#                 # break
#         print("elements of the list",element) 

# search for a number x in this tuple using loops     
tup=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("enter the number you want to find="))
# i=0
# while i<=len(tup):
#    if(x==tup[i]):
#        print("we got the number",x,"at the index",i)
#        break
#    else:
#         i+=1        
                       
                       
"""range in python,range functions return a sequence of numbers starting from 0 by default , 
and increments by 1 by default and stop before a specified number."""
# range(start,stop,step) stop is compulsory and other 2 are by defalut 1 if not given
# here the stop number is not included....
# even number from the 1 to 100 (1 and 100 is included)
# for i in range (2,101,2):
#         print(i)

# enter the number from 100 to 1 . include 100 and 1
# for i in range (100,0,-1):
#         print(i)

# find the multiplication table of the number taken from the user.
# n=float(input("enter the number for which you want to calculate table="))
# for i in range (1,11,1):
#         print(i*n)
        
# wap to find the sum of first n natural number , n will be taken from the user using while loop        
# n=int(input("enter the number for which you have to find sum of natural number="))
# sum=0
# i=0
# while i<=n:
#    sum+=i
#    i+=1
        
# print("total sum of the natural number",n,"is",sum)   

# find the factorial of the number taken from the user.
# n=int(input("enter the number for which you have to find factorial="))
# fact=1
# i=1
# while i<=n:
#     fact=fact*i
#     i+=1
# print("the factorial of the number",n,"is",fact)    


# now doing the same problem from the 2nd method 

# n=int(input("enter the number for which you have to find factorial="))
# fact=1
# for i in range (1,n+1,1):
#         fact*=i
        
# print("the factorial of the number",n,"is",fact)         


""" The Step Counter: Print all numbers from 1 to 50, but for every number,
 also print its square next to it (e.g., 1 - 1, 2 - 4, 3 - 9)."""
# i=1
# while i<=50:
#         print("The number is",i,"and the square of the same number is",i*i)
#         i+=1
        
"""The Vowel Counter (Loop Edition): Take a string input and use a for loop to count how many 
total vowels{a,e,i,o,u,s} are in it. (Don't use .count(), iterate through the string instead!)."""        

# user_input=input("enter the sentence for which you have count the string=").lower()
# count=0
# for elements in user_input:
#         if(elements=="a"):
#             count+=1
#         elif(elements=="e"):
#             count+=1
#         elif(elements=="i"):
#             count+=1
#         elif(elements=="o"):
#             count+=1
#         elif(elements=="u"):
#             count+=1
  
# print("the total number of the vowels are",count)            


# # method 2
# user_input=input("enter the sentence for which you have count the string=").lower()
# count=0
# for elements in user_input:
#     if elements in "aeiou":
#         count+=1
# print("the number of vowel from the user_input is",count)        
    
    
"""Sum of Evens: Ask the user for a number $n$. 
Calculate the sum of all even numbers from 1 to $n$ using a while loop.""" 

# user_input=float(input("enter the number till which you have to calculate sum of even="))
# i=0
# sum_even=0
# while i<=user_input:
#     if(i%2==0):
#         sum_even+=i
#     i+=1
        
# print(sum_even)


"""The Multiplier Table Grid: Ask the user for a number. 
Print the multiplication table for that number, but format it like this: 5 x 1 = 5"""

# n=float(input("enter the number fo which you have to find table="))
# i=1
# while i<=10:
#     print
#     print(n,"*",i,"=",n*i)
#     i+=1 
    
"""List Filter: Given the list nums = [12, 45, 7, 80, 22, 3, 59, 10], 
create a new list called large_nums that only contains numbers greater than 30 using a loop."""

# nums = [12, 45, 7, 80, 22, 3, 59, 10]
# nums_30=[]
# i=0
# while i<=len(nums)-1:
#     if(nums[i]>30):
#         nums_30.append(nums[i])
#     i+=1    
    
# print(nums_30)

"""The Reverse Countdown: Using range(), print a countdown from 100 to 1, 
but only print numbers that are divisible by 5."""

# for i in range(100,0,-1):
#     if(i%5==0):
#         print(i)
        
"""Password Guessing Game: Set a "secret password" variable. 
Use a while loop to keep asking the user to enter the password. 
If they get it wrong, say "Try again." If they get it right, say "Access Granted" and break the loop."""        
  
# secret_password="shivam123"
# user_input=input("enter the secret password=")
# while True:
#     if(user_input==secret_password):
#         print("YOU GOT THE CORRECT PASSWORD!! Access Granted")
#         break   
#     else:
#         user_input=input("TRY AGAIN=")
        
"""Pattern Printing: Use nested loops to print the following pattern based on a number $n$ (if $n=4$):
Plaintext
*
**
***
****"""
# number=int(input("enter the number for which we have to create plain star text="))
# i = 1
# while i <= number:
#     print("*" * i)
#     i += 1
# # now same pattern with the inverted 
# number=int(input("enter the number for which we have to create inverted plain star text="))
# i=number
# while i >= 1:
#     print("*"*i)
#     i-=1
 


"""Prime Number Checker: Take a number input from the user and 
determine if it is a Prime Number (a number divisible only by 1 and itself) using a loop."""
# n=int(input("enter the number you want to check if it is a prime number or not="))
# if(n%n==0 and n%1==0):
#     print("it is a prime number")
# else:
#     print("it is not a prime number")    