import random

print("Rock, Paper, Scissors Game!")
user = input("Enter your choice (rock/paper/scissors): ").lower()
computer = random.choice(["rock", "paper", "scissors"])

print(f"Computer chose: {computer}")

if user == computer:
    print("It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif user == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("You lose!")
elif user == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid input!")
