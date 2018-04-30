from config.herokudbconfig import pg_config
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
        query = "SELECT * FROM messages;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageById(self, mid):
        cursor = self.conn.cursor()
        query = "SElect * FROM messages WHERE mid = %s;"
        cursor.execute(query, (mid,))
        result = cursor.fetchone()
        return result

    def getAllMessagesBySenderINFO(self, pid):
        cursor = self.conn.cursor()
        query = "SELECT * FROM messages WHERE pid = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllGroupMessagesINFO(self, gid):
        cursor = self.conn.cursor()
        query = "SELECT username, content, date " \
                "FROM messages NATURAL INNER JOIN person " \
                "WHERE gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesInGroupBySenderINFO(self, gid, pid):
        cursor = self.conn.cursor()
        query = "SELECT username, content, date " \
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

    def insert(self, content, pid, gid):
        cursor = self.conn.cursor()
        query = "INSERT INTO messages (content, pid, gid) VALUES (%s, %s, %s)" \
                "RETURNING mid, date;"
        cursor.execute(query, (content, pid, gid))
        mid = cursor.fetchone()
        self.conn.commit()
        return mid
