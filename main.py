# heroku Password: 3b884db910a7ed97661a75d3203b101e7bf41248fb6c8b36d39ff02dc1556fd5

from flask import Flask, render_template, jsonify, request
from handlers.messages import MessageHandler
from handlers.groups import GroupHandler
from handlers.reactions import ReactionHandler
from handlers.users import UserHandler
from flask_cors import CORS

app = Flask(__name__, template_folder='template')

CORS(app)

@app.route('/')
def home():
    return "Welcome to Message App"


@app.route('/MessageApp/register', methods=['POST'])
def register():
    if request.method == 'POST':
        return UserHandler().insertUser(request.json)


@app.route('/MessageApp/login', methods=['POST'])
def login():
    if request.method == 'POST':
        return UserHandler().UserLogin(request.json)


@app.route('/MessageApp/users', methods=['GET'])
def users():
    if request.method == 'GET':
        if not request.args:
            return UserHandler().getAllUsers()
        else:
            return UserHandler().searchUser(request.args)


# @app.route('/MessageApp/users/<string:username>')
# def getUserByUsername(username):
#     return UserHandler().getUserByUsername(username)

# @app.route('/MessageApp/users/<string:firstName>-<string:lastName>')
# def getUserSearchByName(firstName, lastName):
#     return UserHandler().getUserSearchByName(firstName, lastName)


@app.route('/MessageApp/users/<int:pid>', methods=['GET', 'PUT'])
def getUserById(pid):
    if request.method == 'GET':
        return UserHandler().getUserById(pid)


@app.route('/MessageApp/users/<int:pid>/contacts', methods=['GET', 'POST'])
def getMyContacts(pid):
    if request.method == 'GET':
        if not request.args:
            return UserHandler().getUserContacts(pid)
        else:
            return UserHandler().searchContacts(pid, request.args)

# @app.route('/MessageApp/users/<int:pid>/contacts/<string:firstName>-<string:lastName>')
# def getUserContactsByName(pid,firstName, lastName):
#     return UserHandler().getUserContactsByName(pid, firstName, lastName)


@app.route('/MessageApp/users/<int:pid>/mygroups')
def getUserGroups(pid):
    return UserHandler().getUserGroups(pid)


@app.route('/MessageApp/users/<int:pid>/mygroups/admin')
def getAllGroupsAdminByUser(pid):
    return GroupHandler().getAllGroupsAdminByUser(pid)


@app.route('/MessageApp/groups')
def groups():
    return GroupHandler().getAllGroupsINFO()

@app.route('/MessageApp/groups/<int:gid>')
def getGroupById(gid):
    return GroupHandler().getGroupByIdINFO(gid)


@app.route('/MessageApp/groups/<int:gid>/members')
def getGroupMembers(gid):
    return GroupHandler().getGroupMembersINFO(gid)


@app.route('/MessageApp/groups/<int:gid>/messages', methods=['GET', 'POST'])
def get_messages_in_chat(gid):
    if request.method == 'GET':
        if not request.args:
            return MessageHandler().getAllGroupMessages(gid)
        else:
            return MessageHandler().searchGroupMessages(gid, request.args)


@app.route('/MessageApp/groups/<int:gid>/messages/by/<int:pid>')
def getMessageInGroupBySender(gid, pid):
    return MessageHandler().getAllMessagesInGroupBySender(gid, pid)


@app.route('/MessageApp/groups/<int:gid>/messages/hashtag/<string:tag>')
def getAllMessagesInGroupWithHashtag(gid, tag):
    return MessageHandler().getAllMessagesInGroupWithHashtag(gid, tag)


@app.route('/MessageApp/messages', methods=['GET', 'POST'])
def getAllMessages():
    if request.method == 'POST':
        return MessageHandler().addMessage(request.form)
    else:
        return MessageHandler().getAllMessages()


@app.route('/MessegeApp/messages/<int:mid>', methods=['GET', 'PUT', 'DELETE'])
def getMessageById(mid):
    if request.method == 'GET':
        return MessageHandler().getMessageById(mid)
    elif request.method == 'PUT':
        return MessageHandler().updateMessage(mid, request.form)
    elif request.method == 'DELETE':
        return MessageHandler().deleteMessage(mid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/MessageApp/messages/by/<int:pid>')
def getMessageBySender(pid):
    return MessageHandler().getAllMessagesBySender(pid)

@app.route('/MessageApp/messages/<int:mid>/replies')
def getMessageReplies(mid):
    return MessageHandler().getReplies(mid)


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
