from flask import Flask, request
from handler.parts import PartHandelr

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"

@app.route('/login')
def login():
    return "No Login  for you!!!"

@app.route('/groups')
def groups():

@app.route('/groups/<')

if __name__ == '__main__':
    app.run()