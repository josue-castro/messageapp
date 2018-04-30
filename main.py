from flask import Flask, render_template
from handlers.messages import MessageHandler
from handlers.contacts import ContactHandler
from handlers.members import MemberHandler
from handlers.groups import GroupHandler
from handlers.reactions import ReactionHandler
from handlers.users import UserHandler

app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    return "Welcome to Message App"


@app.route('/MessageApp/register')
def register():
    return render_template('register.html')


@app.route('/MessageApp/login')
def login():
    return render_template('login.html')


@app.route('/MessageApp/users')
def users():
    return UserHandler().getAllUsers()


@app.route('/MessageApp/users/<string:username>')
def getUserByUsername(username):
    return UserHandler().getUserByUsername(username)


@app.route('/MessageApp/users/<int:pid>/contacts')
def getMyContacts(pid):
    return UserHandler().getUserContacts(pid)


@app.route('/MessageApp/groups')
def groups():
    return GroupHandler().getAllGroupsINFO()


# @app.route('/groups/<int:gid>/owner')
# def groupOwner(gid):
#     return GroupHandler().getGroupOwner(gid)

@app.route('/MessageApp/groups/<int:gid>/members')
def getGroupMembers(gid):
    return GroupHandler().getGroupMembersINFO(gid)


@app.route('/MessageApp/groups/<int:gid>/messages')
def get_messages_in_chat(gid):
    return MessageHandler().getAllGroupMessages(gid)


@app.route('/MessageApp/groups/<int:gid>/messages/by/<int:pid>')
def getMessageInGroupBySender(gid, pid):
    return MessageHandler().getAllMessagesInGroupBySender(gid, pid)


@app.route('/MessageApp/groups/<int:gid>/messages/hashtag/<string:tag>')
def getAllMessagesInGroupWithHashtag(gid, tag):
    return MessageHandler().getAllMessagesInGroupWithHashtag(gid, tag)


@app.route('/MessageApp/messages')
def messages():
    return MessageHandler().getAllMessages()


@app.route('/MessageApp/messages/by/<int:pid>')
def getMessageBySender(pid):
    return MessageHandler().getAllMessagesBySender(pid)


@app.route('/MessageApp/<int:pid>/contacts/<string:name>')
def getContactByName(pid, name):
    return ContactHandler().getContactByName(pid, name)


@app.route('/MessageApp/messages/<int:mid>/number-of-likes')
def number_of_likes(mid):
    return ReactionHandler().getMessageLikes(mid)


@app.route('/MessageApp/messages/<int:mid>/who-likes')
def get_who_liked(mid):
    return ReactionHandler().getWhoLikedMessage(mid)


@app.route('/MessageApp/messages/<int:mid>/number-of-dislikes')
def number_of_dislikes(mid):
    return ReactionHandler().getMessageDislikes(mid)


@app.route('/MessageApp/messages/<int:mid>/who-dislikes')
def get_who_disliked(mid):
    return ReactionHandler().getWhoDislikedMessage(mid)


@app.route('/MessageApp/messages/hashtag/<string:tag>')
def getAllMessagesWithHashtag(tag):
    return MessageHandler().getAllMessagesWithHashtag(tag)


if __name__ == '__main__':
    app.run()
