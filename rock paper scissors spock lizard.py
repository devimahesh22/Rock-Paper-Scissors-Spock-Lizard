import random

print ("Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors")
user_wins = 0
computer_wins = 0

options = ["Rock", "Paper","Scissors", "Lizard", "Spock"]

while True:
    user_input = input("Rock, Paper, Scissors, Lizard, Spock? Press Q to quit: ").lower()
    if user_input =="q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,4)
    # rock: 0, paper:1, scissors:2, lizard:3, spock:4
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user-input == "Rock" and computer_pick == "Lizard":
        print("You won!")
        user_wins == 1
        
    elif user-input == "Paper" and computer_pick == "Rock":
          print("You won!")
          user_wins == 1
        
    elif user-input == "Scissors" and computer_pick == "Paper":
          print("You won!")
          user_wins == 1

    elif user-input == "Lizard" and computer_pick == "Spock":
          print("You won!")
          user_wins == 1

    elif user-input == "Spock" and computer_pick == "Scissors":
          print("You won!")
          user_wins == 1

    elif user-input == "Scissors" and computer_pick == "Lizard":
          print("You won!")
          user_wins == 1

    elif user-input == "Lizard" and computer_pick == "Paper":
          print("You won!")
          user_wins == 1

    elif user-input == "Paper" and computer_pick == "Spock":
          print("You won!")
          user_wins == 1

    elif user-input == "Spock" and computer_pick == "Rock":
          print("You won!")
          user_wins == 1

    elif user-input == "Rock" and computer_pick == "Scissors":
          print("You won!")
          user_wins == 1



    else: 
        print("You Lost!")
        computer_wins == 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins,"times.")
print("Goodbye!")


    