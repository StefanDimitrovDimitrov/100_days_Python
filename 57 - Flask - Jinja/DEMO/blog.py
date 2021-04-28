from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

url_Qs = 'https://api.npoint.io/f00bece59a4fa785a3ae'

@app.route('/')
def home():
    return render_template('blog.html')


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get(url_Qs)
    data = response.json()
    return render_template("blog.html",posts=data)


if __name__ == "__main__":
    app.run(debug=True)
