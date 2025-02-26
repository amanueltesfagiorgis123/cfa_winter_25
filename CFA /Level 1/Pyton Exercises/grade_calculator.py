# Exercise 1: Plans with friends depend upon the weather
# 1. Get the temperature from the user and convert to an int
# 2. Create a variable called precipitation, and set its value to True or False
# 3. Create a conditional statement with the following plans:
#  If it's warmer than 50 degrees and it's not raining, you'll go hiking.
#  If it's cold but not raining, you'll walk to the coffee shop.
#  If it is raining, you'll play video games. 
# 4. Print your plans for the day.
temperature = int(input("What is the temperature : "))
precipitation = True or False 
if temperature >50 and "it's not raining" :
    print("You will go walking")
elif temperature <= 50 and "not raining" :
    print("you will walk to the coffee shop")
else:
    print("you will play video games")


  

# Exercise 2: Converting a percentage grade to a letter grade
# 1. Get a grade percentage from the user and convert it an int. 
# 2. Create an if statement that converts the grade percentage to a letter grade based on the scale below:
#
# 94 and up     : A
# 90 to 93      : A-
# 87 to 89      : B+
# 83 to 86      : B
# 80 to 82      : B-
# 77 to 79      : C+
# 73 to 76      : C
# 70 to 72      : C-
# 67 to 69      : D+
# 60 to 66      : D
# Less than 60  : F
#
# Chain as many elif statements as you need.
# 3. After the conditional statement, use a single print statement to show the person's letter grade, concatenated with a string like: "You got a ___ in this class!" 

percentage_grade = int(input("What is your percentage grade : "))
if percentage_grade >= 94 :
    print("A")
elif percentage_grade >= 90 :
    print("A-")
elif percentage_grade >= 87 :
    print("B+")
elif percentage_grade >= 83 :
    print("B")
elif percentage_grade >= 80 :
    letter_grade = "B-"
elif percentage_grade >= 77 :
    letter_grade = "C+"
elif percentage_grade >= 73 :
    letter_grade = "C"
elif percentage_grade >= 70 :
    letter_grade = "C-"
elif percentage_grade >= 67 :
    letter_grade = "D+"
elif percentage_grade >= 60 :
    letter_grade= "D"
else :
    letter_grade = "F"





# Exercise 3 Login a user to your social media app
# 1. Create a variable valid_username and set its value to a string
# 2. Create a variables valid_password and set its value to a string
# 3. Print a welcome banner for your app
# 4. Get a username from the user
# 5. Get a password from the user
# 6. Create a conditional statement checking to see if the user entered the correct uesername and password. If they got both username and password correct, log them into your app. 
# If the user did not type anything, tell them they must enter the data.
# If they got the username wrong, tell them and ask them to try again.
# If they got the password wrong, tell them and ask them to try again.
# 7. Thoroughly test all conditions to make sure everything works!



valid_username = "numberoneuser"
valid_password = "thisispassword"
print("WELCOME!!!")
username = input("What is your user name : ")
password = input("What is your password : ")
if not username or not password:
    print("must enter data")
elif not username :
    print("try again")
elif not password :
    print("try again")
else :
    print("✅")

# Advanced students
# Create a guess the number game.
# Use the randint() function from the Python random module, like this:
# from random import randint
# random_num = randint(1, 20) 
# 1. Have Python pick a random number between 1 and 20
# 2. The user wins $100 if they get the number right
# 3. The user wins $50 if their guess is close, within 2 numbers of Python's choice, 
# 4. Else they lose. 
# 5. Tell the user what the random number was.   