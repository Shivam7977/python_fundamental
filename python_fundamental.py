print("hello world\nAre you all okay.")
print("hello world","Are you all okay.")
shivam="opuuhfdw"
_shivam=69
print(_shivam)
print(shivam)

num_1=4
num_2=5
sum=num_1+num_2
print(sum)
print(num_1+num_2)


name="shivam"
age=20
print("my name is",name,"and my age is",age)

# # finding data type in pyhton.
# # syntax = print(type(variable_name))
print(type(name))
print(type(age))

# expresssion execution
# 1st string and numeric ka multiplication. answer will be string ko utne baar likha do jisse multiply karo....
string="@"
answer=2*string
print(answer)

# 2nd string and string can operate with +
A,B="2",3
text="@"
print((A+text)*B)


# some arthemetic division

# 1st normal like a/b answer will be in float data type....
a,b=1,2
c=a/b
print(c)

# 2nd integer division and floor division like a//b and floor(a/b) it take to the closest integer less than that of the actual answer
import math
a,b=5,2
c=a//b
d=math.floor(a/b)
print(c)
print(d)

# taking input from the user....
# 1st normalyy for the string 
name = input("what is your name=")
print("your name is",name ,",just recheck it.")

# # 2nd now for the integer 
age=int(input("what is your age="))
print("your age is",age,".")

# 3rd now for the float 
price=float(input("enter the price of the product="))
print("the price of the product is",price)

# types of operator and their precedence...
""" 1st Arithemetic operator... it's precedence 
() → Parentheses
** → Exponentiation (power)
*, /, //, % → Multiplication, Division, Floor Division, Modulus (if these all comes in the same question, Evaluated left to right)
+, - → Addition, Subtraction"""
a,b=5,2
print("sum=",a+b)
print("minus=",a-b)
print("multiplication=",a*b)
print("division=",a/b)
print("floor division=",a//b)
print("modular=",a%b)
print("power=",a**b)



# relational/ comparision operators.. precedense (==,!=,>,<,>=,<=) always answer as true and flase i.e boolen..
a,b=50,50

equality=a==b
print(equality)

not_equal_to=a!=b
print(not_equal_to)

greater_than=a>b
print(greater_than)

less_than=a<b
print(less_than)

greater_than_equal_to=a>=b
print(greater_than_equal_to)

less_than_equal_to=a<=b
print(less_than_equal_to)


# Assignment operator (=,+=,-=,*=,/=,%=,**=)

num=10
num+=10
print(num)

num=10
num-=10
print(num)

num=10
num*=10
print(num)

num=10
num/=10
print(num)

num=10
num%=10
print(num)

num=10
num**=10
print(num)

# logical operator (not, and , or)   (or, and work on 2 operand) (not work on singel operand)


# answer=(not True) and False or True
# print(answer)

#Type casting

a,b=1,"2"
c=int(b)
sum=a+c
print(sum)
print(type(c))
print(type(b))


a=1
b="5"
print(type(a))
print(type(b))
c=int(b)
print(type(c))


# some example 
# area of square having sides1 and side2
side1=float(input("enter the side1="))
side2=float(input("enter the side2="))
print("the area of square=",side1*side2)

# average of 2 floating number.
num1=float(input("enter the num1="))
num2=float(input("enter the num2="))
average=(num1+num2)/2
print(average)

# 2 integer , give true if greater and false if smaller..
num1=int(input("enter the num1="))
num2=int(input("enter the num2="))
print(num1>=num2)

# string and conditional statement.....

# for going on next line we use \n and for the gap of 4 that is tab we use \t...

str="this is a string.\nwe are creating it in the python" #use \n for the string.
print(str)

str="this is a string.\twe are creating it in the python" #use \t for the string.
print(str)

str="this is a string. \n \twe are creating it in the python" #use \n and \t both for the string.
print(str)

# Basic operation on string 
# 1st concatenation (adding strings together)

str1="shivam"
str2=" pandey"
print(str1+str2)

# 2nd length of string syntax === len(string)   [ismai space ke bhi length hota hai ]

print(len(str1))
print(len(str2))
print(len(str1+str2))

# indexing in string.... the indexing starts form 0. (we can read character and word in string but cannot replace character.)

str="shivam_pandey"
ch=str[2]
print(ch)


# slicing in string syntax == str[starting_idx:ending_idx]  in these slicing last idx is not included..

str="Apna_college"
hello=str[0:4]
print(hello)


# function in string
# 1st str.endswith("")   here in these it gives true or false check if the string is end with the given word or not...
string = "I am studing python form the apna college."
print(string.endswith("kuewf"))
print(string.endswith("ege"))

# 2nd str.capitalize()   in these  function the string made to be start from the capital letter, but it does not effect the usual string
string = "i am studing python form the apna college."
print(string.capitalize())

# 3rd str.repalce(old,new) repalce all the occurrences of old...
string = "I am studing python form the apna college"
print(string.replace("a","b"))
print(string.replace("aa","bb"))

# 4th str.find("word")  return 1st index of the first occurence of the word..
string = "I am studing python form the apna college"
print(string.find("python")) 

# 5th str.count("") count the occurence of substring
string = "I am studing python form the apna college"
print(string.count("pa"))


# few example
# take input as a name and print it's length...

name=input("enter your name =")
print(len(name))

# find the number of ouccurence of $ in the sentence 
string="the sign of the dollar is $ and these $ sign is print on the US currency."
print(string.count("$"))


#conditional statement ...