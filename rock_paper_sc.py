# In this program i am going to create a rock , paper and scissors game:
import random
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Here we are making list and we can put all the storage variable image in the one list over here
game_image = [Rock,Paper,Scissors]
user_choice = int(input("What do you want to choose 0 for rock, 1 for paper and 2 for scissors : = "))
if user_choice >= 0 and user_choice <= 2:
    print(game_image[user_choice])
computer_choice= random.randint(0,2)
print(f"computer_choice")
print(game_image[computer_choice])
if user_choice >= 3 and user_choice < 0:
    print("You type an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You wins!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")