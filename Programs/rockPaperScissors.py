import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    print("computer: ", computer)
    print("player: ", player)

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
        if computer == "paper":
            print("You lose!")
    elif player == "paper":
        if computer == "rock":
            print("You win!")
        if computer == "scissors":
            print("You lose!")
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
        if computer == "rock":
            print("You lose!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!")
