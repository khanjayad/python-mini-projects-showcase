import random
print("codewithjack")
def play_game():
    item_list = ["Rock", "Paper", "Scissor"]
    user_score = 0
    comp_score = 0

    while True:
        user_choice = input("\nEnter your move (Rock, Paper, Scissor): ").capitalize()
        if user_choice not in item_list:
            print("Invalid choice! Please choose Rock, Paper, or Scissor.")
            continue

        comp_choice = random.choice(item_list)
        print(f"User choice: {user_choice}, Computer choice: {comp_choice}")

        if user_choice == comp_choice:
            print("It's a tie!")
        elif (user_choice == "Rock" and comp_choice == "Scissor") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissor" and comp_choice == "Paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            comp_score += 1

        print(f"Score -> You: {user_score}, Computer: {comp_score}")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

play_game()
