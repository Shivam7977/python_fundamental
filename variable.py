# # #  
# name="shivam"
# age=23
# print("my name is=",name,"and age is=",age)
# num1=123
# num2=9823
# sum=num1+num2
# print("sum of 2 number is",sum)
# let_a=None
# print(type(name))
# print(type(age))
# print(type(let_a))

# a=8 #it is integer
# b="6"# it is string
# multiple=a*b
# print(multiple)

# division operator
# import math
# b,a=6,4
# c=b//a # integer division, these can be also done using floor
# hello=math.floor(c)
# print(c)
# print("floor wala answer =",hello)

# a,b=7,6
# c=a/b # normal division
# print(c) 

 
# # now taking input from user 
# num1=int(input("num1 is = "))
# num2=int(input("num2 is 5= "))
# print("sum=",num1+num2)

# # some logical question.
# hello=not True and False or True
# print(hello)

# some if-else question.
# voting senerio
# age=int(input("what is your age="))
# if(age>=18):
#     print("you can vote")
# elif(age<18):
    # print("can not vote as you are under age")    
    
# # traffic light senerio
# light=input("what is the curret traffic light=") 
# if(light=="green"):
#     print("vehicles can move")   
# elif(light=="yellow"):
#     print("before moving look")    
# elif(light=="red"):
#     print("vehicles can not move")
# else:
#     print("ligth is broken")

# # student's marks senerio
# marks=int(input("what is your marks="))
# if(marks>=90):
#     print("grade is A")
# elif(90>marks>=80):
#     print("grade is B")   
# elif(80>marks>=60):
#     print("grade is C")   
# elif(60>marks>=40):
#     print("grade is D")  
# else:
#     print("grade is E")      

# # calculate simple interest
# P=float(input("principle amount="))
# R=float(input("rate of interest="))
# T=float(input("tennure of the investment="))
# Simple_Interset=(P*R*T)/100
# print(Simple_Interset)

#1. he Currency Converter Ask the user for an amount in USD (Dollars). Convert it to INR (Rupees).

# Hint: Assume 1 USD = 84 INR.

# Goal: Practice float() input and multiplication *.
# how_dollar=float(input("enter the amount of dollar="))
# in_rupee=how_dollar*84
# print("the amount the dollar in rupees is=", in_rupee)

# The Repeater Ask the user for their name and a number (e.g., "5"). Print their name that many times.
# name=input("what is name=")
# repeat_time=int(input("how many time you want to repeayt the name="))
# ans=name*repeat_time
# print(ans)

# . Odd or Even Checker Ask for a number. If the number is even, print "Even"; otherwise, print "Odd"
# number=int(input("enter the number="))
# if(number%2==0):
#     print("number is even")
# else:
#     print("number is odd")    


# make fake login system

# user_name=input("create your user_name=")
# password=input("create your password=")


# check_user=input("enter your user_name=")
# check_pass=input("enter your password=")

# if(user_name==check_user and password==check_pass):
#     print("login succesfully")
# elif(user_name!=check_user and password==check_pass):
#     print("check your user_name")   
# elif(user_name==check_user and password!=check_pass):
#     print("check your password")
# else:
#     print("check your user_name and password")

# validate the triangle is correct or not
# Try_A=float(input("enter the angle A="))
# Try_B=float(input("enter the angle B="))
# Try_C=float(input("enter the angle C="))
# if(Try_A+Try_B+Try_C==180):
#     print("the triangle is valid")
# else:
#     print("the triangle is invalid")    
#The Shopping Discount Ask the user for their "Total Purchase Amount".

# If the amount is greater than 1000, give a 10% discount.
# If the amount is greater than 500 (but less than 1000), give a 5% discount.
# Otherwise, no discount# Print: The final price they have to pay.

# amount=float(input("Enter the amount you have did shopping="))
# if(amount>=1000):
#     print("you got the discount 10% , so you have to pay",amount*0.90)
# elif(1000>amount>=500):
#     print("you got the discount of 5% , so you have to pay=", amount*0.95)
# else:
#     print("No discount, so you ahve to pay=",amount)        

# The "Greatest of Three" Ask the user for three distinct numbers: num1, num2, and num3.

# Use logical operators (and) to find which number is the biggest.

# Example Logic: if num1 > num2 and num1 > num3: ...

# num1=float(input("enter num1="))
# num2=float(input("enter num2="))
# num3=float(input("enter num3="))
# if(num1>num2 and num1>num3):
#     print("num1 is greater")
# elif(num2>num1 and num2>num3):
#     print("num2 is greater")  
# else:
#     print("num3 is greater")      
            
            
# stone paper scissors game  
# --- ROCK, PAPER, SCISSORS GAME ---

# 1. Get the user's choice
# Hint: Use input(). converting to .lower() helps match cases like "rock" vs "Rock"
# user_choice = input("Enter Rock, Paper, or Scissors: ")

import random  # Import the random module

# 1. The List of options
options = ["Rock", "Paper", "Scissors"]

# Get the user's choice
user_choice = input("Enter Rock, Paper, or Scissors: ").strip().capitalize()

# 2. The Computer chooses randomly! (The magic line)
computer_choice = random.choice(options) 

print("Computer chose:", computer_choice)

# Now, your logic below makes perfect sense because 
# we genuinely don't know what the computer picked!

# 3. The Logic: Who wins?
# Scenario 1: It's a Tie
if user_choice == computer_choice:
    print("It's a tie!")

# Scenario 2: User chose Rock
elif user_choice == "Rock":
    if computer_choice == "Scissors":
        print("You Win! Rock smashes Scissors.")
    else:
        print("You Lose! Paper covers Rock.")

# Scenario 3: User chose Paper
elif user_choice == "Paper":
    if computer_choice == "Scissors":
        print("You loss! Scissors cut the paper.")
    else:
        print("You Win! Rock break the Scissors")
        


# Scenario 4: User chose Scissors
elif user_choice == "Scissors":
    if computer_choice == "Rock":
        print("You Loss! Rock breaks the Scissors.")
    else:
        print("You Win!Scissors cut teh paper.")  
    pass

else:
    print("Invalid input! Please check your spelling.") 