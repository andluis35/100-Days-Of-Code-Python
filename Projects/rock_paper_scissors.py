import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
ROCK = 0
PAPER = 1
SCISSORS = 2

computer_choice = random.randint(ROCK, SCISSORS)
player_choice = int(input("What do you choose?\n[0] Rock\n[1] Paper\n[2] Scissors\nR: "))

print("\n---------------------------------------------------------------------------\n")
print("Computer chose:\n" + choices[computer_choice] + "\n")
print("You chose:\n" + choices[player_choice] + "\n")

if computer_choice == player_choice:
    print("DRAW!")

elif ((computer_choice == ROCK and player_choice == PAPER) or
      (computer_choice == PAPER and player_choice == SCISSORS) or
      (computer_choice == SCISSORS and player_choice == ROCK)):
    print("YOU WIN!")

elif ((computer_choice == ROCK and player_choice == SCISSORS) or
      (computer_choice == PAPER and player_choice == ROCK) or
      (computer_choice == SCISSORS and player_choice == PAPER)):
    print("YOU LOSE!")

else:
    print("Restart the game and choose a valid option.")