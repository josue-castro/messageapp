# heroku Password: 3b884db910a7ed97661a75d3203b101e7bf41248fb6c8b36d39ff02dc1556fd5

from flask import Flask, jsonify, request
from handlers.messages import MessageHandler
from handlers.groups import GroupHandler
from handlers.reactions import ReactionHandler
from handlers.users import UserHandler
from handlers.members import MemberHandler
from handlers.contacts import ContactHandler
from handlers.dashboard import DashboardHandler
from flask_cors import CORS, cross_origin

app = Flask(__name__, template_folder='template')

CORS(app)

@app.route('/')
def home():
    return "Welcome to Message App"


@app.route('/MessageApp/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return UserHandler().insertUser(request.json)
    else:
        return "Register"


@app.route('/MessageApp/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return UserHandler().UserLogin(request.json)
    else:
        return "Login"


@app.route('/MessageApp/users', methods=['GET'])
def users():
    if request.method == 'GET':
        if not request.args:
            return UserHandler().getAllUsers()
        else:
            return UserHandler().searchUser(request.args)


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
    elif request.method == 'POST':
        return ContactHandler().insertContact(pid, request.json)


@app.route('/MessageApp/users/<int:pid>/mygroups', methods=['GET', 'POST'])
def getUserGroups(pid):
    if request.method == 'GET':
        return UserHandler().getUserGroups(pid)
    elif request.method == 'POST':
        return GroupHandler().createGroup(pid, request.json)


@app.route('/MessageApp/users/<int:pid>/mygroups/admin', methods=['GET', 'POST'])
def getAllGroupsAdminByUser(pid):
    if request.method == 'GET':
        if not request.args:
            return GroupHandler().getAllGroupsAdminByUser(pid)
    elif request.method == 'POST':
        return MemberHandler().addMember(pid, request.json)


@app.route('/MessageApp/groups')
def groups():
    return GroupHandler().getAllGroupsINFO()

@app.route('/MessageApp/groups/<int:gid>')
def getGroupById(gid):
    return GroupHandler().getGroupByIdINFO(gid)


@app.route('/MessageApp/groups/<int:gid>/admin')
def getGroupAdmin(gid):
    return GroupHandler().getGroupAdminInfo(gid)


@app.route('/MessageApp/groups/<int:gid>/members')
def getGroupMembers(gid):
    return GroupHandler().getGroupMembersINFO(gid)


@app.route('/MessageApp/groups/<int:gid>/messages', methods=['GET', 'POST'])
def getMessagesInChat(gid):
    if request.method == 'GET':
        if not request.args:
            return MessageHandler().getAllGroupMessages(gid)
        else:
            return MessageHandler().searchGroupMessages(gid, request.args)
    elif request.method == 'POST':
        return MessageHandler().addMessage(gid, request.json)


@app.route('/MessageApp/groups/<int:gid>/messages/<int:mid>', methods=['GET', 'POST'])
def getMessageInGroup(gid, mid):
    if request.method == 'GET':
        return MessageHandler().getMessageById(mid)
    elif request.method == 'POST':
        return MessageHandler().addReplyMessage(gid, mid, request.json)


@app.route('/MessageApp/messages', methods=['GET', 'POST'])
def getAllMessages():
    if request.method == 'GET':
        if not request.args:
            return MessageHandler().getAllMessages()
        else:
            return MessageHandler().searchMessages(request.args)
    # elif request.method == 'POST':
    #     return MessageHandler().addMessage(request.json)


@app.route('/MessageApp/messages/<int:mid>/likes', methods=['GET', 'POST'])
def likes(mid):
    if request.method == 'GET':
        if not request.args:
            return ReactionHandler().getMessageLikes(mid)
        else:
            return ReactionHandler().getWhoLikedMessage(mid, request.args)
    elif request.method == 'POST':
        return ReactionHandler().like(mid, request.json)


@app.route('/MessageApp/messages/<int:mid>/dislikes', methods=['GET', 'POST'])
def dislikes(mid):
    if request.method == 'GET':
        if not request.args:
            return ReactionHandler().getMessageDislikes(mid)
        else:
            return ReactionHandler().getWhoDislikedMessage(mid, request.args)
    elif request.method == 'POST':
        return ReactionHandler().dislike(mid, request.json)


@app.route('/MessageApp/messages/<int:mid>', methods=['GET', 'PUT', 'DELETE'])
def getMessageById(mid):
    if request.method == 'GET':
        return MessageHandler().getMessageById(mid)
    elif request.method == 'PUT':
        return MessageHandler().updateMessage(mid, request.form)
    elif request.method == 'DELETE':
        return MessageHandler().deleteMessage(mid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/MessageApp/messages/<int:mid>/replies')
def getMessageReplies(mid):
    return MessageHandler().getReplies(mid)


# @app.route('/MessageApp/messages/<int:mid>/number-of-likes')
# def number_of_likes(mid):
#     return ReactionHandler().getMessageLikes(mid)
#
#
# @app.route('/MessageApp/messages/<int:mid>/who-likes')
# def get_who_liked(mid):
#     return ReactionHandler().getWhoLikedMessage(mid)


# @app.route('/MessageApp/messages/<int:mid>/number-of-dislikes')
# def number_of_likes(mid):
#     return ReactionHandler().getMessageDislikes(mid)
#
#
# @app.route('/MessageApp/messages/<int:mid>/who-dislikes')
# def get_who_disliked(mid):
#     return ReactionHandler().getWhoDislikedMessage(mid)


# @app.route('/MessageApp/messages/hashtag/<string:tag>')
# def getAllMessagesWithHashtag(tag):
#     return MessageHandler().getAllMessagesWithHashtag(tag)


@app.route("/MessageApp/dashboard/toptenhashtags")
def trendingHashtags():
    return DashboardHandler().topTenHashtags()


@app.route('/MessageApp/dashboard/dailymessages')
def dailyMessages():
    return DashboardHandler().messagesPerDay()


@app.route("/MessageApp/dashboard/dailyreplies")
def dailyReplies():
    return DashboardHandler().repliesPerDay()


@app.route("/MessageApp/dashboard/dailylikes")
def dailyLikes():
    return DashboardHandler().likesPerDay()


@app.route("/MessageApp/dashboard/dailydislikes")
def dailyDisikes():
    return DashboardHandler().dislikesPerDay()


@app.route("/MessageApp/dashboard/todaystopusers")
def topUsers():
    return DashboardHandler().topActiveUsers()


if __name__ == '__main__':
    app.run()
