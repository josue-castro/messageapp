from flask import Flask, render_template
from handlers.messages import MessageHandler
from handlers.contacts import ContactHandler
from handlers.groups import GroupHandler

app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    return "Welcome to Message App"


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/groups')
def groups():
    return GroupHandler().getAllGroups()


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
