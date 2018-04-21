from flask import jsonify
from dao.message import MessageDAO


class MessageHandler:
    def mapToDic(self, row):
        result = {}
        result['mid'] = row[0]
        result['content'] = row[1]
        result['pid'] = row[2]
        result['gid'] = row[3]
        result['date'] = row[4]
        return result

    def getAllMessages(self):
        dao = MessageDAO()
        result = dao.getAllMessagesINFO()
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
        return jsonify(Messages_in_group=mapped_results)

    def getAllMessagesBySender(self, pid):
        dao = MessageDAO()
        result = dao.getAllMessagesBySenderINFO(pid)
        mapped_results = []
        for m in result:
            mapped_results.append(self.mapToDic(m))
        return jsonify(Messages_by=mapped_results)

    def getAllMessagesInGroupBySender(self, gid, pid):
        dao = MessageDAO()
        result = dao.getAllMessagesInGroupBySenderINFO(gid, pid)
        mapped_results = []
        for m in result:
            mapped_results.append(self.mapToDic(m))
        return jsonify(Messages_by=mapped_results)
