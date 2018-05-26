from flask import jsonify
from dao.message import MessageDAO


class MessageHandler:
    def build_message_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['content'] = row[1]
        result['pid'] = row[2]
        result['gid'] = row[3]
        result['date'] = row[4]
        result['username'] = row[5]
        return result

    def build_tagged_message_dict(self, row):
        result = {}
        result['username'] = row[0]
        result['content'] = row[1]
        result['date'] = row[2]
        result['hashtag'] = row[3]
        return result

    def build_message_attributes_with_date(self, mid, content, pid, gid, date):
        result = {}
        result['mid'] = mid
        result['content'] = content
        result['pid'] = pid
        result['gid'] = gid
        result['date'] = date
        return result

    def build_message_attributes_without_date(self, mid, content, pid, gid):
        result = {}
        result['mid'] = mid
        result['content'] = content
        result['pid'] = pid
        result['gid'] = gid
        return result

    def map_to_content(self, content):
        result = {}
        result['content'] = content
        return result

    def build_reply_dict(self, mid, reply_id):
        result = {}
        result['mid'] = mid
        result['reply'] = reply_id
        return result


    def getAllMessages(self):
        dao = MessageDAO()
        result = dao.getAllMessagesINFO()
        mapped_results = []
        for m in result:
            mapped_results.append(self.build_message_dict(m))
        return jsonify(Messages=mapped_results)

    def getMessageById(self, mid):
        dao = MessageDAO()
        row = dao.getMessageById(mid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            message = self.build_message_dict(row)
            return jsonify(Message=message)

    def getAllGroupMessages(self, gid):
        dao = MessageDAO()
        result = dao.getAllGroupMessagesINFO(gid)
        mapped_results = []
        for m in result:
            mapped_results.append(self.build_message_dict(m))
        return jsonify(Messages_in_group=mapped_results)

    def searchGroupMessages(self, gid, args):
        username = args.get("username")
        hashtag = args.get("hashtag")
        dao = MessageDAO()

        if (len(args) == 1) and username:
            message_list = dao.getAllMessagesInGroupBySenderINFO(gid, username)
        elif (len(args) == 1) and hashtag:
            message_list = dao.getAllMessagesInGroupWithHashtagINFO(gid, hashtag)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in message_list:
            result_list.append(self.build_message_dict(row))
        return jsonify(Messages=result_list)

    # def getAllMessagesBySender(self, pid):
    #     dao = MessageDAO()
    #     result = dao.getAllMessagesBySenderINFO(pid)
    #     mapped_results = []
    #     for m in result:
    #         mapped_results.append(self.build_message_dict(m))
    #     return jsonify(Messages_by=mapped_results)

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

    def searchMessages(self, args):
        group = args.get("gid")
        user = args.get("pid")
        date = args.get('date')
        dao = MessageDAO()
        message_list = []
        if (len(args) == 2) and group and user:
            message_list = dao.getAllMessagesInGroupBySenderINFO(group, user)
        elif (len(args) == 3) and group and user and date:
            message_list = dao.getMessagesByGroupPersonAndDate(group, user, date)
        elif (len(args) == 1) and user:
            message_list = dao.getAllMessagesBySenderINFO(user)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in message_list:
            result = self.build_message_dict(row)
            result_list.append(result)
            return jsonify(Messages=result_list)

    def getReplies(self, mid):
        dao = MessageDAO()
        replies = dao.getReplies(mid)
        result_list = []
        for row in replies:
            result_list.append(self.build_message_dict(row))
        return jsonify(Replies=result_list)

    def addMessage(self, gid, json):
        if len(json) >= 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            content = json['content']
            pid = json['pid']
            if content and pid:
                message_dao = MessageDAO()
                mid_date = message_dao.insertMessage(content, pid, gid)
                result = self.build_message_attributes_with_date(mid_date[0], content, pid, gid, mid_date[1])
                return jsonify(Message=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def addReplyMessage(self, gid, mid, json):
        if len(json) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            content = json['content']
            pid = json['pid']
            if content and pid:
                dao = MessageDAO()
                original_message = dao.getMessageById(mid)
                reply_message = '"RE: ' + original_message[1] + '" ' + content
                mid_date = dao.insertMessage(reply_message, pid, gid)
                result = self.build_message_attributes_with_date(mid_date[0], reply_message, pid, gid, mid_date[1])
                return jsonify(Message=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateMessage(self, mid, form):
        """Only update message content. Form should have new content"""
        dao = MessageDAO()
        if not dao.getMessageById(mid):
            return jsonify(Error="Part not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                content = form['content']
                pid = form['pid']
                gid = form['gid']
                if content:
                    dao.updateMessage(mid, content)
                    result = self.build_message_attributes_without_date(mid, content, pid, gid)
                    return jsonify(new_Message=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteMessage(self, mid):
        dao = MessageDAO()
        if not dao.getMessageById(mid):
            return jsonify(Error="Message not found."), 404
        else:
            dao.deleteMessage(mid)
            return jsonify(DeleteStatus="OK"), 200
