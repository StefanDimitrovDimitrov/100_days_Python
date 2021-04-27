# from flask import Flask
#
# app = Flask(__name__)
#
# def make_bold(func):
#     def wrap_func():
#         return f'<b>{func()}</b>'
#     return wrap_func
#
# def make_italic(func):
#     def wrap_func():
#         return f'<em>{func()}</em>'
#     return wrap_func
#
# def make_underline(func):
#     def wrap_func():
#         return f'<u>{func()}</u>'
#     return wrap_func
#
#
#
# @app.route('/')
# def hello_world():
#     return '<h1 style="text-align: center"> Hello, World!</h1>'\
#             '<p>This is a Paragraph</p>'\
#             '<img src="https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif" width=200>'
#
# @app.route('/bye')
# @make_bold
# @make_italic
# @make_underline
# def bye():
#     return "Bye!"
#
# # @app.route('/username/<name>')
# # def greet(name_1):
# #     return f"Hello {name_1}!"
# #
# # @app.route('/username/<path:name>') # if - /username/Stefan/1
# # def greet_1(name):
# #     return f"Hello {name}!"
# #
# # @app.route('/username/<name>/<int:number>')
# # def greet(name, number):
# #     return f"Hello {name}, you are {number} years old!"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)