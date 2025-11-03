
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

if u == "rock" and c == "rock":
    print("TIE GAME")
elif u == "rock" and c == "paper":
    print("COMPUTER WINS")
elif u == "rock" and c == "scissors":
    print("USER WINS")
elif u == "paper" and c == "rock":
    print("COMPUTER WINS") # OOPS
elif u == "paper" and c == "paper":
    print("TIE GAME")
elif u == "paper" and c == "scissors":
    print("USER WINS") # OOPS
elif u == "scissors" and c == "rock":
    print("COMPUTER WINS")
elif u == "scissors" and c == "paper":
    print("USER WINS")
elif u == "scissors" and c == "scissors":
    print("TIE GAME")


