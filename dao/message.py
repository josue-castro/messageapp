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

    def getGroupMessagesINFO(self, gid):
        cursor = self.conn.cursor()
        query = 'SELECT * FROM messages WHERE gid = %s;'
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesInGroupBySenderINFO(self, gid, pid):
        cursor = self.conn.cursor()
        query = "SELECT * FROM messages WHERE gid = %s AND pid = %s;"
        cursor.execute(query, (gid, pid))
        result = cursor.fetchone()
        return result

    def getAllMessagesBySenderINFO(self, pid):
        cursor = self.conn.cursor()
        query = "SELECT * FROM messages WHERE pid = %s;"
        cursor.execute(query, (pid,))

    def getAllGroupMessages(self, gid):
        cursor = self.conn.cursor()
        query = "SELECT * FROM messages WHERE gid = %s;"
        cursor.execute(query, (gid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesInGroupBySenderINFO(self, gid, pid):
        cursor = self.conn.cursor()
        query = "SELECT * FROM messages WHERE pid = %s AND gid = %s;"
        cursor.execute(query, (pid, gid))
        result = []
        for row in cursor:
            result.append(row)
        return result
