import random

rock_image = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_image = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_image = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock_image, paper_image, scissors_image]

# User choice:
user_choice = int( input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if user_choice == 0:
  print(game_images[0])
elif user_choice == 1:
  print(game_images[1])
elif user_choice == 2:
  print(game_images[2])
else:
  print("You chose an invalid number, try again")
  
print('')
print('')
# Computer choice:
computer_choice = random.randint(0, 2)

if computer_choice == 0:
  print(f"Computer chose:\n{game_images[0]}")
elif computer_choice == 1:
  print(f"Computer chose:\n{game_images[1]}")
elif computer_choice == 2:
  print(f"Computer chose:\n{game_images[2]}")

print('')
print('')

# Compare choices:
if user_choice == 0:
  if computer_choice == 0:
    print("It's a draw!")
  elif computer_choice == 1:
    print("You lose!")
  elif computer_choice == 2:
    print("You win!")

elif user_choice == 1:
  if computer_choice == 0:
    print("You win!")
  elif computer_choice == 1:
    print("It's a draw!")
  elif computer_choice == 2:
    print("You lose!")

elif user_choice == 2:
  if computer_choice == 0:
    print("You lose!")
  elif computer_choice == 1:
    print("You win!")
  elif computer_choice == 2:
    print("It's a draw!")

else:
  print("You typed an invalid number, you lose!")