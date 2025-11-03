
import random
# Ask the user for an input
user_choice = input("Please choose rock, paper, or scissors")
valid_choices = ['ROCK','PAPER','SCISSORS']
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
def determine_winner(u, c):
    if u == "rock" and c == "rock":
        return "TIE GAME"
    elif u == "rock" and c == "paper":
        return "COMPUTER WINS"
    elif u == "rock" and c == "scissors":
        return "USER WINS"
    elif u == "paper" and c == "rock":
        return "COMPUTER WINS" # OOPS
    elif u == "paper" and c == "paper":
        return "TIE GAME"
    elif u == "paper" and c == "scissors":
        return "USER WINS" # OOPS
    elif u == "scissors" and c == "rock":
        return "COMPUTER WINS"
    elif u == "scissors" and c == "paper":
        return "USER WINS"
    elif u == "scissors" and c == "scissors":
        return "TIE GAME"

result = determine_winner(user_choice,computer_choice)
print(result)

# TO test code, need to use assert, and capture the code into a function (refactor the code -- reorg it w/o changing the logic)

# assert determine_winner("rock","rock") == "TIE "
