from config.herokudbconfig import pg_config
from dao.reaction import ReactionDAO
import psycopg2


class MessageDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['dbname'],
                                                                            pg_config['user'],
                                                                            pg_config['password'],
                                                                            pg_config['port'],
                                                                            pg_config['host'])

        self.conn = psycopg2.connect(connection_url)

    def getAllMessagesINFO(self):
        cursor = self.conn.cursor()
        query = "SELECT mid, content, pid, gid, date, username FROM messages NATURAL INNER JOIN person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageById(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT mid, content, pid, gid, date, username FROM messages NATURAL INNER JOIN person WHERE mid = %s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    def getAllMessagesBySenderINFO(self, pid):
        cursor = self.conn.cursor()
        query = "SELECT mid, content, pid, gid, date, username FROM messages NATURAL INNER JOIN person WHERE pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllGroupMessagesINFO(self, gid):
        cursor = self.conn.cursor()
        query = "SELECT mid, content, pid, gid, date, username " \
                "FROM messages NATURAL INNER JOIN person " \
                "WHERE gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesInGroupBySenderINFO(self, gid, pid):
        cursor = self.conn.cursor()
        query = "SELECT mid, content, pid, gid, date, username " \
                "FROM messages NATURAL INNER JOIN person " \
                "WHERE pid = %s AND gid = %s;"
        cursor.execute(query, (pid, gid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesWithHashtagINFO(self, tag):
        cursor = self.conn.cursor()
        query = "SELECT username, content, date, tag " \
                "FROM tagged NATURAL INNER JOIN hashtag NATURAL INNER JOIN person NATURAL INNER JOIN messages " \
                "WHERE tag = %s;"
        cursor.execute(query, (tag,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesInGroupWithHashtagINFO(self, gid, tag):
        cursor = self.conn.cursor()
        query = "SELECT username, content, date, tag " \
                "FROM tagged NATURAL INNER JOIN hashtag NATURAL INNER JOIN person NATURAL INNER JOIN messages " \
                "WHERE messages.gid = %s AND tag = %s;"
        cursor.execute(query, (gid, tag,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByGroupPersonAndDate(self, gid, pid, date):
        cursor = self.conn.cursor()
        query = "SELECT * " \
                "FROM messages " \
                "WHERE gid = %s AND pid = %s AND date = %s;"
        cursor.execute(query, (gid, pid, date))
        result = cursor.fetchone()
        return result

    def getReplies(self, mid):
        cursor = self.conn.cursor()
        query = "SELECT mid, content, pid, gid, date " \
                "FROM replies NATURAL INNER JOIN messages " \
                "WHERE mid = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertMessage(self, content, pid, gid):
        cursor = self.conn.cursor()
        query = "INSERT INTO messages (content, pid, gid) VALUES (%s, %s, %s)" \
                "RETURNING mid, date;"
        cursor.execute(query, (content, pid, gid))
        mid_date = cursor.fetchone()
        self.conn.commit()
        reaction_dao = ReactionDAO()
        hashtags = set(tag[1:] for tag in content.split() if tag.startswith("#"))
        for tag in hashtags:
            hid = reaction_dao.getTagId(tag)
            if not hid:
                hid = reaction_dao.createHashtag(tag)
                reaction_dao.insertTag(mid_date[0], hid)
            else:
                reaction_dao.insertTag(mid_date[0], hid)
        return mid_date

    def deleteMessage(self, mid):
        cursor = self.conn.cursor()
        query = "DELETE FROM messages WHERE mid = %s;"
        cursor.execute(query, (mid,))
        self.conn.commit()
        return mid

    def updateMessage(self, mid, content):
        cursor = self.conn.cursor()
        query = "UPDATE messages SET content = %s " \
                "WHERE mid = %s;"
        cursor.execute(query, (content, mid))
        self.conn.commit()
        return mid

    def updateMessageInfo(self, mid, content, pid, gid):
        cursor = self.conn.cursor()
        query = "UPDATE messages SET content = %s, pid = %s, gid = %s " \
                "WHERE mid = %s;"
        cursor.execute(query, (content, pid, gid, mid))
        self.conn.commit()
        return mid

    def insertReply(self, mid, reply_id):
        cursor = self.conn.cursor()
        query = "INSERT INTO replies (mid, reply_id) " \
                "VALUES (%s, %s);"
        cursor.execute(query, (mid, reply_id))
        self.conn.commit()
        return mid

    def deleteReply(self, mid):
        cursor = self.conn.cursor()
        query = "DELETE FROM replies WHERE mid = %s;"
        cursor.execute(query, (mid,))
        self.conn.commit()
        return mid