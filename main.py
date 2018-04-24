from flask import Flask, render_template
from handlers.messages import MessageHandler
from handlers.contacts import ContactHandler
from handlers.members import MemberHandler
from handlers.groups import GroupHandler
from handlers.Reactions import ReactionHandler
from handlers.users import UserHandler

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

@app.route('/groups/<int:gid>/owner')
def groupOwner(gid):
    return GroupHandler().getGroupOwner(gid)

@app.route('/users')
def users():
    return UserHandler().getAllUsers()

@app.route('/groups/<int:gid>/members')
def members(gid):
    return MemberHandler().getMembers(gid)


@app.route('/messages')
def messages():
    return MessageHandler().getAllMessages()


@app.route('/messages/by/<int:pid>')
def getMessageBySender(pid):
    return MessageHandler().getAllMessagesBySender(pid)


@app.route('/groups/<int:gid>/messages')
def get_messages_in_chat(gid):
    return MessageHandler().getGroupMessages(gid)


@app.route('/groups/<int:gid>/messages/by/<int:pid>')
def getMessageInGroupBySender(gid, pid):
    return MessageHandler().getAllMessagesInGroupBySender(gid, pid)


@app.route('/<int:pid>/contacts')
def getMyContacts(pid):
    return ContactHandler().getMyContacts(pid)


@app.route('/<int:pid>/contacts/<string:name>')
def getContactByName(pid, name):
    return ContactHandler().getContactByName(pid, name)


@app.route('/messages/<int:mid>/number-of-likes')
def number_of_likes(mid):
    return ReactionHandler().getMessageLikes(mid)


@app.route('/messages/<int:mid>/who-likes')
def get_who_liked(mid):
    return ReactionHandler().getWhoLikedMessage(mid)


@app.route('/messages/<int:mid>/number-of-dislikes')
def number_of_dislikes(mid):
    return ReactionHandler().getMessageDislikes(mid)


@app.route('/messages/<int:mid>/who-dislikes')
def get_who_disliked(mid):
    return ReactionHandler().getWhoDislikedMessage(mid)


if __name__ == '__main__':
    app.run()
