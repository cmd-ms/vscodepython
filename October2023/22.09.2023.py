import random

def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = 0
    while player_choice != options:
        player_choice = str(input("Enter a choice = rock, paper, scissors: "))    
        if player_choice not in options:
            print("Incorrect choice. Please chose again.")
        else:
            break
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, Computer Chose: {computer}")
    if player == computer:
        return "Its a Tie!"
    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock, You Lose"
        else:
            return "Rock breaks scissors, You Win"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cut paper, You Lose"
        else:
            return "Paper covers rock, You Win"
    elif player == "scissors":
        if computer == "rock":
            return "Rock breaks scissors, You Lose"
        else:
            return "Scissors cut paper, You Win"
    else:
        return "Somethings gone wrong here!"
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
