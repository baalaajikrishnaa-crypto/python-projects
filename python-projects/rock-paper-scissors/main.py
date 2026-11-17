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

# Rock, Paper, Scissors

game_images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")
print("0 = Rock, 1 = Paper, 2 = Scissors")

user = int(input("What do you choose? "))

if user < 0 or user > 2:
    print("Invalid choice!")

else:
    computer = random.randint(0, 2)

    print(f"You chose:\n{game_images[user]}")
    print(f"Computer chose:\n{game_images[computer]}")

    # Check the winner
    if user == computer:
        print("It's a draw!")
    elif (user == 0 and computer == 2) or \
         (user == 1 and computer == 0) or \
         (user == 2 and computer == 1):
        print("You win!")
    else:
        print("You lose!")