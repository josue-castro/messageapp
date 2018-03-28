from flask import Flask
from handlers.messages import MessageHandler
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"

@app.route('/login')
def login():
    return "Login page"

@app.route('/groups')
def groups():
    return 0

@app.route('/groups/<int:gid>/members')
def members():
    return 0

@app.route('/group/<int:gid>/messages')
def getGroupMessages(gid):
    return MessageHandler().getGroupMessages(gid)


@app.route('/contacts')
def contacts():
    return 0


if __name__ == '__main__':
    app.run()
