import random
from art import logo, vs
from game_data import data


def first_random(first):
    return f"Campare A: {first['name']}, a {first['description']}, from {first['country']}."


def second_random(second):
    return f"Against B: {second['name']}, a {second['description']}, from {second['country']}."


def current_winner(first, second):
    if first['follower_count'] > second["follower_count"]:
        winner = "a"
    else:
        winner = "b"
    return winner


def the_game():
    print(first_random(first))
    print(vs)
    print(second_random(second))


print(logo)
current_score = 0
answer = ''
first = random.choice(data)
while True:
    while True:
        second = random.choice(data)
        if first != second:
            break
    the_game()
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    # replit.clear()
    print(logo)
    if answer == current_winner(first, second):
        current_score += 1
        print(f"You're right.Current score: {current_score}.")
        first = second
    else:
        # replit.clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {current_score}")
        break
