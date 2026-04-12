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

i=1
while i<=100:
    if(i%2==0):
        i+=1
        # continue
    print(i)
    i+=1

# print only odd number between 1 to 100.

# i=1
# while(i<=100):
#     if(i%2!=0):
#         i+=1
#         continue
#     print(i)   
#     i+=1 