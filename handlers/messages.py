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

    def getGroupMessages(self, gid):
        dao = MessageDAO()
        result = dao.getGroupMessages(gid)
        mapped_results = []
        for m in result:
            mapped_results.append(self.mapToDic(m))
        return jsonify(Messages=mapped_results)

    def getMessagesBySender(self, gid, pid):
        dao = MessageDAO()
        result = dao.getMessagesBySender(gid, pid)
        mapped_results = []
        for m in result:
            mapped_results.append(self.mapToDic(m))
        return jsonify(Message_by=mapped_results)
