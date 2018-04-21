from flask import jsonify
from dao.message import MessageDAO


class MessageHandler:
    def mapToDic(self, row):
        result = {}
        result['mid'] = row[0]
        result['content'] = row[1]
        result['sendBy'] = row[2]
        result['sendTo'] = row[3]
        result['replied'] = row[4]
        result['date'] = row[5]
        return result

    def getAllMessages(self):
        dao = MessageDAO()
        result = dao.getAllMessages()
        mapped_results = []
        for m in result:
            mapped_results.append(self.mapToDic(m))
        return jsonify(Messages=mapped_results)

    def getAllGroupMessages(self, gid):
        dao = MessageDAO()
        result = dao.getGroupMessages(gid)
        mapped_results = []
        for m in result:
            mapped_results.append(self.mapToDic(m))
        return jsonify(Messages=mapped_results)

    def getAllUserMessages(self, pid):
        dao = MessageDAO()
        result = dao.getAllUserMessages()
        mapped_results = []
        for m in result:
            mapped_results.append(self.mapToDic(m))
        return jsonify(Messages=mapped_results)

    def getGroupMessagesByUser(self, gid, pid):
        dao = MessageDAO()
        result = dao.getMessagesBySender(gid, pid)
        mapped_results = []
        for m in result:
            mapped_results.append(self.mapToDic(m))
        return jsonify(Message_by=mapped_results)

    def getMessageById(self, mid):
        dao = MessageDAO()
        row = dao.getMessageById(mid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)
