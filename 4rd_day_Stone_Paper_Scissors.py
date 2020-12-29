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

list_rps = [rock, paper, scissors]
list_num = [0, 1, 2]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("Your chose:")
user_choice = list_rps[user_input - 1]
user_index = user_input - 1
print(user_choice)


random.shuffle(list_num)

computer_choice = list_rps[list_num[0]]
computer_choice_index = list_num[0]
print("Computer chose:")
print(computer_choice)

if user_index == computer_choice_index:
    print("Draw")
elif user_index > computer_choice_index:
    print("You Won")
else:
    print("You lose")