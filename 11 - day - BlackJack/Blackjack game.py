import random
from art import logo


def play():
    answer = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if answer == "y":
        return blackjack()
    else:
        return


def blackjack():

    def random_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def final_hand():
        return f"Your final hand: {user_cards}, final score: {total_user}\nComputer's final hand: {computer_cards}, final score: {total_computer}"

    def check_the_winner():
        if total_user == total_computer:
            return f"The game is draw.\U0001F643"
        elif total_user == 21:
            return f"You win with a Blackjack!!! \U0001f600"
        elif total_computer == 21:
            return f"You opponent win with a Blackjack!!! \U0001F62D"
        elif total_user > total_computer and total_user < 21:
            return f"You win! \U0001f600"
        elif total_user > total_computer and total_user > 21:
            return f"You went over. You lose. \U0001F62D"  # to do krining emotoecon
        elif total_computer > total_user and total_computer <= 21:
            return f"You lose. \U0001F62D"
        elif total_computer > total_user and total_computer >= 21:
            return f"Opponent went over. You win! \U0001f600"

    def check_for_ACE():
        if total_user > 21 and 11 in user_cards:
            user_cards[user_cards.index(11)] = 1
        if total_computer > 21 and 11 in computer_cards:
            computer_cards[computer_cards.index(11)] = 1

    user_cards = []
    computer_cards = []
    is_finish = False
    print(logo)
    user_cards.append(random_card())
    computer_cards.append(random_card())
    computer_cards.append(random_card())


    while True:
        user_cards.append(random_card())
        total_user = sum(user_cards)
        total_computer = sum(computer_cards)

        check_for_ACE()

        total_user = sum(user_cards)
        total_computer = sum(computer_cards)

        print(f"Your cards: {user_cards}, current score: {total_user} ")
        print(f"Computer's first card: {computer_cards[0]}")

        if total_user >= 21:
            print(final_hand())
            print(check_the_winner())
            is_finish = True
            break

        pass_continue = input("Type 'y' to get another card, type 'n' to pass: ")

        if pass_continue == "n":
            break

    if not is_finish:
        while total_computer <= 17:
            computer_cards.append(random_card())
            check_for_ACE()
            total_computer = sum(computer_cards)

        print(final_hand())
        print(check_the_winner())
        play()
    else:
        play()

play()
