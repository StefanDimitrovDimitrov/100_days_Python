# import random
# from flask import Flask
#
# app = Flask(__name__)
#
# target_number = random.randint(0, 10)
# print(target_number)
#
# list_gift_low = [
#     "https://media.giphy.com/media/XJLEXP9xEJRevqXxnR/giphy.gif",
#     "https://media.giphy.com/media/6MSPYu86rQHzLEdZzQ/giphy.gif",
#     "https://media.giphy.com/media/Zdg7tS9JPHO1cytujy/giphy.gif",
#     "https://media.giphy.com/media/ffDDmEIUS15ra/giphy.gif",
# ]
#
# list_gift_high = [
#     "https://media.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.gif",
#     "https://media.giphy.com/media/26ufplp8yheSKUE00/giphy.gif",
#     "https://media.giphy.com/media/l41lIioP4RFRmIVB6/giphy.gif",
#     "hhttps://media.giphy.com/media/mufPePT1wysiA/giphy.gif",
# ]
#
# won_url = "https://media.giphy.com/media/1dMNqVx9Kb12EBjFrc/giphy.gif"
#
# list_color = ["blue", "red", "pink", "purple", "orange", "green", "black"]
#
#
# def final_result(result):
#     if result == 'win':
#         return f'<h1 style="color:{random.choice(list_color)}">You found me!</h1><img src={won_url} width=500>'
#     elif result == 'low':
#         return f'<h1 style="color:{random.choice(list_color)}">Too low. Try again!</h1><img src={random.choice(list_gift_low)} width=500>'
#     elif result == 'high':
#         return f'<h1 style="color:{random.choice(list_color)}">Too high. Try again!</h1><img src={random.choice(list_gift_high)} width=500>'
#
#
# @app.route('/')
# def guess_the_number():
#     return '<h1>"Guess a number between 0 and 9"</h1>' \
#            '<img src="https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif" width=200>'
#
#
# @app.route('/<int:number>')
# def number(number):
#     result = ''
#     if number == target_number:
#         result = 'win'
#     elif number < target_number:
#         result = 'low'
#     elif number > target_number:
#         result = 'high'
#
#     return final_result(result)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
