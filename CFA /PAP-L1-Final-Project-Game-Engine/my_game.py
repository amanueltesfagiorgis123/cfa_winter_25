from game_funcs import *
import game_engine

#Set this first to decide the world dimensions
set_game_size(1600, 900)
#Below is where most of your code will be written
add_background('park.jpg', horizontal_align = "center", vertical_align="bottom") 
my_text = "🎢WELCOME TO THE PARK🎢 , 60"
centered_text = my_text.center(30)
print(centered_text)
play_music("")






# WARNING: For advanced students/game requirements
# Called once per frame (there are 60 frames per second)
# DO NOT CHANGE FUNCTION NAME
def update():
    pass

#DO NOT EDIT BELOW 
game_engine.start(update)