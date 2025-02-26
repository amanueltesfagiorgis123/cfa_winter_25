from scavenger import hunt

# Exercise 1
# You and your friends are going on a scavenger hunt. 
# In the hunt dictionary is a list of items their locations.
# Found items
# 1. Import the hunt dictionary from scavenger.py
# 2. Print a sentence like: "The following items were found"
# 2. Find the following 3 items and print where you found them:
#    cloisonne vase, orange tabby, horse figurine
#    Concatenate with a sentence like: The _____ was found _____
# 3. The diary was not found where originally listed, correct its hiding place
# and then print it out
# Items not found
# 4. Print a sentence such as: "Here are the items we did not find."
# 5. Remove the found items from the hunt dictionary. Use a for loop to print out the keys and values,
# concatenate with a sentence like: The _____ was hiding _____
# HINT: print \n to tidy up the output
print("The following items were found : ")

items_to_find = ("cloisonne vase", "orange tabby", "horse figurine")

for item in items_to_find:
    print(f"The {item} was found in {hunt[item]}." )

hunt["diary"] = "under the bookshelf"
print(f"The dairy was found {hunt['dairy']}.")

print("Here are the iteams that we did not find:")

for item in items_to_find:
    hunt.pop (item , None ) 


for item in hunt.items():
    print(f"The {item} was hidding.")


# Exercise 2: Phonebook
# 1. Create a phonebook dictionary to list your friends and their phone numbers
#    (Don't use real phone numbers, you can make them up.)
#    Make at least 6 key value pairs in the phonebook
# 2. Define a function called search with 1 parameter - name
#    Inside the function:
# 3. Check if name is in the phonebook, if true, print the name and phone number
#    Concatenated with: "_____'s phone number is _____"
# 4. If false, print "That name is not in your phonebook"
#    and get the number from the user
#    add the name and number to the phonebook and print "Name and number added."
# 5. Get a name from the user and call the search function, passing it the name

phonebook = {
    "Malvin" : "2064766555" ,
    "David"  : "2065434411" ,
    "Kobe"   : "2065490000" ,
    "Alice"  : "2065490000" ,
    "Emma"   : "2065478900" ,
    "Frank"  : "2063334567" 
}

def search (name):
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}.")
    else: 
        print("The name is not in the phonebook ")
        new_number = input(f"Please enter {name}'s phone number:" )
        phonebook[name] = new_number
        print("Name and number added")
user_name = input("Enter a name to search :")
search(user_name)

# Exercise 3 Phonebook continued
# 1. Ask the user if they'd like to add a name and number to the phonebook y/n
# 2. While the answer is yes (y), add a name and number to the phonebook...
#    Inside the loop, get a name from the user
#    get a number from the user
#    Ask the user if they'd like to add another name and number
# 3. If the answer is no,
#    Print "Your updated phonebook"
# 4. Use a for loop to print out the phone book showing both names and numbers   

phonebook = {}
while True: 
    answer = input("Would you like to add a name and number to the phonebook? (y/n):").lower()

    if answer == 'y':
        name = input("Enter the name:")
        number = input ("Enter the phone number:")
        phonebook[name] = number 
    elif answer == 'n':
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
print("Your updated phonebook:")
for name, number in phonebook.iteams():
    print(f"{name}:{number}")