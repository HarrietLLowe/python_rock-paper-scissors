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

human_choice = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. \n")

if human_choice == "0":
  print(rock)
elif human_choice == "1":
  print(paper)
elif human_choice == "2":
  print(scissors)

print("Computer choses:")
computer_choice = random.randint(0, 2)

if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print (scissors)

if human_choice == "0" and computer_choice == 1:
  print("You win")
elif human_choice == "0" and computer_choice == 2:
  print ("You lose")
elif human_choice == "1" and computer_choice == 0:
  print ("You win")
elif human_choice == "1" and computer_choice == 2:
  print ("You lose")
elif human_choice == "2" and computer_choice == 1:
  print ("You win")
elif human_choice == "2" and computer_choice == 0:
  print ("You lose")
else:
  print("It's a draw!")
