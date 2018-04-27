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

    def build_message_attributes(self, mid, content, pid, gid, date):
        result = {}
        result['mid'] = mid
        result['content'] = content
        result['pid'] = pid
        result['gid'] = gid
        result['date'] = date
        return result



    def getAllMessages(self):
        dao = MessageDAO()
        result = dao.getAllMessagesINFO()
        mapped_results = []
        for m in result:
            mapped_results.append(self.mapToDic(m))
        return jsonify(Messages=mapped_results)

    def getAllGroupMessages(self, gid):
        dao = MessageDAO()
        result = dao.getAllGroupMessages(gid)
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
        return jsonify(Message_by=mapped_results)

    def getMessageById(self, mid):
        dao = MessageDAO()
        row = dao.getMessageById(mid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def insertMessage(self, form):
        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            content = form['content']
            pid = form['pid']
            gid = form['gid']
            if content and pid and gid:
                dao = MessageDAO()
                mid = dao.insert(content, pid, gid)
                result = self.build_message_attributes(mid[0], content, pid, gid, mid[1])
                return jsonify(Message=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
