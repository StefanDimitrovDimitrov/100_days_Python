from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

# add FLASK_APP=hello.py
# flask run
# pwd
# cd
#touch
#mkdir
#rm - rf - dealete folder
#rm - delete file 