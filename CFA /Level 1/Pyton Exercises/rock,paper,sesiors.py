
import random

player_wins = 0 
computer_wins = 0 
num_ties = 0
num_games = 0 


def play_rps_game():
    global num_games
    name = input("Enter your name: ") 
    choices = ["Rock", "Paper", "Scissors"]

    user_choose = input(f"{name}, choose Rock, Paper, or Scissors: ")
    
    while user_choose not in choices:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choose = input(f"{name}, choose Rock, Paper, or Scissors: ")
    
    print(f"{name} chooses {user_choose}")
    
    random_choice = random.choice(choices)
    print(f"Computer chooses {random_choice}")
    
    result = play_rps_game_results(name, user_choose, random_choice)
    print(result)

    num_games += 1 

    keep_playing = (f"Would like to keep playing? : (y/n)").lower()
    return keep_playing

def play_rps_game_results(name, user_choose, random_choice):
    global computer_wins, player_wins, num_ties
    if (
        (user_choose == "Rock" and random_choice == "Scissors") or
        (user_choose == "Scissors" and random_choice == "Paper") or
        (user_choose == "Paper" and random_choice == "Rock")
    ):
        return f"{name} Wins !!!!"
    elif user_choose == random_choice:
        return "It is a tie"
    else:
        return "Computer Wins"

keep_playing = play_rps_game()
while keep_playing == "y":
    keep_playing = play_rps_game()
else:
    print("\nMatch Summary:")
    print(f"Rounds played: {num_games}")
    print(f"You won: {player_wins}")
    print(f"Computer won: {computer_wins}")
    print(f"Ties: {num_ties}")

