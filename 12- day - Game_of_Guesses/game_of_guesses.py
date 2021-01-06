import random
from logo import logo

print("Welcome to the Game of Numbers")
print("I'am thinking of a number between 1 and 100.")
print("level of difficylty is 5 guesses for HARD and 10 guesses for EASY")

COMPUTER_NUMBER = random.randint(1, 100)
HARD = 5
EASY = 10


def game_of_numbers(difficulty_level):
    global COMPUTER_NUMBER
    while difficulty_level != 0:
        print(f"You have {difficulty_level} attempts remaining to guess the number ")
        user_guess = int(input("Make a guess: "))
        if user_guess == COMPUTER_NUMBER:
            print("You guess the number. You win.")
            break
        elif user_guess > COMPUTER_NUMBER:
            print("Too high.")
        else:
            print("Too low.")

        difficulty_level -= 1
        if difficulty_level != 0:
            print("Guss again")
        else:
            print("You've run out of guesses, you lose.")
            print(f"The number is: {COMPUTER_NUMBER}")
            break

print(logo)
difficulty_level_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty_level_choice == "hard":
    difficulty_level = HARD
else:
    difficulty_level = EASY

game_of_numbers(difficulty_level)
