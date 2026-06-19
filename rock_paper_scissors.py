import random

print("=== Rock Paper Scissors Game ===")

while True:
    choices = ["rock", "paper", "scissors"]

    user = input("Enter Rock, Paper, or Scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer = random.choice(choices)

    print("You took:", user)
    print("Computer took:", computer)

    if user == computer:
        print("It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
    else:
        print("Computer Wins!")

    choice = input("Do you want to continue? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you for playing!")
        break
