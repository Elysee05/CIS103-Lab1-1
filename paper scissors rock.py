import random
playing = True
while playing:
    user_action = input("Choose your weapon (rock, paper, scissors):")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"Your weapon {user_action}")
    print(f"Kilroy's weapon {computer_action}")
    if user_action == computer_action:
        print("{user_action} Draw!")
    elif user_action == "rock" and computer_action == "scissors":
        print("You Win!")
    elif user_action == "paper" and computer_action == "rock":
        print("You Win!")
    elif user_action == "scissors" and computer_action == "paper":
        print("You Win!")
    else:
        print("K.O. You Lose")
    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        playing = False
print("Don't be afraid to come back for more")