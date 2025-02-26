# Exercise 1
# 1. Create a function called about_you with 2 parameters, name, age
# Inside the function 
#  2. Print "Your name is " and concatenate the name
#  3. Print "You are" concatenate age "years old."
#  4. Call the function and send it a string argument for name, 
#  and an integer argument for age.
from datetime import date


def about_you(name , age) :
    print(f"Your name is : {name}")
    print(f"Your are : {age}")
about_you("Amanuel" , 12)



# Exercise 2
# 1. Create a function called table with 1 parameter: num
# Inside the function
#  2. Create a variable called results
#  3. Set its value to a multiline F string. Create a multiplication table, 
#  4. multiply num times the numbers 1-10, showing each calculation on a new line
#  5. for example: {num} x 1 = num*1
#  6. Print results
#  7. Call the function and send it an integer argument.
#  8. Get a number from the user, and convert it to an int. Call the function using the user's number
def table(num) :
    results = (f'''
    {num} * 2 = {num * 2}
    {num} * 3 = {num * 3}
    {num} * 4 = {num * 4}
    {num} * 5 = {num * 5}
    {num} * 6 = {num * 6}
    {num} * 7 = {num * 7}
    {num} * 8 = {num * 8}
    {num} * 9 = {num * 9} 
    {num} * 10 = {num * 10}''')
    print(results)
user_num = int(input("Enter the number for multiplication table :"))
table=(user_num)


  

# Exercise 3
# 1. Get 3 responses from the user:
# What was the last thing ate?
# What is the color of your pants?
# What was the last thing you bought?
# 2. Create a function called band_name with 3 parameters.
# Inside the function:
# 3. Print "Your bandname is..." using all 3 parameters
# 3. Call the function and send it the variables containing the user's 3 responses.
last_ate = input ("What was the last thing you ate ? : ")
pants_color = input ("What is the color of your pants? : ")
last_bought = input(" What was the last thing you bought? : ")
def ban_name (name , color , bought) :
    print = (f"Your brand name is: {last_ate} {color} {bought}")
band_name = (last_ate , pants_color , last_bought)

    



# Advanced students 
# Exercise 1 Use a keyword argument for age, call the function without a value for age.
# Exercise 2 Use a loop with one of line code inside it to produce the multiplication table.
# Exercise 3 Inside the function, use random to mix up the order of the parameters.