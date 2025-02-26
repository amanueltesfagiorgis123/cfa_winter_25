# Practice Session #
# Exercise 1
# 1. Create a variable: name
# Give it a string value of any name of your choice
# 2. Print out the variable concatenated with:
# "Hello (name). It's nice to meet you."
# Use an escape character to make the second sentence appear on a new line
name = "Python"
print("Hello " + name + "\n It's nice to meet you.")
# Practice bonus
# 1. To make the output look better, add new line characters in between the exercises, like this: print('\n')
print('\n')

# Exercise 2 
# 1. Open the file story.txt and look over the text, notice the paragraph breaks.
# 2. Create 2 variables: dog_name, and story
# 3. Give dog_name a string value, any name you like.
# 4. Give story a multiline F string value. Copy the story from story.txt and paste it inside the F string.
# 5. Find all instances of the name "Nimb" inside the story and replace them with dog_name
# 6. Place end of line characters at the end of each paragraph.
# 7. Print story
# Advanced students - practice using other escape characters from this list:
# https://www.w3schools.com/python/gloss_python_escape_characters.asp
dog_name = "Max"
story = R'''The Dogleg When I was a teenager, we lived in the last house on a dead end street, surrounded by woods. The woods backed up to a golf course, specifically the fifteenth hole. Its fairway curved so golfers could not see the flag from the tee, in other words, it was a dogleg.

We had a dog named Nimb. He was named after a math game my brother and I played on our father's calculator. Nimb was a Border Collie and loved to run. He'd tear across the golf course and bark-swim in its water hazards. We tried to keep him from escaping our yard, but we weren't very good at it.

Sometimes golfers missed their shots and balls ended up in our woods . They'd try to hit high over the bend in the dogleg, but the trees were too tall for a lot of them. After Nimb passed puppyhood, we noticed that the number of golf balls in our woods began to multiply. Some even appeared on our back deck, which was, in terms of physics, an impossible shot from the tee. Who was gifting us golf balls?

One day we let Nimb escape on purpose, and followed him. We watched as he ran right to the edge of the fairway, and sat just out of sight, next to a tree. The course was busy, and with the next crack of a golfer's wooden driver, Nimb took off running. The ball landed in the middle of the fairway. Nimb scooped it up and loped back to us. He dropped the ball at our feet. He was so proud, circling around us, whole-body wiggle-waggling his tail, expecting praise. Could there be any better fetch game? 

We grabbed Nimb and ran back to our house. Before we could get inside, "we heard the screams of the golfer, Where is that rascal, that, grrrrr, that dratted black and white dog! Where is my ball!" Nimb got away with his fetch game for a long time, mostly due to the dogleg. If he sat north of the bend in the fairway, the better golfers couldn't see him retrieving their balls. They'd tee off with what they thought was a perfect shot, clear over the trees, but then round the bend to empty grass, no ball in sight. Nimb would have dropped it in the woods by then.

He collected hundreds of balls before chance sightings coalesced into rumors which coalesced into complaints. A few months after we heard the golfer scream, we received a letter threatening a fine and a call to animal welfare. We had no choice but to keep Nimb leashed up for good, but it wasn't forever. On warm summer nights, after the golfers had all gone home, we'd let him go. We'd wander behind him as he ran to and fro over the fairways, looking for golf balls.

© Copyright 2023, Lynn Schirmer. All rights reserved.'''

updated_story = story.replace("Nimb", dog_name)
print(updated_story)



# Exercise 3
# 1. Go to https://www.asciiart.eu/ and find another ascii character picture you like
# 2. Create a variable with a multiline R string value, and paste the ascii character inside the triple quotes
# 3. Print the character
picture = r''' 
^..^      /
/_/\_____/
   /\   /\
  /  \ /  \
  '''
print(picture)