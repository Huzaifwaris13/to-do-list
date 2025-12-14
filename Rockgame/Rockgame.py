import random


user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print(" Welcome to Rock Paper Scissors Game")
print("Rules:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")

while True:
    print("\nChoose one: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print(" Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    
    if user_choice == computer_choice:
        print(" It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print(" You win this round!")
        user_score += 1

    else:
        print(" Computer wins this round!")
        computer_score += 1

    
    print("\n Current Score")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n Thanks for playing!")
        print(f"Final Score → You: {user_score}, Computer: {computer_score}")
        break
