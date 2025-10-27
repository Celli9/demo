
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
print("TO DO LATER")