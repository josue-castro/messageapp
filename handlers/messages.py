from flask import jsonify
from dao.message import MessageDAO


class MessageHandler:
    def build_message_info_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['content'] = row[1]
        result['pid'] = row[2]
        result['gid'] = row[3]
        result['date'] = row[4]
        return result

    def build_message_dict(self, row):
        result = {}
        result['username'] = row[0]
        result['content'] = row[1]
        result['date'] = row[2]
        return result

    def build_tagged_message_dict(self, row):
        result = {}
        result['username'] = row[0]
        result['content'] = row[1]
        result['date'] = row[2]
        result['hashtag'] = row[3]
        return result

    def build_message_attributes(self, mid, content, pid, gid, date):
        result = {}
        result['mid'] = mid
        result['content'] = content
        result['pid'] = pid
        result['gid'] = gid
        result['date'] = date
        return result

    def build_reply_dict(self, mid, reply_id):
        result = {}
        result['mid'] = mid
        result['reply']



    def getAllMessages(self):
        dao = MessageDAO()
        result = dao.getAllMessagesINFO()
        mapped_results = []
        for m in result:
            mapped_results.append(self.build_message_info_dict(m))
        return jsonify(Messages=mapped_results)

    def getMessageById(self, mid):
        dao = MessageDAO()
        row = dao.getMessageById(mid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            message = self.build_message_info_dict(row)
            return jsonify(Message=message)

    def getAllGroupMessages(self, gid):
        dao = MessageDAO()
        result = dao.getAllGroupMessagesINFO(gid)
        mapped_results = []
        for m in result:
            mapped_results.append(self.build_message_dict(m))
        return jsonify(Messages_in_group=mapped_results)

    def getAllMessagesBySender(self, pid):
        dao = MessageDAO()
        result = dao.getAllMessagesBySenderINFO(pid)
        mapped_results = []
        for m in result:
            mapped_results.append(self.build_message_info_dict(m))
        return jsonify(Messages_by=mapped_results)

    def getAllMessagesInGroupBySender(self, gid, pid):
        dao = MessageDAO()
        result = dao.getAllMessagesInGroupBySenderINFO(gid, pid)
        mapped_results = []
        for m in result:
            mapped_results.append(self.build_message_dict(m))
        return jsonify(Message_by=mapped_results)

    def getAllMessagesWithHashtag(self, hid):
        dao = MessageDAO()
        message_list = dao.getAllMessagesWithHashtagINFO(hid)
        result_list = []
        for row in message_list:
            result_list.append(self.build_tagged_message_dict(row))
        return jsonify(Messages=result_list)

    def getAllMessagesInGroupWithHashtag(self, gid, hid):
        dao = MessageDAO()
        message_list = dao.getAllMessagesInGroupWithHashtagINFO(gid, hid)
        result_list = []
        for row in message_list:
            result_list.append(self.build_tagged_message_dict(row))
        return jsonify(Messages=result_list)

    def getReplies(self, mid):
        dao = MessageDAO()
        replies = dao.getReplies(mid)
        result_list = []
        for row in replies:
            result_list.append(self.build_message_info_dict(row))
        return jsonify(Replies=result_list)

    def addMessage(self, form):
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            content = form['content']
            pid = form['pid']
            gid = form['gid']
            if content and pid and gid:
                dao = MessageDAO()
                mid_date = dao.insertMessage(content, pid, gid)
                result = self.build_message_attributes(mid_date[0], content, pid, gid, mid_date[1])
                return jsonify(Message=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteMessage(self, mid):
        dao = MessageDAO()
        if not dao.getMessageById(mid):
            return jsonify(Error="Message not found."), 404
        else:
            dao.deleteMessage(mid)
            return jsonify(DeleteStatus="OK"), 200
