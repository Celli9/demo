
import random

valid_choices = ['ROCK','PAPER','SCISSORS']

def determine_winner(u, c):
    if u == "rock" and c == "rock":
        return "TIE GAME"
    elif u == "rock" and c == "paper":
        return "COMPUTER WINS"
    elif u == "rock" and c == "scissors":
        return "USER WINS"
    elif u == "paper" and c == "rock":
        return "USER WINS" # OOPS
    elif u == "paper" and c == "paper":
        return "TIE GAME"
    elif u == "paper" and c == "scissors":
        return "COMPUTER WINS" # OOPS
    elif u == "scissors" and c == "rock":
        return "COMPUTER WINS"
    elif u == "scissors" and c == "paper":
        return "USER WINS"
    elif u == "scissors" and c == "scissors":
        return "TIE GAME"
    


if __name__ == "__main__":

    # only run the code below if we are running the script from the CLI, but not if we are just trying to import stuff from the file

    # Ask the user for an input
    user_choice = input("Please choose rock, paper, or scissors")

    print(f"You chose {user_choice}")
    # Validate
    user_choice = user_choice.upper()

    if user_choice not in valid_choices:
        print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
        quit()

    # Generate random computer choice

    computer_choice = random.choice(valid_choices)
    print(f"Computer Choice: {computer_choice}")

    #Determine the winner
    u = user_choice
    c = computer_choice


    result = determine_winner(u,c)
    print(result)

# TO test code, need to use assert, and capture the code into a function (refactor the code -- reorg it w/o changing the logic)

# assert determine_winner("rock","rock") == "TIE "
