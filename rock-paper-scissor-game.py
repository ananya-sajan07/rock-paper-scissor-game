import random

def get_choices():
    print("Enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    num_choice = int(input("Enter 1, 2, or 3: "))
    
    if num_choice < 1 or num_choice > 3:
        print("Invalid number. Try again.\n")
        return get_choices()

    options = ["rock", "paper", "scissors"]
    player_choice = options[num_choice - 1]
    computer_choice = random.choice(options)

    return {"player": player_choice, "computer": computer_choice}

def check_win(player, computer):
    print(f"\nYou chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"

    elif player == "rock":
        return "You win!" if computer == "scissors" else "You lose."

    elif player == "paper":
        return "You win!" if computer == "rock" else "You lose."

    elif player == "scissors":
        return "You win!" if computer == "paper" else "You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
