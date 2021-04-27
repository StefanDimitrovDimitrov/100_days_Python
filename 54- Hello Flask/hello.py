from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
# add FLASK_APP=hello.py
# flask run
# pwd
# cd
#touch
#mkdir
#rm - rf - dealete folder
#rm - delete file 