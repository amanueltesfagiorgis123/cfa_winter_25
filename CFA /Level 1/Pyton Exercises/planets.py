# Exercise 1 The planets
# 1. Create a list of the planets in our solar system 
#    (in order from closest to the sun to farthest from the sun)
# 2. Use a for loop to print the planets
# 3. Count the number of planets and print it
#    concatenated with "There are _____ planets in our solar system"
planets = ["Mercuary" , "Venus" , "Earth", "Mars" , "Jupiter" , "Saturn" , "Uranus" , "Neptune"]

for planet in planets :
    print(planet) 

num_planets = len(planets)
print(f"There are {num_planets} planets in our solar system")

#Exercise 2
# Use the index to print the following sentences:
# 1.   I live on _____.
# 2.   The closest planet to the sun is _____.
# 3.   The farthest planet from the sun is _____.
# 4.   The great red spot is on _____.
# 5.   _____ is a planet with rings of debris around it.

print(f"I live on {planets[2]}")
print(f"The colsest planet to the sun is {planets[0]}.")
print(f"The farthers planet from the sun is {planets[7]}.")
print(f"The great red spot is on {planets[4]}.")
print(f"{planets[5]} is a planet with rings of debris around it.")




# Exercise 3: What is Pluto?
# 1. Print Is Pluto a planet? 
# 2. Pretend you're a group of arguing scientists. 
#    Write an illogical if statement to check if Pluto is in the planets list
#    If true, remove Pluto from the planet list
#    If not, append Pluto to the list
# 3. Use a for loop to print the updated planet list
# 4. Consult with scientists (Internet search).
#    Print the list of planets using a for loop. If the iteration variable is Pluto,
#    break the loop and print "Pluto is not a planet!".

print("what is Pluto?")

if "Pluto" in planets == False:
    planets.append("Pluto")

else:
    planets.remove("pluto")

print("Updated list of planets : ")
for planet in planets : 
    print(planets)

print("Final planets list :")
for planet in planets:
    if planet == "Pluto":
        print("Pluto is not a planet")
    break
print(planet)

non_planets = ('Pluto' , 'Astroids' , 'Comets' , 'Moon' , 'Satelities')
solar_system = planets + non_planets

# Exercise 4
# 1. Create a new list of non-planet bodies in the solar system, including Pluto
# 2. Combine it with the planets
# 3. Use a for loop to print out all the bodies in the solar system.
# 4. When the iteration variable is equal to Sun, 
#    print a sun fact and continue the loop
for body in solar_system :
    if body == "Sun":
        print("The sun is the center of the solar system , and it is very hot to the point it will melt your flesh ")
    continue
    print(body)

   #Advanced students
# Exercise 1
# 1. Make a list of alien species
# 2. Combine the alien list with the solar system list
# 3. Print a random item from the aliens list
# 4. Pop a random item from the aliens list 
# 5. Sort the aliens list
# 6. Loop through the combined lists. Inside the loop, check the value
# of the iteration variable, if it equals a certain alien, print
# "_____ has visited earth!" then continue 
import random

print("👽ALIENS👽")

aliens= ('Martian' , 'Reptilians' , 'Nordics' , 'Insectodis') 

combined = aliens + solar_system

print("Random Alien: " , random.choice(aliens))

removed_alien = random.choice(aliens)
aliens.remove(removed_alien)
print(f"Removed Alien : {removed_alien}")

aliens.sort()
print("New aliens list : " , aliens)

for boady in combined:
    if boady == 'Martian':
        print("Martian has visted earth!")
        continue
    elif boady == 'Nordics' : 
        print("Nordics has visted earth!")
        continue 
    print(boady)
