import random
from flask import Flask

app = Flask(__name__)

target_number = random.randint(0, 20)


def low_link():
    list_gift_low = [
        "https://media.giphy.com/media/XJLEXP9xEJRevqXxnR/giphy.gif",
        "https://media.giphy.com/media/6MSPYu86rQHzLEdZzQ/giphy.gif",
        "https://media.giphy.com/media/Zdg7tS9JPHO1cytujy/giphy.gif",
        "https://media.giphy.com/media/ffDDmEIUS15ra/giphy.gif",
    ]
    return random.choice(list_gift_low)


def high_link():
    list_gift_high = [
        "https://media.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.gif",
        "https://media.giphy.com/media/26ufplp8yheSKUE00/giphy.gif",
        "https://media.giphy.com/media/l41lIioP4RFRmIVB6/giphy.gif",
        "https://media.giphy.com/media/mufPePT1wysiA/giphy.gif",
    ]

    return random.choice(list_gift_high)


won_url = "https://media.giphy.com/media/1dMNqVx9Kb12EBjFrc/giphy.gif"

list_color = ["blue", "red", "pink", "purple", "orange", "green", "black"]


@app.route('/')
def guess_the_number():
    return '<h1>"Guess a number between 0 and 20"</h1>' \
           '<img src="https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif" width=200>'


@app.route('/<int:number>')
def number(number):
    if number == target_number:
        return f'<h1 style="color:{random.choice(list_color)}">You found me!</h1><img src={won_url} width=500>'
    elif number < target_number:
        return f'<h1 style="color:{random.choice(list_color)}">Too low. Try again!</h1><img src={low_link()} width=500>'
    elif number > target_number:
        return f'<h1 style="color:{random.choice(list_color)}">Too high. Try again!</h1><img src={high_link()} width=500>'


if __name__ == "__main__":
    app.run(debug=True)
