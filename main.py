from flask import Flask
from handler.groups import GroupHandler

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"

@app.route('/login')
def login():
    return "No Login  for you!!!"

@app.route('/groups')
def groups():
    return GroupHandler.getAllGroups()

@app.route('/groups/<int:gid>/members')
def members():
    return 0

@app.route('/groups/<int:gid>/messages')
def messages():
    return 0

@app.route('/contacts')
def contacts():
    return 0


if __name__ == '__main__':
    app.run()
