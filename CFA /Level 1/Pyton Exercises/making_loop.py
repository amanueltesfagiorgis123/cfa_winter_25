# from random import randint

# Exercise 1 Refactor the multiplication table code with a for loop
# 1. Create a variable: num , set its value to integer of your choice  
# 2. Create a for loop with iteration variable c and 
#    range function for numbers 1 through 10
# 3. Inside the for loop, print an f string showing 
#    the calculation of num times the iteration variable and its result
# 4. Give num a new value and test again

num = 7 

for c in range (1,11):
    print(f"{num} * {c} = {num * c}")

num = 8 

for c in range (1,11):
    print(f"{num} * {c} = {num * c}")

# Exercise 2 
# 1. Put the multiplication for loop you created in Exercise 1 inside a function with 1 parameter
# 2. Get a number to be multiplied from the user 
# 3. Call the function and pass it the user's number

def multiplication_table(num):
    for c in range (1,11):
        print(f"{num} * {c} = {num * c}")

user_num = int(input("Input your int here : "))
multiplication_table(user_num)
     
# Exercise 3: Christmas tree lot  
# 1. Ask the user how tall they want their tree, convert it to an integer and save it in a variable.
# 2. Edit the tree code to make the tree as many lines tall as the customer ordered.
# 3. Don't forget to adjust the trunk. Hint: the value of the user's height ends at 0, so you must use leaf instead. 
# Remember to check for the data type of any calculation output, and use type conversion.

tree_h = int(input("How tall you want your tree : "))

for i in range (tree_h):
    space = tree_h - i - 1 
    leaf = 2 * i + 1 
    print("" * space + "*" * leaf)

trunk_spaces = tree_h - 1
print("" * trunk_spaces + "l")


# Exercise 4: Make an upside down tree
# 1. Copy, paste, and edit the loop that makes the tree so it appears upside down.
# 2. Don't forget the trunk

tree_h = int(input("Enter tree height:"))

for i in range (tree_h, 0, -1):
    spaces = tree_h - i 
    leaves = 2 * i -1 
    print("" * spaces + "*" * leaves)

trunk_spaces = tree_h - 1 
print(" " * trunk_spaces + "*")

# Exercise: Create a slot machine game.
# Each player gets 5 rounds to get a jackpot
# 1. Create a variable for total rounds.
# 2. Create a variable to keep score
# 3. Create a variable for rounds played
# 3. Create a while loop that runs until the rounds are over
# 4. Inside the loop,
#   Ask the user if they wish to keep playing, if true: 
#   Generate 3 random numbers between 1 and 7
#   Create a conditional statement that checks for:
#    jackpot (all 3 match)
#    double ( 2 match)
#    loss (no matches)
#   Print the slots and result of each round
# 6. Outside the loop, print the results of all 5 rounds

print("🎰SLOT MECHINE GAME🎰")
import random 
total_rounds = 5
keep_score = 0 
rounds_played = 0 

while rounds_played < total_rounds:
    play = input ("Do you want to spin the slot machine? (yes/no): ").strip() .lower()

    if play == "yes" : 
        rounds_played += 1

        slot1 = random.randint(1,7)
        slot2 = random.randint(1,7)
        slot3 = random.randint(1,7)

        print(f"Round {rounds_played}:[{slot1}] [{slot2}] [{slot3}]")

        if slot1 == slot2 == slot3:
            print("JACKPOT! YOU WON 10 POINTS 🚨")
            keep_score += 10
        elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
            print("DOUBLE MATCH! YOU WON 5 POINTS 🥈")
            keep_score += 5
        else :
            print("NO MATCH ! 😔")
        
    elif play == "no":
        print("GAME OVER!")
        break 
    else:
        print("Invalid input. Please enter 'yes' or 'no' . ")

print("\n GAME OVER")
print(f"Total rounds played: {rounds_played} ")
print(f"Final Score: {keep_score} points")


