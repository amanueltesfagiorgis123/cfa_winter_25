# Note: Exercise 1 of the Practice Session is in the in-class file.

# Exercise 2
# 1. Create a function called mad_libs
# Inside the function: 
# 2. create 3 variables: noun, verb, adjective
# 3. Get the value of the variables from the user, give good instructions!
# 4. Print out the following mad-lib:
#    f"The noun went for a verb but was interrupted by a adjective giraffe."
# 5. Unindent to call the function  

def mad_libs () :
    noun = input("Please enter a noun here : ")
    verb = input("Please enter a verb here : ")
    adjective = input("Pleas enter an ajective here : ")
    print(f"The {noun} went for a {verb} but was interrupted by a {adjective} giraffe.")
mad_libs ()
# Exercise 3
# 1. Create a function called flattering_chatbot
# Inside the function: 
# 2. Print a welcome banner from the chatbot, have it say its name
# 3. Create a variable for name, get the value from the user, ask their name
# 4. Print something like: "name is my favorite name!"
# 5. Create a variable movie, get its value from the user, ask the user's favorite movie
# 6. Print the chatbot saying that its favorite movie too
# 7. Think of 3 more questions to ask the user. After each question, 
# have the chatbot repeat what the user entered and say something flattering about it.
# 8. Unindent to call the function

def flattering_chatbot () :
    print("Hello this is garvis personal assistant")
    name = input("What is your name : ")
    print(f"{name} is my favorite name!")
    movie = input("What is your favorite movie : ")
    print(f"{movie} is my favorite movie too!")
    age = input("What is your age : ")
    print(f"{age} is nice age to be at")
    color = input("What is your favorite color : ") 
    print("{color} same!!!")
    season = input ("What is your favorite season : ")
    print("mine is summer")
flattering_chatbot

# Exercise 4
# Reorganize your code into the proper structure
# 1. Put all the exercise comments at the top
# 2. Put the function definitions next
# 3. Put the function calls at the bottom

## 1. Create a function called mad_libs
# Inside the function: 
# 2. create 3 variables: noun, verb, adjective
# 3. Get the value of the variables from the user, give good instructions!
# 4. Print out the following mad-lib:
#    f"The noun went for a verb but was interrupted by a adjective giraffe."
# 5. Unindent to call the function  

# 1. Create a function called flattering_chatbot
# Inside the function: 
# 2. Print a welcome banner from the chatbot, have it say its name
# 3. Create a variable for name, get the value from the user, ask their name
# 4. Print something like: "name is my favorite name!"
# 5. Create a variable movie, get its value from the user, ask the user's favorite movie
# 6. Print the chatbot saying that its favorite movie too
# 7. Think of 3 more questions to ask the user. After each question, 
# have the chatbot repeat what the user entered and say something flattering about it.
# 8. Unindent to call the function
fun = input("What do like to do for fun? : ")
def mad_libs () :
    noun = input("Please enter a noun here : ")
    verb = input("Please enter a verb here : ")
    adjective = input("Pleas enter an ajective here : ")
    print(f"The {noun} went for a {verb} but was interrupted by a {adjective} giraffe.")
def flattering_chatbot () :
     print("Hello this is garvis personal assistant")
     name = input("What is your name : ")
     print(f"{name} is my favorite name!")
     movie = input("What is your favorite movie : ")
     print(f"{movie} is my favorite movie too!")
     age = input("What is your age : ")
     print(f"{age} is nice age to be at")
     color = input("What is your favorite color : ") 
     print("{color} same!!!")
     season = input ("What is your favorite season : ")
     print("mine is summer")
def ask() : 
    print(f"{fun} that is my favorite too!!! ")
mad_libs () 
flattering_chatbot ()
ask () 
# Exercise 5
# 1. Create a global variable and get its value from the user
# You can ask anything you want
# 2. Display the answer by adding the variable into one of the print statements inside one of the functions
fun = input("What do like to do for fun? : ")
def ask() : 
    print(f"{fun} that is my favorite too!!! ")
ask()