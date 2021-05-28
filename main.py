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
#Rock wins against scissors; Scissors wins against paper; Paper wins against rock
import random
game_images = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. \n"))

if human_choice >= 3 or human_choice < 0:
  print("Invalid number, you lose!")
else:
  print(game_images[human_choice])
  print("Computer choses:")
  computer_choice = random.randint(0, 2)

  print(game_images[computer_choice])

  if human_choice == 0 and computer_choice == 1:
    print("You win")
  elif human_choice == 0 and computer_choice == 2:
    print ("You lose")
  elif human_choice == 1 and computer_choice == 0:
    print ("You win")
  elif human_choice == 1 and computer_choice == 2:
    print ("You lose")
  elif human_choice == 2 and computer_choice == 1:
    print ("You win")
  elif human_choice == 2 and computer_choice == 0:
    print ("You lose")
  else:
    print("It's a draw!")
