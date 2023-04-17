## Getting information from the user and converting strings and numbers

## What is the keyword used to get information from the user?
name = input("enter your name")

## The following code will break Python because there's no __________ to receive the input. (1 word)

input("Enter your first name: ")

## variable 

## Complete the code. The prompt is "Name: "

user_name = input("Name: ")

## Ask for the user's name and store the answer in user_name. The prompt is "Name: ". Don't forget to add the space after Name:
 
user_name = input("Name: ")


## Code an input statement. Make up the variable name and the prompt.

total = input("how much am i")

##  Code an input statement. Make up the variable name and the prompt. Then display the user's answer.

team = input("enter team name: ")
print(team)

## In a single line of code convert a number to a string and assign it to a variable. Make up the number and the variable name.

age = input("Enter age")
print(str(age))

## Convert a string to an integer and assign it to a variable. Make up the string and the variable name.

gpa = input(int("what is your grade point average"))

## Convert a string to a float and assign it to a variable. Make up the string and the variable name.

gpa = float("3.9")

## On line 1 ask the user for a number. On line 2 convert it to a float. On line 3 add the float to another number and assign the sum to a variable. Make everything up.
a = 1

any_num = input("give me a number please")
float_num = float(any_num)
total = float_num + 1

## Get the user's age.
## Python interprets the user's input as a string even if it's a number, so convert the response to an integer.
## Add 1 to the integer.
## Convert the sum to a string.
## Display Next year you'll be plus next year's age.

user_age = input("what is your age? ")
int_age = int(user_age)
plus_age = int_age + 1
print(plus_age)
str_age = plus_age
print(f"you will be {str_age} years old in 1 year")
