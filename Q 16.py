Q 16) Rock-Paper-Scissors: Use dict for choices, loop 5 rounds with random (import random), 
track wins with set.



# Program to play Rock-Paper-Scissors for 5 rounds

import random

# Dictionary for choices
choices = {1: "rock", 2: "paper", 3: "scissors"}

player_wins = set()   # to store rounds player won
computer_wins = set() # to store rounds computer won

round_number = 1

# Play 5 rounds
while round_number <= 5:
    print("\nRound", round_number)

    # Random choice for player and computer
    player_choice = random.randint(1, 3)
    computer_choice = random.randint(1, 3)

    print("Player chose:", choices[player_choice])
    print("Computer chose:", choices[computer_choice])

    # Check result
    if player_choice == computer_choice:
        print("Result: Tie")

    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        print("Result: Player wins this round")
        player_wins.add(round_number)

    else:
        print("Result: Computer wins this round")
        computer_wins.add(round_number)

    round_number = round_number + 1

# Print final results
print("\nPlayer won rounds:", player_wins)
print("Computer won rounds:", computer_wins)



OUTPUT : 

Round 1
Player chose: rock
Computer chose: scissors
Result: Player wins this round

Round 2
Player chose: paper
Computer chose: rock
Result: Player wins this round

Round 3
Player chose: scissors
Computer chose: scissors
Result: Tie

Round 4
Player chose: rock
Computer chose: paper
Result: Computer wins this round

Round 5
Player chose: scissors
Computer chose: rock
Result: Computer wins this round

Player won rounds: {1, 2}
Computer won rounds: {4, 5}
