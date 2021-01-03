from art import logo

# how to clean the screen after the first loop?
print(logo)

print("Welcome to the secret auction program")

new_participant = {}
repeat = True

def find_the_winner(new_participant):
    winner = ''
    bid = 0
    for name in new_participant:
        if new_participant[name] > bid:
            bid = new_participant[name]
            winner = name
    print(f"The winner is {winner} with a bid of ${bid}.")

while repeat:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    new_participant[name] = bid
    other = input("Are there any other bidders? Type 'yes' or 'no'.: ").lower()
    if other == "yes":
        repeat = True

    elif other == "no":
        repeat = False
        find_the_winner(new_participant)


