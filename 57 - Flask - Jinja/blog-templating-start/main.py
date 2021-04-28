from flask import Flask, render_template, url_for
from post import Post


app = Flask(__name__)


@app.route('/')
def all_questions():
    data = Post()
    list_questions = data.get_q()
    return render_template("index.html",posts=list_questions)


@app.route('/question/<num>')
def new_q(num):
    data = Post()
    questions = data.get_q()
    question = [question for question in questions if question["id"] == num]

    return render_template("post.html", answer=question[0])


if __name__ == "__main__":
    app.run(debug=True)
#
