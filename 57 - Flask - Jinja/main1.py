from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Start The game type in the url /guess/your name</h1>"


@app.route('/guess/<name>')
def guess(name):
    guess_name = name.capitalize()

    response_name = requests.get(f'https://api.agify.io?name={guess_name}')
    data = response_name.json()
    age = data['age']

    response_name = requests.get(f'https://api.genderize.io?name={guess_name}')
    data = response_name.json()
    sex = data['gender']

    return render_template('index1.html', name=guess_name, sex=sex, age=age)


if (__name__) == "__main__":
    app.run(debug=True)
