from flask import Flask
from handlers.messages import MessageHandler
from handlers.contacts import ContactHandler
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

@app.route('/group/<int:gid>/messages/by/<int:pid>')
def getMessageBySender(gid, pid):
    return MessageHandler().getMessagesBySender(gid, pid)

@app.route('/<int:pid>/contacts')
def getMyContacts(pid):
    return ContactHandler().getMyContacts(pid)

@app.route('/<int:pid>/contacts/<string:name>')
def getContactByName(pid, name):
    return ContactHandler().getContactByName(pid, name)


if __name__ == '__main__':
    app.run()
